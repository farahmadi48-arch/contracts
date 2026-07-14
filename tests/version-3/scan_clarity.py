#!/usr/bin/env python3
"""
Clarity Contract Static Scanner
================================
Scans .clar files in a project for KNOWN SUSPICIOUS PATTERNS related to
common smart-contract bug classes. This is a HEURISTIC tool: every hit is
a "worth checking by hand or with a Clarinet test" flag, NOT a confirmed
bug. False positives are expected and normal.

Usage:
    python3 scan_clarity.py /path/to/project/contracts
    python3 scan_clarity.py /path/to/project/contracts --out report.md

Notes on Clarity vs. other chains:
  - Clarity auto-aborts on integer overflow/underflow at runtime, so the
    classic Solidity-style overflow bug class mostly does not apply here.
  - Clarity transactions are atomic, so naive "check-after-effect" ordering
    is usually NOT exploitable by itself (we confirmed this empirically
    earlier in this project) -- still flagged, but downgraded to LOW.
"""

import argparse
import re
import sys
from pathlib import Path
from dataclasses import dataclass, field

@dataclass
class Finding:
    file: str
    line: int
    rule: str
    severity: str
    snippet: str
    note: str

@dataclass
class Rule:
    id: str
    description: str
    severity: str
    note: str
    pattern: re.Pattern
    # optional: a second pattern that, if present nearby, downgrades/skips
    require_absent_nearby: re.Pattern = None
    context_lines: int = 6

RULES = [
    Rule(
        id="MINT_BURN_NO_AUTH_CHECK",
        description="public function performs ft-mint?/ft-burn?/stx-transfer? "
                    "but the function body has no visible authorization check "
                    "(check-is-protocol / check-is-admin / is-eq tx-sender)",
        severity="HIGH",
        note="Confirm manually: does this function need to be restricted to "
             "the protocol/DAO, or is it intentionally open (e.g. a public "
             "deposit)? If restricted, verify the check is actually present "
             "and executed before the state change.",
        pattern=re.compile(
            r"\(define-public\s*\(([a-zA-Z0-9\-]+)[^)]*\)((?:(?!\(define-public).)*?"
            r"(?:ft-mint\?|ft-burn\?|nft-mint\?|stx-transfer\?))",
            re.DOTALL,
        ),
    ),
    Rule(
        id="EFFECT_BEFORE_CHECK",
        description="a state-changing call (ft-mint?/ft-burn?/map-set/var-set) "
                    "appears to occur textually before a check-is-protocol / "
                    "check-is-admin call in the same function",
        severity="LOW",
        note="In Clarity this is usually NOT exploitable on its own because "
             "transactions are atomic and a failed check rolls back the "
             "whole call (confirmed empirically in this project). Still "
             "worth fixing for gas efficiency / best practice, but do not "
             "report as Critical/High without a concrete exploit path.",
        pattern=re.compile(
            r"\(define-public\s*\(([a-zA-Z0-9\-]+)[^)]*\)"
            r"((?:(?!\(define-public).)*?(?:ft-mint\?|ft-burn\?|map-set|var-set)"
            r"(?:(?!\(define-public).)*?check-is-(?:protocol|admin))",
            re.DOTALL,
        ),
    ),
    Rule(
        id="UNWRAP_PANIC_EXTERNAL_CALL",
        description="unwrap-panic used directly on a contract-call? result",
        severity="LOW",
        note="unwrap-panic aborts the whole transaction on error, which is "
             "often fine, but check whether a graceful (err ...) would be "
             "more appropriate here (e.g. to avoid griefing via a "
             "malicious/broken trait implementation).",
        pattern=re.compile(r"unwrap-panic\s*\(contract-call\?"),
    ),
    Rule(
        id="DIVISION_INSIDE_MULTIPLICATION",
        description="a division appears NESTED INSIDE a multiplication, i.e. "
                    "(* (/ a b) c) -- this divides first and truncates before "
                    "multiplying, which loses precision. The safer order is "
                    "(/ (* a c) b) -- multiply first, divide last.",
        severity="MEDIUM",
        note="Clarity has no fixed-point/decimal type, so truncation order "
             "matters a lot. Check who benefits from the early truncation "
             "here (protocol vs. user) -- this is the exact bug class found "
             "in real Stacks-ecosystem audits (see e.g. the Bitflow "
             "Stableswap admin-fee report).",
        pattern=re.compile(r"\(\*\s*[^()]*\([^()]*/"),
    ),
    Rule(
        id="AS_CONTRACT_WITH_CONTRACT_CALLER",
        description="contract-caller used as an argument inside an "
                    "as-contract block",
        severity="INFO",
        note="Note: as-contract overrides BOTH tx-sender and contract-caller "
             "to the contract's own principal (confirmed empirically in this "
             "project) -- this pattern is usually NOT a bug, but worth a "
             "second look if the surrounding logic assumes the ORIGINAL "
             "caller's identity.",
        pattern=re.compile(r"as-contract\s*\([^()]*contract-caller"),
    ),
    Rule(
        id="HARDCODED_MAINNET_PRINCIPAL",
        description="a hardcoded mainnet-style principal (SP...) appears in "
                    "the contract",
        severity="LOW",
        note="Check this isn't accidentally left over from mainnet in a "
             "testnet/devnet build, or vice versa -- a classic deployment "
             "mistake.",
        pattern=re.compile(r"'SP[0-9A-Z]{28,41}"),
    ),
    Rule(
        id="TX_SENDER_AUTH_CHECK",
        description="authorization check uses tx-sender directly instead of "
                    "contract-caller (or vice versa)",
        severity="MEDIUM",
        note="REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, "
             "~183,548 STX lost) happened because a function authorized "
             "based on tx-sender, and an attacker routed the call through "
             "an intermediate contract's as-contract block to make "
             "tx-sender equal a trusted principal (confused-deputy pattern). "
             "Check: (1) is this comparing tx-sender against a hardcoded/"
             "trusted principal? (2) can this function be reached through "
             "another contract that wraps the call in as-contract? If yes "
             "to both, this may be a real bypass -- verify with a Clarinet "
             "test where a proxy contract relays the call.",
        pattern=re.compile(r"is-eq\s+tx-sender\b"),
    ),
    Rule(
        id="LIST_PARAM_AGGREGATION_NO_DEDUP_CHECK",
        description="a public function takes a (list ...) parameter and the "
                    "body contains fold/map (likely aggregating a value per "
                    "list item), with no visible duplicate-detection logic",
        severity="MEDIUM",
        note="REAL-WORLD PRECEDENT: the Zest Protocol hack (April 2024, "
             "~322,000 STX / ~$1M lost) happened because a Borrow function "
             "accepted a list of up to 100 collateral assets and did not "
             "check for duplicates -- an attacker listed the same asset "
             "many times to inflate their collateral value. Check: does "
             "this function sum/aggregate a value (balance, collateral, "
             "voting power, etc.) per list entry? If so, verify duplicates "
             "in the list are rejected or naturally cannot inflate the "
             "total.",
        pattern=re.compile(
            r"\(define-public\s*\(([a-zA-Z0-9\-]+)\s*\([^)]*\(list\s"
            r"((?:(?!\(define-public).)*?(?:fold|map)\s)",
            re.DOTALL,
        ),
    ),
]

def find_matches(text: str, rule: Rule, filename: str):
    findings = []
    for m in rule.pattern.finditer(text):
        line_no = text.count("\n", 0, m.start()) + 1
        start = max(0, m.start() - 40)
        end = min(len(text), m.start() + 160)
        snippet = " ".join(text[start:end].split())
        findings.append(
            Finding(
                file=filename,
                line=line_no,
                rule=rule.id,
                severity=rule.severity,
                snippet=snippet,
                note=rule.note,
            )
        )
    return findings

def scan_project(root: Path):
    all_findings = []
    clar_files = sorted(root.rglob("*.clar"))
    if not clar_files:
        print(f"No .clar files found under {root}", file=sys.stderr)
    for f in clar_files:
        try:
            text = f.read_text(encoding="utf-8", errors="ignore")
        except Exception as e:
            print(f"Could not read {f}: {e}", file=sys.stderr)
            continue
        rel = str(f.relative_to(root))
        for rule in RULES:
            all_findings.extend(find_matches(text, rule, rel))
    return clar_files, all_findings

def write_report(clar_files, findings, out_path: Path):
    sev_order = {"HIGH": 0, "MEDIUM": 1, "LOW": 2, "INFO": 3}
    findings_sorted = sorted(
        findings, key=lambda fnd: (sev_order.get(fnd.severity, 9), fnd.file, fnd.line)
    )

    lines = []
    lines.append("# Clarity Static Scan Report\n")
    lines.append(f"Scanned **{len(clar_files)}** `.clar` files, found "
                  f"**{len(findings)}** review-worthy locations.\n")
    lines.append(
        "> ⚠️ Every item below is a HEURISTIC hint, not a confirmed bug. "
        "Verify each one manually or with a Clarinet test before drawing "
        "any conclusion or writing a report.\n"
    )

    by_sev = {}
    for fnd in findings_sorted:
        by_sev.setdefault(fnd.severity, []).append(fnd)

    for sev in ["HIGH", "MEDIUM", "LOW", "INFO"]:
        items = by_sev.get(sev, [])
        if not items:
            continue
        lines.append(f"\n## {sev} ({len(items)})\n")
        for fnd in items:
            lines.append(f"### `{fnd.file}:{fnd.line}` — {fnd.rule}")
            lines.append(f"- **Snippet:** `{fnd.snippet}`")
            lines.append(f"- **Why flagged:** {fnd.note}\n")

    out_path.write_text("\n".join(lines), encoding="utf-8")

def main():
    parser = argparse.ArgumentParser(description="Scan Clarity contracts for known suspicious patterns.")
    parser.add_argument("path", help="Path to the project root (or a folder containing .clar files)")
    parser.add_argument("--out", default="clarity_scan_report.md", help="Output report path (Markdown)")
    args = parser.parse_args()

    root = Path(args.path).resolve()
    if not root.exists():
        print(f"Path does not exist: {root}", file=sys.stderr)
        sys.exit(1)

    clar_files, findings = scan_project(root)
    out_path = Path(args.out).resolve()
    write_report(clar_files, findings, out_path)

    print(f"Scanned {len(clar_files)} files.")
    print(f"Found {len(findings)} review-worthy locations.")
    print(f"Report written to: {out_path}")

if __name__ == "__main__":
    main()