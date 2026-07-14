# Clarity Static Scan Report

Scanned **123** `.clar` files, found **412** review-worthy locations.

> ⚠️ Every item below is a HEURISTIC hint, not a confirmed bug. Verify each one manually or with a Clarinet test before drawing any conclusion or writing a report.


## HIGH (90)

### `core/ststx-token.clar:70` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `----------------------- ;; Mint method (define-public (mint-for-protocol (amount uint) (recipient principal)) (begin (try! (contract-call? .dao check-is-protocol contract-caller)) (ft-mint?`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `core/ststx-token.clar:78` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `amount recipient) ) ) ;; Burn method (define-public (burn-for-protocol (amount uint) (sender principal)) (begin (try! (contract-call? .dao check-is-protocol contract-caller)) (ft-burn? st`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `core/ststx-token.clar:86` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `amount sender) ) ) ;; Burn external (define-public (burn (amount uint)) (begin (ft-burn? ststx amount tx-sender) ) )`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `core/ststx-withdraw-nft-v2.clar:122` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `;------------------------------------- (define-public (mint-for-protocol (recipient principal)) (let ( (next-id (+ u1 (var-get last-id))) ) (try! (contract-call? .dao check-is-protocol co`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `core/ststx-withdraw-nft-v2.clar:136` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `t last-id next-id) (ok true) ) ) (define-public (burn-for-protocol (token-id uint)) (let ( (owner (unwrap! (unwrap! (get-owner token-id) (err ERR_GET_OWNER)) (err ERR_GET_OWNER))) )`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `core/ststx-withdraw-nft-v2.clar:188` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `n-ustx", id: id }) (ok true) ) ) (define-public (buy-in-ustx (id uint) (commission-contract <commission-trait>)) (let ( (owner (unwrap! (nft-get-owner? ststx-withdraw id) (err ERR_NFT_NOT`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `core/ststx-withdraw-nft.clar:123` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `;------------------------------------- (define-public (mint-for-protocol (recipient principal)) (let ( (next-id (+ u1 (var-get last-id))) ) (try! (contract-call? .dao check-is-protocol co`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `core/ststx-withdraw-nft.clar:137` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `t last-id next-id) (ok true) ) ) (define-public (burn-for-protocol (token-id uint)) (let ( (owner (unwrap! (unwrap! (get-owner token-id) (err ERR_GET_OWNER)) (err ERR_GET_OWNER))) )`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `core/ststx-withdraw-nft.clar:193` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `n-ustx", id: id }) (ok true) ) ) (define-public (buy-in-ustx (id uint) (commission-contract <commission-trait>)) (let ( (owner (unwrap! (nft-get-owner? ststx-withdraw id) (err ERR_NFT_NOT`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `core/ststxbtc-token-v2.clar:77` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `----------------------- ;; Mint method (define-public (mint-for-protocol (amount uint) (recipient principal)) (let ( (result (ft-mint? ststxbtc amount recipient)) ) (try! (contract-call?`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `core/ststxbtc-token-v2.clar:89` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `ent))) result ) ) ;; Burn method (define-public (burn-for-protocol (amount uint) (sender principal)) (let ( (result (ft-burn? ststxbtc amount sender)) ) (try! (contract-call? .dao c`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `core/ststxbtc-token-v2.clar:101` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `r))) result ) ) ;; Burn external (define-public (burn (amount uint)) (let ( (result (ft-burn? ststxbtc amount tx-sender)) ) (try! (contract-call? .ststxbtc-tracking-data-v2 set-tota`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `core/ststxbtc-token.clar:73` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `----------------------- ;; Mint method (define-public (mint-for-protocol (amount uint) (recipient principal)) (let ( (result (ft-mint? ststxbtc amount recipient)) ) (try! (contract-call?`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `core/ststxbtc-token.clar:85` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `ent))) result ) ) ;; Burn method (define-public (burn-for-protocol (amount uint) (sender principal)) (let ( (result (ft-burn? ststxbtc amount sender)) ) (try! (contract-call? .dao c`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `core/ststxbtc-token.clar:97` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `r))) result ) ) ;; Burn external (define-public (burn (amount uint)) (let ( (result (ft-burn? ststxbtc amount tx-sender)) ) (try! (contract-call? .ststxbtc-tracking-data set-total-s`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `core/ststxbtc-withdraw-nft.clar:122` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `;------------------------------------- (define-public (mint-for-protocol (recipient principal)) (let ( (next-id (+ u1 (var-get last-id))) ) (try! (contract-call? .dao check-is-protocol co`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `core/ststxbtc-withdraw-nft.clar:136` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `t last-id next-id) (ok true) ) ) (define-public (burn-for-protocol (token-id uint)) (let ( (owner (unwrap! (unwrap! (get-owner token-id) (err ERR_GET_OWNER)) (err ERR_GET_OWNER))) )`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `core/ststxbtc-withdraw-nft.clar:187` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `n-ustx", id: id }) (ok true) ) ) (define-public (buy-in-ustx (id uint) (commission-contract <commission-trait>)) (let ( (owner (unwrap! (nft-get-owner? ststxbtc-withdraw id) (err ERR_NFT_`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `genesis-nft/stacking-dao-cc-nft.clar:130` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `;------------------------------------- (define-public (mint-for-protocol (recipient principal) (type uint)) (let ( (next-id (+ u1 (var-get last-id))) ) (try! (contract-call? .dao check-is`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `genesis-nft/stacking-dao-cc-nft.clar:145` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `t last-id next-id) (ok true) ) ) (define-public (burn-for-protocol (token-id uint)) (let ( (owner (unwrap! (unwrap! (get-owner token-id) (err ERR_GET_OWNER)) (err ERR_GET_OWNER))) )`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `genesis-nft/stacking-dao-cc-nft.clar:192` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `n-ustx", id: id }) (ok true) ) ) (define-public (buy-in-ustx (id uint) (commission-contract <commission-trait>)) (let ( (owner (unwrap! (nft-get-owner? stacking-dao-nyc id) (err ERR_NFT_N`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `genesis-nft/stacking-dao-genesis-nft.clar:132` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `;------------------------------------- (define-public (mint-for-protocol (recipient principal) (type uint)) (let ( (next-id (+ u1 (var-get last-id))) ) (try! (contract-call? .dao check-is`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `genesis-nft/stacking-dao-genesis-nft.clar:147` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `t last-id next-id) (ok true) ) ) (define-public (burn-for-protocol (token-id uint)) (let ( (owner (unwrap! (unwrap! (get-owner token-id) (err ERR_GET_OWNER)) (err ERR_GET_OWNER))) )`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `genesis-nft/stacking-dao-genesis-nft.clar:194` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `n-ustx", id: id }) (ok true) ) ) (define-public (buy-in-ustx (id uint) (commission-contract <commission-trait>)) (let ( (owner (unwrap! (nft-get-owner? stacking-dao-genesis id) (err ERR_N`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `keeper-jobs/rewards-job-v1.clar:56` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `;------------------------------------- (define-public (retreive-stx-tokens (requested-stx uint) (receiver principal)) (begin (try! (contract-call? .dao check-is-protocol tx-sender)) (try!`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `keeper-jobs/tax-v1.clar:119` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `;------------------------------------- (define-public (retreive-stx-tokens (requested-stx uint) (receiver principal)) (begin (try! (contract-call? .dao check-is-protocol tx-sender)) (try!`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `nakamoto/stacking-dao-fomo-eoy-nft.clar:120` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `;------------------------------------- (define-public (mint-for-protocol (recipient principal)) (let ( (next-id (+ u1 (var-get last-id))) ) (try! (contract-call? .dao check-is-protocol co`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `nakamoto/stacking-dao-fomo-eoy-nft.clar:134` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `t last-id next-id) (ok true) ) ) (define-public (burn-for-protocol (token-id uint)) (let ( (owner (unwrap! (unwrap! (get-owner token-id) (err ERR_GET_OWNER)) (err ERR_GET_OWNER))) )`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `nakamoto/stacking-dao-fomo-eoy-nft.clar:182` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `n-ustx", id: id }) (ok true) ) ) (define-public (buy-in-ustx (id uint) (commission-contract <commission-trait>)) (let ( (owner (unwrap! (nft-get-owner? stacking-dao-fomo-eoy id) (err ERR_`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `nakamoto/stacking-dao-fomo-nft.clar:120` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `;------------------------------------- (define-public (mint-for-protocol (recipient principal)) (let ( (next-id (+ u1 (var-get last-id))) ) (try! (contract-call? .dao check-is-protocol co`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `nakamoto/stacking-dao-fomo-nft.clar:134` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `t last-id next-id) (ok true) ) ) (define-public (burn-for-protocol (token-id uint)) (let ( (owner (unwrap! (unwrap! (get-owner token-id) (err ERR_GET_OWNER)) (err ERR_GET_OWNER))) )`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `nakamoto/stacking-dao-fomo-nft.clar:182` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `n-ustx", id: id }) (ok true) ) ) (define-public (buy-in-ustx (id uint) (commission-contract <commission-trait>)) (let ( (owner (unwrap! (nft-get-owner? stacking-dao-fomo id) (err ERR_NFT_`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `tests/fake-reserve.clar:56` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `stx-amount)) (ok stx-amount) ) ) (define-public (request-stx-for-withdrawal (requested-stx uint) (receiver principal)) (begin (try! (contract-call? .dao check-is-protocol contract-caller)`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `tests/fake-reserve.clar:70` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `;------------------------------------- (define-public (request-stx-to-stack (requested-stx uint)) (let ( (receiver contract-caller) ) (try! (contract-call? .dao check-is-protocol contract`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `tests/fake-reserve.clar:83` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `ceiver))) (ok requested-stx) ) ) (define-public (return-stx-from-stacking (stx-amount uint)) (begin (try! (contract-call? .dao check-is-protocol contract-caller)) (try! (contract-call`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `tests/fake-reserve.clar:98` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `;------------------------------------- (define-public (get-stx (requested-stx uint) (receiver principal)) (begin (try! (contract-call? .dao check-is-protocol contract-caller)) (try! (as-co`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `tests/pox-3-mock.clar:44` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `-balance account) }) ) ) ) (define-public (unlock-mock (account principal)) (let ( (locked-amount (get locked (stx-account-mock account))) ) (asserts! (< (get unlo`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `tests/pox-3-mock.clar:677` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `the Stacker (tx-sender) automatically. (define-public (stack-stx (amount-ustx uint) (pox-addr (tuple (version (buff 1)) (hashbytes (buff 32)))) (st`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `tests/pox-3-mock.clar:1081` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `e `tx-sender` must already be Stacking. (define-public (stack-increase (increase-by uint)) (let ((stacker-info (stx-account-mock tx-sender)) (amount-stacked (get locked stacker-info))`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `tests/sbtc-token.clar:23` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `ient) ) ) ;; #[allow(unchecked_data)] (define-public (protocol-lock (amount uint) (owner principal)) (begin (try! (contract-call? .sbtc-registry validate-protocol-caller contract-caller)) (try!`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `tests/sbtc-token.clar:32` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `wner) ) ) ;; #[allow(unchecked_data)] (define-public (protocol-unlock (amount uint) (owner principal)) (begin (try! (contract-call? .sbtc-registry validate-protocol-caller contract-caller)) (tr`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `tests/sbtc-token.clar:41` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `wner) ) ) ;; #[allow(unchecked_data)] (define-public (protocol-mint (amount uint) (recipient principal)) (begin ;; (try! (contract-call? .sbtc-registry validate-protocol-caller contract-caller))`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `tests/sbtc-token.clar:49` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `ient) ) ) ;; #[allow(unchecked_data)] (define-public (protocol-burn (amount uint) (owner principal)) (begin ;; (try! (contract-call? .sbtc-registry validate-protocol-caller contract-caller)) (f`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `tests/sbtc-token.clar:57` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `wner) ) ) ;; #[allow(unchecked_data)] (define-public (protocol-burn-locked (amount uint) (owner principal)) (begin (try! (contract-call? .sbtc-registry validate-protocol-caller contract-caller))`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `tests/sbtc-token.clar:81` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `bol)) ) ) ;; #[allow(unchecked_data)] (define-public (protocol-set-token-uri (new-uri (optional (string-utf8 256)))) (begin (try! (contract-call? .sbtc-registry validate-protocol-caller contract-`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `tests/swap-lp-token.clar:66` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `) error (err error) ) ) ) (define-public (mint (who principal) (amount uint)) (begin (asserts! (is-eq contract-caller (var-get approved-minter)) ERR-UNAUTHORIZED-MINT) ;; amoun`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `tests/swap-lp-token.clar:76` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `mint? swap-lp-token amount who) ) ) (define-public (burn (burner principal) (amount uint)) (begin (asserts! (is-eq tx-sender burner) ERR-NOT-AUTHORIZED) (ft-burn? swap-lp-token amount bu`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `tests/wstx-token.clar:50` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `i) (ok (some (var-get token-uri))) ) (define-public (transfer (amount uint) (sender principal) (recipient principal) (memo (optional (buff 34)))) (let ( (sender-is-protocol (is-protocol-addre`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `tests/wstx-token.clar:101` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `-------------------------------------- (define-public (wrap (amount uint)) (begin (try! (stx-transfer? amount tx-sender (as-contract tx-sender))) (ft-mint? wstx amount tx-sender) ) ) (de`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `tests/wstx-token.clar:108` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `(ft-mint? wstx amount tx-sender) ) ) (define-public (unwrap (amount uint)) (let ( (recipient tx-sender) ) (try! (as-contract (stx-transfer? amount (as-contract tx-sender) recipient)))`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-1/commission-v1.clar:55` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `n is split between stakers and protocol (define-public (add-commission (staking-contract <staking-trait>) (stx-amount uint)) (let ( (amount-for-staking (/ (* stx-amount (get-staking-basispoints)`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-1/commission-v1.clar:82` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `;------------------------------------- (define-public (withdraw-commission) (let ( (receiver tx-sender) (amount (stx-get-balance (as-contract tx-sender))) ) (try! (contract-call? .dao`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-1/reserve-v1.clar:69` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `stx-amount)) (ok stx-amount) ) ) (define-public (request-stx-for-withdrawal (requested-stx uint) (receiver principal)) (begin (try! (contract-call? .dao check-is-protocol contract-caller)`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-1/reserve-v1.clar:83` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `;------------------------------------- (define-public (request-stx-to-stack (requested-stx uint)) (let ( (receiver contract-caller) ) (try! (contract-call? .dao check-is-protocol contract`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-1/reserve-v1.clar:96` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `ceiver))) (ok requested-stx) ) ) (define-public (return-stx-from-stacking (stx-amount uint)) (begin (try! (contract-call? .dao check-is-protocol contract-caller)) (try! (contract-call`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-1/reserve-v1.clar:111` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `;------------------------------------- (define-public (get-stx (requested-stx uint) (receiver principal)) (begin (try! (contract-call? .dao check-is-protocol contract-caller)) (try! (as-co`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-1/stacking-dao-core-v1.clar:152` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `------------- ;; Deposit STX for stSTX (define-public (deposit (reserve-contract <reserve-trait>) (stx-amount uint) (referrer (optional principal))) (let ( (cycle-id (get-pox-cycle)) (curre`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-1/stacking-dao-core-v1.clar:250` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `rewards management is a manual process. (define-public (add-rewards (commission-contract <commission-trait>) (staking-contract <staking-trait>) (reserve principal) (stx-amount uint) (cy`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-2/commission-v2.clar:55` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `n is split between stakers and protocol (define-public (add-commission (staking-contract <staking-trait>) (stx-amount uint)) (let ( (amount-for-staking (/ (* stx-amount (get-staking-basispoints)`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-2/commission-v2.clar:82` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `;------------------------------------- (define-public (withdraw-commission) (let ( (receiver tx-sender) (amount (stx-get-balance (as-contract tx-sender))) ) (try! (contract-call? .dao`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-2/rewards-v2.clar:70` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `an be called at the end of each cycle. (define-public (add-rewards (pool principal) (stx-amount uint) ) (let ( (commission (contract-call? .data-pools-v1 get-pool-commission pool)) (`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-2/rewards-v2.clar:98` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `mission))) (ok true) ) ) ) (define-public (process-rewards (commission-contract <commission-trait>) (staking-contract <staking-trait>) (reserve <reserve-trait>) ) (begin (`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-2/rewards-v2.clar:132` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `;------------------------------------- (define-public (get-stx (requested-stx uint) (receiver principal)) (begin (try! (contract-call? .dao check-is-protocol contract-caller)) (try! (as-co`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-2/stacking-dao-core-v2.clar:71` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `------------- ;; Deposit STX for stSTX (define-public (deposit (reserve <reserve-trait>) (commission-contract <commission-trait>) (staking-contract <staking-trait>) (direct-helpers <direc`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-2/stacking-dao-core-v2.clar:151` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `user will receive back the STX tokens. (define-public (cancel-withdraw (reserve <reserve-trait>) (direct-helpers <direct-helpers-trait>) (nft-id uint) (pool (optional principal)) ) (let (`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-2/stacking-dao-core-v3.clar:71` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `------------- ;; Deposit STX for stSTX (define-public (deposit (reserve <reserve-trait>) (commission-contract <commission-trait>) (staking-contract <staking-trait>) (direct-helpers <direc`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-2/stacking-delegate-1.clar:131` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `u0 ) (ok return-amount) ) ) (define-public (get-stx (requested-stx uint) (receiver principal)) (begin (try! (contract-call? .dao check-is-protocol contract-caller)) (try! (as-co`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-2/stacking-pool-payout-v1.clar:106` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `;------------------------------------- (define-public (deposit-rewards (amount uint) (cycle uint)) (let ( (reward-id (var-get last-reward-id)) (total-stacked (unwrap! (get-total-stacked cyc`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-2/stacking-pool-payout-v1.clar:119` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `-sender (as-contract tx-sender)) ) ) (define-public (distribute-rewards (users (list 200 principal)) (reward-id uint)) (let ( (reward-id-list (list reward-id reward-id reward-id reward-id rew`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-2/stacking-pool-payout-v1.clar:177` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `tacking-pool pool) (ok true) ) ) (define-public (get-stx (requested-stx uint) (receiver principal)) (begin (try! (contract-call? .dao check-is-protocol contract-caller)) (try! (as-co`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-3/rewards-v3.clar:108` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `;------------------------------------- (define-public (add-rewards (pool principal) (stx-amount uint) ) (let ( (commission (contract-call? .data-pools-v1 get-pool-commission pool)) (`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-3/rewards-v3.clar:180` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `;------------------------------------- (define-public (process-rewards (cycle uint) (commission-ststx-contract <commission-trait>) (commission-ststxbtc-contract <commission-trait>) (stakin`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-3/rewards-v3.clar:234` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `;------------------------------------- (define-public (get-stx (requested-stx uint) (receiver principal)) (begin (try! (contract-call? .dao check-is-protocol contract-caller)) (try! (as-co`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-3/rewards-v4.clar:102` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `;------------------------------------- (define-public (add-rewards (pool principal) (stx-amount uint) ) (let ( (commission (contract-call? .data-pools-v1 get-pool-commission pool)) (`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-3/rewards-v4.clar:202` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `ion-sbtc cycle-ststxbtc)), } ) ) (define-public (process-rewards (cycle uint) (commission-ststx-contract <commission-trait>) (commission-ststxbtc-contract <commission-trait>) (stakin`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-3/rewards-v4.clar:260` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `;------------------------------------- (define-public (get-stx (requested-stx uint) (receiver principal)) (begin (try! (contract-call? .dao check-is-protocol contract-caller)) (try! (as-co`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-3/rewards-v5.clar:110` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `;------------------------------------- (define-public (add-rewards (pool principal) (stx-amount uint) ) (let ( (commission (contract-call? .data-pools-v1 get-pool-commission pool)) (`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-3/rewards-v5.clar:210` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `ion-sbtc cycle-ststxbtc)), } ) ) (define-public (process-rewards (cycle uint) (commission-ststx-contract <commission-trait>) (commission-ststxbtc-contract <commission-trait>) (stakin`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-3/rewards-v5.clar:301` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `;------------------------------------- (define-public (get-stx (requested-stx uint) (receiver principal)) (begin (try! (contract-call? .dao check-is-protocol contract-caller)) (try! (as-co`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-3/stacking-dao-core-btc-v1.clar:88` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `---------- ;; Deposit STX for stSTXbtc (define-public (deposit (reserve <reserve-trait>) (commission-contract <commission-trait>) (staking-contract <staking-trait>) (direct-helpers <direc`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-3/stacking-dao-core-btc-v2.clar:94` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `---------- ;; Deposit STX for stSTXbtc (define-public (deposit (reserve <reserve-trait>) (commission-contract <commission-trait>) (staking-contract <staking-trait>) (direct-helpers <direc`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-3/stacking-dao-core-btc-v3.clar:94` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `---------- ;; Deposit STX for stSTXbtc (define-public (deposit (reserve <reserve-trait>) (commission-contract <commission-trait>) (staking-contract <staking-trait>) (direct-helpers <direc`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-3/stacking-dao-core-v4.clar:105` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `------------- ;; Deposit STX for stSTX (define-public (deposit (reserve <reserve-trait>) (commission-contract <commission-trait>) (staking-contract <staking-trait>) (direct-helpers <direc`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-3/stacking-dao-core-v5.clar:111` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `------------- ;; Deposit STX for stSTX (define-public (deposit (reserve <reserve-trait>) (commission-contract <commission-trait>) (staking-contract <staking-trait>) (direct-helpers <direc`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-3/stacking-dao-core-v6.clar:111` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `------------- ;; Deposit STX for stSTX (define-public (deposit (reserve <reserve-trait>) (commission-contract <commission-trait>) (staking-contract <staking-trait>) (direct-helpers <direc`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-x/sdao-token.clar:72` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `----------------------- ;; Mint method (define-public (mint-for-protocol (amount uint) (recipient principal)) (begin (try! (contract-call? .dao check-is-protocol contract-caller)) (ft-mint?`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-x/sdao-token.clar:80` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `amount recipient) ) ) ;; Burn method (define-public (burn-for-protocol (amount uint) (sender principal)) (begin (try! (contract-call? .dao check-is-protocol contract-caller)) (ft-burn? sd`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-x/sdao-token.clar:88` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `amount sender) ) ) ;; Burn external (define-public (burn (amount uint)) (begin (ft-burn? sdao amount tx-sender) ) )`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-x/staking-v1.clar:177` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `000000000)) ) (ok rewards) ) ) (define-public (claim-pending-rewards) (let ( (staker tx-sender) ) (try! (contract-call? .dao check-is-enabled)) (unwrap-panic (increase-cumm-re`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.

### `version-x/staking-v1.clar:263` — MINT_BURN_NO_AUTH_CHECK
- **Snippet:** `d by the commission contract to add STX (define-public (add-rewards (amount uint) (end-block uint)) (let ( ;; Get rewards not distributed yet (reward-blocks-left (if (< burn-block-height (va`
- **Why flagged:** Confirm manually: does this function need to be restricted to the protocol/DAO, or is it intentionally open (e.g. a public deposit)? If restricted, verify the check is actually present and executed before the state change.


## MEDIUM (61)

### `core/ststx-token.clar:44` — TX_SENDER_AUTH_CHECK
- **Snippet:** `al (buff 34)))) (begin (asserts! (is-eq tx-sender sender) (err ERR_NOT_AUTHORIZED)) (try! (ft-transfer? ststx amount sender recipient)) (print memo) (print { action: "transfer", dat`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `core/ststx-withdraw-nft-v2.clar:86` — TX_SENDER_AUTH_CHECK
- **Snippet:** `ent principal)) (begin (asserts! (is-eq tx-sender sender) (err ERR_NOT_AUTHORIZED)) (asserts! (is-none (map-get? market token-id)) (err ERR_IS_LISTED)) (try! (transfer-helper token-id se`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `core/ststx-withdraw-nft-v2.clar:162` — TX_SENDER_AUTH_CHECK
- **Snippet:** `tstx-withdraw id) false)) ) (and (is-eq tx-sender owner) (is-eq contract-caller owner)) ) ) (define-public (list-in-ustx (id uint) (price uint) (commission-contract <commission-trait>)) (le`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `core/ststx-withdraw-nft.clar:87` — TX_SENDER_AUTH_CHECK
- **Snippet:** `ent principal)) (begin (asserts! (is-eq tx-sender sender) (err ERR_NOT_AUTHORIZED)) (asserts! (is-none (map-get? market token-id)) (err ERR_IS_LISTED)) (try! (transfer-helper token-id se`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `core/ststx-withdraw-nft.clar:167` — TX_SENDER_AUTH_CHECK
- **Snippet:** `tstx-withdraw id) false)) ) (and (is-eq tx-sender owner) (is-eq contract-caller owner)) ) ) (define-public (list-in-ustx (id uint) (price uint) (commission-contract <commission-trait>)) (le`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `core/ststxbtc-token-v2.clar:48` — TX_SENDER_AUTH_CHECK
- **Snippet:** `al (buff 34)))) (begin (asserts! (is-eq tx-sender sender) (err ERR_NOT_AUTHORIZED)) (try! (ft-transfer? ststxbtc amount sender recipient)) (try! (contract-call? .ststxbtc-tracking-v2 re`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `core/ststxbtc-token.clar:44` — TX_SENDER_AUTH_CHECK
- **Snippet:** `al (buff 34)))) (begin (asserts! (is-eq tx-sender sender) (err ERR_NOT_AUTHORIZED)) (try! (ft-transfer? ststxbtc amount sender recipient)) (try! (contract-call? .ststxbtc-tracking refre`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `core/ststxbtc-tracking-v2.clar:148` — LIST_PARAM_AGGREGATION_NO_DEDUP_CHECK
- **Snippet:** `(+ rewards rewards-saved)) ) ) ) (define-public (claim-pending-rewards-many (holders (list 200 (tuple (holder principal) (position principal))))) (ok (map claim-pending-rewards-iter holders))`
- **Why flagged:** REAL-WORLD PRECEDENT: the Zest Protocol hack (April 2024, ~322,000 STX / ~$1M lost) happened because a Borrow function accepted a list of up to 100 collateral assets and did not check for duplicates -- an attacker listed the same asset many times to inflate their collateral value. Check: does this function sum/aggregate a value (balance, collateral, voting power, etc.) per list entry? If so, verify duplicates in the list are rejected or naturally cannot inflate the total.

### `core/ststxbtc-tracking.clar:125` — LIST_PARAM_AGGREGATION_NO_DEDUP_CHECK
- **Snippet:** `(ok u0) (ok rewards) ) ) ) (define-public (claim-pending-rewards-many (holders (list 200 (tuple (holder principal) (position principal))))) (ok (map claim-pending-rewards-iter holders))`
- **Why flagged:** REAL-WORLD PRECEDENT: the Zest Protocol hack (April 2024, ~322,000 STX / ~$1M lost) happened because a Borrow function accepted a list of up to 100 collateral assets and did not check for duplicates -- an attacker listed the same asset many times to inflate their collateral value. Check: does this function sum/aggregate a value (balance, collateral, voting power, etc.) per list entry? If so, verify duplicates in the list are rejected or naturally cannot inflate the total.

### `core/ststxbtc-withdraw-nft.clar:86` — TX_SENDER_AUTH_CHECK
- **Snippet:** `ent principal)) (begin (asserts! (is-eq tx-sender sender) (err ERR_NOT_AUTHORIZED)) (asserts! (is-none (map-get? market token-id)) (err ERR_IS_LISTED)) (try! (transfer-helper token-id se`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `core/ststxbtc-withdraw-nft.clar:161` — TX_SENDER_AUTH_CHECK
- **Snippet:** `xbtc-withdraw id) false)) ) (and (is-eq tx-sender owner) (is-eq contract-caller owner)) ) ) (define-public (list-in-ustx (id uint) (price uint) (commission-contract <commission-trait>)) (le`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `genesis-nft/stacking-dao-cc-nft-minter.clar:25` — TX_SENDER_AUTH_CHECK
- **Snippet:** `yer principal)) (begin (asserts! (is-eq tx-sender (var-get deployer)) (err ERR_NOT_AUTHORIZED)) (var-set deployer new-deployer) (ok true) ) ) ;;-------------------------------------`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `genesis-nft/stacking-dao-cc-nft-minter.clar:41` — TX_SENDER_AUTH_CHECK
- **Snippet:** `ype (get type info)) ) (asserts! (is-eq tx-sender (var-get deployer)) (err ERR_NOT_AUTHORIZED)) (try! (contract-call? .stacking-dao-cc-nft mint-for-protocol recipient type)) (ok true)`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `genesis-nft/stacking-dao-cc-nft-minter.clar:47` — LIST_PARAM_AGGREGATION_NO_DEDUP_CHECK
- **Snippet:** `l recipient type)) (ok true) ) ) (define-public (airdrop-many (recipients (list 25 (tuple (recipient principal) (type uint))))) (begin (asserts! (is-eq tx-sender (var-get deployer)) (err`
- **Why flagged:** REAL-WORLD PRECEDENT: the Zest Protocol hack (April 2024, ~322,000 STX / ~$1M lost) happened because a Borrow function accepted a list of up to 100 collateral assets and did not check for duplicates -- an attacker listed the same asset many times to inflate their collateral value. Check: does this function sum/aggregate a value (balance, collateral, voting power, etc.) per list entry? If so, verify duplicates in the list are rejected or naturally cannot inflate the total.

### `genesis-nft/stacking-dao-cc-nft-minter.clar:49` — TX_SENDER_AUTH_CHECK
- **Snippet:** `(type uint))))) (begin (asserts! (is-eq tx-sender (var-get deployer)) (err ERR_NOT_AUTHORIZED)) (ok (map airdrop recipients)) ) )`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `genesis-nft/stacking-dao-cc-nft.clar:94` — TX_SENDER_AUTH_CHECK
- **Snippet:** `ent principal)) (begin (asserts! (is-eq tx-sender sender) (err ERR_NOT_AUTHORIZED)) (asserts! (is-none (map-get? market token-id)) (err ERR_IS_LISTED)) (try! (transfer-helper token-id se`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `genesis-nft/stacking-dao-cc-nft.clar:166` — TX_SENDER_AUTH_CHECK
- **Snippet:** `acking-dao-nyc id) false)) ) (or (is-eq tx-sender owner) (is-eq contract-caller owner)) ) ) (define-public (list-in-ustx (id uint) (price uint) (commission-contract <commission-trait>)) (le`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `genesis-nft/stacking-dao-genesis-nft-minter-v2.clar:57` — TX_SENDER_AUTH_CHECK
- **Snippet:** `nd-block uint)) (begin (asserts! (is-eq tx-sender DEPLOYER) (err ERR_NOT_AUTHORIZED)) (ok (var-set cycle-end-block end-block)) ) ) ;;------------------------------------- ;; Claim ;;----`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `genesis-nft/stacking-dao-genesis-nft-minter-v2.clar:83` — TX_SENDER_AUTH_CHECK
- **Snippet:** `ype (get type info)) ) (asserts! (is-eq tx-sender DEPLOYER) (err ERR_NOT_AUTHORIZED)) (asserts! (can-claim recipient) (err ERR_CANNOT_CLAIM)) (asserts! (not (has-claimed recipient)) (err`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `genesis-nft/stacking-dao-genesis-nft-minter-v2.clar:93` — LIST_PARAM_AGGREGATION_NO_DEDUP_CHECK
- **Snippet:** `ms recipient true) (ok true) ) ) (define-public (airdrop-many (recipients (list 25 (tuple (recipient principal) (type uint))))) (begin (asserts! (is-eq tx-sender DEPLOYER) (err ERR_NOT_AU`
- **Why flagged:** REAL-WORLD PRECEDENT: the Zest Protocol hack (April 2024, ~322,000 STX / ~$1M lost) happened because a Borrow function accepted a list of up to 100 collateral assets and did not check for duplicates -- an attacker listed the same asset many times to inflate their collateral value. Check: does this function sum/aggregate a value (balance, collateral, voting power, etc.) per list entry? If so, verify duplicates in the list are rejected or naturally cannot inflate the total.

### `genesis-nft/stacking-dao-genesis-nft-minter-v2.clar:95` — TX_SENDER_AUTH_CHECK
- **Snippet:** `(type uint))))) (begin (asserts! (is-eq tx-sender DEPLOYER) (err ERR_NOT_AUTHORIZED)) (ok (map airdrop recipients)) ) ) (map-set claims 'SP2N3KC4CR7CC0JP592S9RBA9GHVVD30WRA5GXE8G true) (m`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `genesis-nft/stacking-dao-genesis-nft-minter.clar:57` — TX_SENDER_AUTH_CHECK
- **Snippet:** `nd-block uint)) (begin (asserts! (is-eq tx-sender DEPLOYER) (err ERR_NOT_AUTHORIZED)) (ok (var-set cycle-end-block end-block)) ) ) ;;------------------------------------- ;; Claim ;;----`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `genesis-nft/stacking-dao-genesis-nft-minter.clar:83` — TX_SENDER_AUTH_CHECK
- **Snippet:** `ype (get type info)) ) (asserts! (is-eq tx-sender DEPLOYER) (err ERR_NOT_AUTHORIZED)) (asserts! (can-claim recipient) (err ERR_CANNOT_CLAIM)) (asserts! (not (has-claimed recipient)) (err`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `genesis-nft/stacking-dao-genesis-nft-minter.clar:93` — LIST_PARAM_AGGREGATION_NO_DEDUP_CHECK
- **Snippet:** `ms recipient true) (ok true) ) ) (define-public (airdrop-many (recipients (list 25 (tuple (recipient principal) (type uint))))) (begin (asserts! (is-eq tx-sender DEPLOYER) (err ERR_NOT_AU`
- **Why flagged:** REAL-WORLD PRECEDENT: the Zest Protocol hack (April 2024, ~322,000 STX / ~$1M lost) happened because a Borrow function accepted a list of up to 100 collateral assets and did not check for duplicates -- an attacker listed the same asset many times to inflate their collateral value. Check: does this function sum/aggregate a value (balance, collateral, voting power, etc.) per list entry? If so, verify duplicates in the list are rejected or naturally cannot inflate the total.

### `genesis-nft/stacking-dao-genesis-nft-minter.clar:95` — TX_SENDER_AUTH_CHECK
- **Snippet:** `(type uint))))) (begin (asserts! (is-eq tx-sender DEPLOYER) (err ERR_NOT_AUTHORIZED)) (ok (map airdrop recipients)) ) ) (map-set claims 'SP2N3KC4CR7CC0JP592S9RBA9GHVVD30WRA5GXE8G true) (m`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `genesis-nft/stacking-dao-genesis-nft.clar:96` — TX_SENDER_AUTH_CHECK
- **Snippet:** `ent principal)) (begin (asserts! (is-eq tx-sender sender) (err ERR_NOT_AUTHORIZED)) (asserts! (is-none (map-get? market token-id)) (err ERR_IS_LISTED)) (try! (transfer-helper token-id se`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `genesis-nft/stacking-dao-genesis-nft.clar:168` — TX_SENDER_AUTH_CHECK
- **Snippet:** `ng-dao-genesis id) false)) ) (or (is-eq tx-sender owner) (is-eq contract-caller owner)) ) ) (define-public (list-in-ustx (id uint) (price uint) (commission-contract <commission-trait>)) (le`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `nakamoto/stacking-dao-fomo-eoy-nft.clar:84` — TX_SENDER_AUTH_CHECK
- **Snippet:** `ent principal)) (begin (asserts! (is-eq tx-sender sender) (err ERR_NOT_AUTHORIZED)) (asserts! (is-none (map-get? market token-id)) (err ERR_IS_LISTED)) (try! (transfer-helper token-id se`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `nakamoto/stacking-dao-fomo-eoy-nft.clar:156` — TX_SENDER_AUTH_CHECK
- **Snippet:** `-dao-fomo-eoy id) false)) ) (and (is-eq tx-sender owner) (is-eq contract-caller owner)) ) ) (define-public (list-in-ustx (id uint) (price uint) (commission-contract <commission-trait>)) (le`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `nakamoto/stacking-dao-fomo-nft.clar:84` — TX_SENDER_AUTH_CHECK
- **Snippet:** `ent principal)) (begin (asserts! (is-eq tx-sender sender) (err ERR_NOT_AUTHORIZED)) (asserts! (is-none (map-get? market token-id)) (err ERR_IS_LISTED)) (try! (transfer-helper token-id se`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `nakamoto/stacking-dao-fomo-nft.clar:156` — TX_SENDER_AUTH_CHECK
- **Snippet:** `king-dao-fomo id) false)) ) (and (is-eq tx-sender owner) (is-eq contract-caller owner)) ) ) (define-public (list-in-ustx (id uint) (price uint) (commission-contract <commission-trait>)) (le`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `tests/pox-3-mock.clar:341` — TX_SENDER_AUTH_CHECK
- **Snippet:** `ad-only (check-caller-allowed) (or (is-eq tx-sender contract-caller) (let ((caller-allowed ;; if not in the caller map, return false (unwrap! (map-get? al`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `tests/pox-3-mock.clar:647` — TX_SENDER_AUTH_CHECK
- **Snippet:** `ler principal)) (begin (asserts! (is-eq tx-sender contract-caller) (err ERR_STACKING_PERMISSION_DENIED)) (ok (map-delete allowance-contract-callers { sender: tx-sender, contrac`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `tests/pox-3-mock.clar:657` — TX_SENDER_AUTH_CHECK
- **Snippet:** `ptional uint))) (begin (asserts! (is-eq tx-sender contract-caller) (err ERR_STACKING_PERMISSION_DENIED)) (ok (map-set allowance-contract-callers { sender: tx-sen`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `tests/pox-4-mock.clar:350` — TX_SENDER_AUTH_CHECK
- **Snippet:** `ad-only (check-caller-allowed) (or (is-eq tx-sender contract-caller) (let ((caller-allowed ;; if not in the caller map, return false (unwrap! (map-get? al`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `tests/pox-4-mock.clar:593` — TX_SENDER_AUTH_CHECK
- **Snippet:** `ler principal)) (begin (asserts! (is-eq tx-sender contract-caller) (err ERR_STACKING_PERMISSION_DENIED)) (ok (map-delete allowance-contract-callers { sender: tx-sender, contrac`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `tests/pox-4-mock.clar:603` — TX_SENDER_AUTH_CHECK
- **Snippet:** `ptional uint))) (begin (asserts! (is-eq tx-sender contract-caller) (err ERR_STACKING_PERMISSION_DENIED)) (ok (map-set allowance-contract-callers { sender: tx-sen`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `tests/pox-fast-pool-v2-mock.clar:342` — LIST_PARAM_AGGREGATION_NO_DEDUP_CHECK
- **Snippet:** `after the current cycle is half through (define-public (delegate-stack-stx-many (users (list 30 principal))) (let ( (current-cycle (contract-call? .pox-4-mock current-pox-reward-cycle)) (sta`
- **Why flagged:** REAL-WORLD PRECEDENT: the Zest Protocol hack (April 2024, ~322,000 STX / ~$1M lost) happened because a Borrow function accepted a list of up to 100 collateral assets and did not check for duplicates -- an attacker listed the same asset many times to inflate their collateral value. Check: does this function sum/aggregate a value (balance, collateral, voting power, etc.) per list entry? If so, verify duplicates in the list are rejected or naturally cannot inflate the total.

### `tests/pox-fast-pool-v2-mock.clar:449` — TX_SENDER_AUTH_CHECK
- **Snippet:** `ptional uint))) (begin (asserts! (is-eq tx-sender contract-caller) err-stacking-permission-denied) (ok (map-set allowance-contract-callers { sender: tx-sender, contract-caller: cal`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `tests/pox-fast-pool-v2-mock.clar:457` — TX_SENDER_AUTH_CHECK
- **Snippet:** `ler principal)) (begin (asserts! (is-eq tx-sender contract-caller) err-stacking-permission-denied) (ok (map-delete allowance-contract-callers { sender: tx-sender, contract-caller: caller})))`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `tests/pox-fast-pool-v2-mock.clar:462` — TX_SENDER_AUTH_CHECK
- **Snippet:** `read-only (check-caller-allowed) (or (is-eq tx-sender contract-caller) (let ((caller-allowed ;; if not in the caller map, return false (unwrap! (map-get? allowance-c`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `tests/sbtc-registry.clar:258` — LIST_PARAM_AGGREGATION_NO_DEDUP_CHECK
- **Snippet:** `s contract. ;; #[allow(unchecked_data)] (define-public (rotate-keys (new-keys (list 128 (buff 33))) (new-address principal) (new-aggregate-pubkey (buff 33)) (new-signature-threshold u`
- **Why flagged:** REAL-WORLD PRECEDENT: the Zest Protocol hack (April 2024, ~322,000 STX / ~$1M lost) happened because a Borrow function accepted a list of up to 100 collateral assets and did not check for duplicates -- an attacker listed the same asset many times to inflate their collateral value. Check: does this function sum/aggregate a value (balance, collateral, voting power, etc.) per list entry? If so, verify duplicates in the list are rejected or naturally cannot inflate the total.

### `tests/sbtc-token.clar:94` — LIST_PARAM_AGGREGATION_NO_DEDUP_CHECK
- **Snippet:** `t item)) ) ;; #[allow(unchecked_data)] (define-public (protocol-mint-many (recipients (list 200 {amount: uint, recipient: principal}))) (begin (try! (contract-call? .sbtc-registry validate-protoco`
- **Why flagged:** REAL-WORLD PRECEDENT: the Zest Protocol hack (April 2024, ~322,000 STX / ~$1M lost) happened because a Borrow function accepted a list of up to 100 collateral assets and did not check for duplicates -- an attacker listed the same asset many times to inflate their collateral value. Check: does this function sum/aggregate a value (balance, collateral, voting power, etc.) per list entry? If so, verify duplicates in the list are rejected or naturally cannot inflate the total.

### `tests/sbtc-token.clar:108` — TX_SENDER_AUTH_CHECK
- **Snippet:** `l (buff 34)))) (begin (asserts! (or (is-eq tx-sender sender) (is-eq contract-caller sender)) ERR_NOT_OWNER) (ft-transfer? sbtc-token amount sender recipient) ) ) (define-read-only (get-name) (`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `tests/swap-lp-token.clar:54` — TX_SENDER_AUTH_CHECK
- **Snippet:** `al (buff 34)))) (begin (asserts! (is-eq tx-sender sender) ERR-NOT-AUTHORIZED) (match (ft-transfer? swap-lp-token amount sender recipient) response (begin (print memo)`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `tests/swap-lp-token.clar:78` — TX_SENDER_AUTH_CHECK
- **Snippet:** `(amount uint)) (begin (asserts! (is-eq tx-sender burner) ERR-NOT-AUTHORIZED) (ft-burn? swap-lp-token amount burner) ) ) ;; Change the minter to any other principal, can only be called th`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `tests/swap-lp-token.clar:86` — TX_SENDER_AUTH_CHECK
- **Snippet:** `who principal)) (begin (asserts! (is-eq tx-sender CONTRACT-OWNER) ERR-NOT-AUTHORIZED) (ok (var-set approved-minter who)) ) ) (define-public (set-token-uri (new-uri (string-utf8 256))) (`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `tests/swap-lp-token.clar:93` — TX_SENDER_AUTH_CHECK
- **Snippet:** `ing-utf8 256))) (begin (asserts! (is-eq tx-sender CONTRACT-OWNER) ERR-NOT-AUTHORIZED) (ok (var-set token-uri new-uri)) ) )`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `tests/wstx-token.clar:55` — TX_SENDER_AUTH_CHECK
- **Snippet:** `-address recipient)) ) (asserts! (is-eq tx-sender sender) (err ERR_NOT_AUTHORIZED)) (if (and (not sender-is-protocol) recipient-is-protocol) ;; User to Protocol (begin (`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `version-2/native-stacking-pool-v1.clar:230` — LIST_PARAM_AGGREGATION_NO_DEDUP_CHECK
- **Snippet:** `re bitcoin height of the current cycle. (define-public (delegate-stack-stx (users (list 30 {user: principal, amount-ustx: uint})) (pox-address { version: (buff 1), hashbytes: (buff 32`
- **Why flagged:** REAL-WORLD PRECEDENT: the Zest Protocol hack (April 2024, ~322,000 STX / ~$1M lost) happened because a Borrow function accepted a list of up to 100 collateral assets and did not check for duplicates -- an attacker listed the same asset many times to inflate their collateral value. Check: does this function sum/aggregate a value (balance, collateral, voting power, etc.) per list entry? If so, verify duplicates in the list are rejected or naturally cannot inflate the total.

### `version-2/native-stacking-pool-v1.clar:243` — LIST_PARAM_AGGREGATION_NO_DEDUP_CHECK
- **Snippet:** `re bitcoin height of the current cycle. (define-public (delegate-stack-stx-simple (users (list 30 principal)) (pox-address { version: (buff 1), hashbytes: (buff 32)})`
- **Why flagged:** REAL-WORLD PRECEDENT: the Zest Protocol hack (April 2024, ~322,000 STX / ~$1M lost) happened because a Borrow function accepted a list of up to 100 collateral assets and did not check for duplicates -- an attacker listed the same asset many times to inflate their collateral value. Check: does this function sum/aggregate a value (balance, collateral, voting power, etc.) per list entry? If so, verify duplicates in the list are rejected or naturally cannot inflate the total.

### `version-2/native-stacking-pool-v1.clar:327` — LIST_PARAM_AGGREGATION_NO_DEDUP_CHECK
- **Snippet:** `k (set-metadata-internal key value)))) (define-public (set-metadata-many (keys (list 30 (string-ascii 8))) (values (list 30 (string-ascii 80)))) (begin (asserts! (check-caller-allowed) err-stac`
- **Why flagged:** REAL-WORLD PRECEDENT: the Zest Protocol hack (April 2024, ~322,000 STX / ~$1M lost) happened because a Borrow function accepted a list of up to 100 collateral assets and did not check for duplicates -- an attacker listed the same asset many times to inflate their collateral value. Check: does this function sum/aggregate a value (balance, collateral, voting power, etc.) per list entry? If so, verify duplicates in the list are rejected or naturally cannot inflate the total.

### `version-2/native-stacking-pool-v1.clar:357` — TX_SENDER_AUTH_CHECK
- **Snippet:** `ptional uint))) (begin (asserts! (is-eq tx-sender contract-caller) err-stacking-permission-denied) (ok (map-set allowance-contract-callers { sender: tx-sender, contract-caller: cal`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `version-2/native-stacking-pool-v1.clar:365` — TX_SENDER_AUTH_CHECK
- **Snippet:** `ler principal)) (begin (asserts! (is-eq tx-sender contract-caller) err-stacking-permission-denied) (ok (map-delete allowance-contract-callers { sender: tx-sender, contract-caller: caller})))`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `version-2/native-stacking-pool-v1.clar:370` — TX_SENDER_AUTH_CHECK
- **Snippet:** `read-only (check-caller-allowed) (or (is-eq tx-sender contract-caller) (let ((caller-allowed ;; if not in the caller map, return false (unwrap! (map-get? allowance-c`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `version-2/stacking-pool-payout-v1.clar:119` — LIST_PARAM_AGGREGATION_NO_DEDUP_CHECK
- **Snippet:** `-sender (as-contract tx-sender)) ) ) (define-public (distribute-rewards (users (list 200 principal)) (reward-id uint)) (let ( (reward-id-list (list reward-id reward-id reward-id reward-id rew`
- **Why flagged:** REAL-WORLD PRECEDENT: the Zest Protocol hack (April 2024, ~322,000 STX / ~$1M lost) happened because a Borrow function accepted a list of up to 100 collateral assets and did not check for duplicates -- an attacker listed the same asset many times to inflate their collateral value. Check: does this function sum/aggregate a value (balance, collateral, voting power, etc.) per list entry? If so, verify duplicates in the list are rejected or naturally cannot inflate the total.

### `version-2/stacking-pool-v1.clar:151` — LIST_PARAM_AGGREGATION_NO_DEDUP_CHECK
- **Snippet:** `block-height } }) (ok true) ) ) (define-public (prepare-delegate-many (delegates (list 50 principal))) (let ( ;; 1. Delegate (delegation-errors (filter is-error (map delegation deleg`
- **Why flagged:** REAL-WORLD PRECEDENT: the Zest Protocol hack (April 2024, ~322,000 STX / ~$1M lost) happened because a Borrow function accepted a list of up to 100 collateral assets and did not check for duplicates -- an attacker listed the same asset many times to inflate their collateral value. Check: does this function sum/aggregate a value (balance, collateral, voting power, etc.) per list entry? If so, verify duplicates in the list are rejected or naturally cannot inflate the total.

### `version-2/strategy-v3.clar:222` — LIST_PARAM_AGGREGATION_NO_DEDUP_CHECK
- **Snippet:** `;------------------------------------- (define-public (return-unlocked-stx (delegates (list 30 <stacking-delegate-trait>)) (reserve <reserve-trait>)) (ok (map return-unlocked-stx-helper delegates (`
- **Why flagged:** REAL-WORLD PRECEDENT: the Zest Protocol hack (April 2024, ~322,000 STX / ~$1M lost) happened because a Borrow function accepted a list of up to 100 collateral assets and did not check for duplicates -- an attacker listed the same asset many times to inflate their collateral value. Check: does this function sum/aggregate a value (balance, collateral, voting power, etc.) per list entry? If so, verify duplicates in the list are rejected or naturally cannot inflate the total.

### `version-3/ststxbtc-migration-v1.clar:16` — LIST_PARAM_AGGREGATION_NO_DEDUP_CHECK
- **Snippet:** `;------------------------------------- (define-public (migrate-ststxbtc (addresses (list 200 principal))) (begin (try! (contract-call? .dao check-is-protocol contract-caller)) (ok (map mig`
- **Why flagged:** REAL-WORLD PRECEDENT: the Zest Protocol hack (April 2024, ~322,000 STX / ~$1M lost) happened because a Borrow function accepted a list of up to 100 collateral assets and did not check for duplicates -- an attacker listed the same asset many times to inflate their collateral value. Check: does this function sum/aggregate a value (balance, collateral, voting power, etc.) per list entry? If so, verify duplicates in the list are rejected or naturally cannot inflate the total.

### `version-x/sdao-token.clar:44` — TX_SENDER_AUTH_CHECK
- **Snippet:** `al (buff 34)))) (begin (asserts! (is-eq tx-sender sender) (err ERR_NOT_AUTHORIZED)) (match (ft-transfer? sdao amount sender recipient) response (begin (print memo) (ok`
- **Why flagged:** REAL-WORLD PRECEDENT: the Charisma protocol hack (Sept 2024, ~183,548 STX lost) happened because a function authorized based on tx-sender, and an attacker routed the call through an intermediate contract's as-contract block to make tx-sender equal a trusted principal (confused-deputy pattern). Check: (1) is this comparing tx-sender against a hardcoded/trusted principal? (2) can this function be reached through another contract that wraps the call in as-contract? If yes to both, this may be a real bypass -- verify with a Clarinet test where a proxy contract relays the call.

### `version-x/strategy-v3-wip.clar:86` — LIST_PARAM_AGGREGATION_NO_DEDUP_CHECK
- **Snippet:** `;------------------------------------- (define-public (perform-return-stx (delegate-traits (list 900 <stacking-delegate-trait>))) (begin ;; TODO: does this check work? anyone should be able to`
- **Why flagged:** REAL-WORLD PRECEDENT: the Zest Protocol hack (April 2024, ~322,000 STX / ~$1M lost) happened because a Borrow function accepted a list of up to 100 collateral assets and did not check for duplicates -- an attacker listed the same asset many times to inflate their collateral value. Check: does this function sum/aggregate a value (balance, collateral, voting power, etc.) per list entry? If so, verify duplicates in the list are rejected or naturally cannot inflate the total.


## LOW (258)

### `block-info-helper-v2.clar:15` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `(let ( (user-index (contract-call? 'SP2VCQJGH7PHP2DJK7Z0V48AGBHQAW3R3ZW1QF4N.pool-reserve-data get-user-index-read account .ststx-token)) ) (if (is-some user-index) ;; (contract-call?`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-helper-v2.clar:18` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `me user-index) ;; (contract-call? 'SP2VCQJGH7PHP2DJK7Z0V48AGBHQAW3R3ZW1QF4N.pool-read-supply get-supplied-balance-user-ststx account) u0 u0 ) ) )`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-nakamoto-ststx-ratio-v2.clar:18` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `rr ERR_BLOCK_INFO))) (ststx-supply (unwrap-panic (contract-call? .ststx-token get-total-supply))) ) (ok (if (is-eq ststx-supply u0) DENOMINATOR_6 (/ (* total-stx-amount`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `block-info-nakamoto-ststx-ratio-v2.clar:32` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `ERR_BLOCK_INFO))) (ststxbtc-supply (unwrap-panic (contract-call? .ststxbtc-token get-total-supply))) (stx-for-ststx (- total-stx-amount ststxbtc-supply)) (ststx-supply (unwrap-panic (contr`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `block-info-nakamoto-ststx-ratio-v2.clar:34` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `nt ststxbtc-supply)) (ststx-supply (unwrap-panic (contract-call? .ststx-token get-total-supply))) ) (ok (if (is-eq ststx-supply u0) DENOMINATOR_6 (/ (* stx-for-ststx DE`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `block-info-nakamoto-ststx-ratio-v2.clar:48` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `ERR_BLOCK_INFO))) (ststxbtc-supply (unwrap-panic (contract-call? .ststxbtc-token-v2 get-total-supply))) (stx-for-ststx (- total-stx-amount ststxbtc-supply)) (ststx-supply (unwrap-panic (co`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `block-info-nakamoto-ststx-ratio-v2.clar:50` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `nt ststxbtc-supply)) (ststx-supply (unwrap-panic (contract-call? .ststx-token get-total-supply))) ) (ok (if (is-eq ststx-supply u0) DENOMINATOR_6 (/ (* stx-for-ststx DE`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `block-info-nakamoto-ststx-ratio.clar:18` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `rr ERR_BLOCK_INFO))) (ststx-supply (unwrap-panic (contract-call? .ststx-token get-total-supply))) ) (ok (if (is-eq ststx-supply u0) DENOMINATOR_6 (/ (* total-stx-amount`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `block-info-nakamoto-ststx-ratio.clar:32` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `ERR_BLOCK_INFO))) (ststxbtc-supply (unwrap-panic (contract-call? .ststxbtc-token get-total-supply))) (stx-for-ststx (- total-stx-amount ststxbtc-supply)) (ststx-supply (unwrap-panic (contr`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `block-info-nakamoto-ststx-ratio.clar:34` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `nt ststxbtc-supply)) (ststx-supply (unwrap-panic (contract-call? .ststx-token get-total-supply))) ) (ok (if (is-eq ststx-supply u0) DENOMINATOR_6 (/ (* stx-for-ststx DE`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `block-info-nakamoto-v1.clar:57` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `(let ( ;; Wallet (balance (unwrap-panic (contract-call? 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-token-v-1-1 get-balance account))) ;; Staked (user-data (contract-c`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `block-info-nakamoto-v1.clar:57` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `(balance (unwrap-panic (contract-call? 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-token-v-1-1 get-balance account))) ;; Staked (user-data (contract-call? 'SPQC38PW542EQJ5M11CR25P`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-nakamoto-v1.clar:60` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `; Staked (user-data (contract-call? 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.earn-stx-ststx-v-1-1 get-user-data .ststx-token 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-tok`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-nakamoto-v1.clar:62` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `get-user-data .ststx-token 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-token-v-1-1 account )) ;; Staked (staked (if (is-some user-data) (get total-curr`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-nakamoto-v1.clar:80` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `(let ( ;; Wallet (balance (unwrap-panic (contract-call? 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-token-v-1-2 get-balance account))) ;; Staked (user-data (contract-c`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `block-info-nakamoto-v1.clar:80` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `(balance (unwrap-panic (contract-call? 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-token-v-1-2 get-balance account))) ;; Staked (user-data (contract-call? 'SPQC38PW542EQJ5M11CR25P`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-nakamoto-v1.clar:83` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `; Staked (user-data (contract-call? 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.earn-stx-ststx-v-1-2 get-user-data .ststx-token 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-tok`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-nakamoto-v1.clar:85` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `get-user-data .ststx-token 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-token-v-1-2 account )) (staked (if (is-some user-data) (get total-currently-staked (`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-nakamoto-v1.clar:120` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `(account principal)) (contract-call? 'SP2VCQJGH7PHP2DJK7Z0V48AGBHQAW3R3ZW1QF4N.zststx get-balance account) ) (define-read-only (get-user-zest-helper-2 (account principal)) (contract-call? 'SP2VC`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-nakamoto-v1.clar:124` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `(account principal)) (contract-call? 'SP2VCQJGH7PHP2DJK7Z0V48AGBHQAW3R3ZW1QF4N.zststx-v1-0 get-balance account) ) (define-read-only (get-user-zest-helper-3 (account principal)) (contract-call? '`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-nakamoto-v1.clar:128` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `(account principal)) (contract-call? 'SP2VCQJGH7PHP2DJK7Z0V48AGBHQAW3R3ZW1QF4N.zststx-v1-2 get-balance account) ) ;;------------------------------------- ;; Arkadiko ;;----------------------------`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-nakamoto-v1.clar:148` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `t principal)) (let ( (vault-info (unwrap-panic (contract-call? 'SP2C2YFP12AJZB4MABJBAJ55XECVS7E4PMMZ89YZR.arkadiko-vaults-data-v1-1 get-vault account .ststx-token))) ) (get collateral vaul`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `block-info-nakamoto-v1.clar:148` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `ault-info (unwrap-panic (contract-call? 'SP2C2YFP12AJZB4MABJBAJ55XECVS7E4PMMZ89YZR.arkadiko-vaults-data-v1-1 get-vault account .ststx-token))) ) (get collateral vault-info) ) ) ;;------------`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-nakamoto-v1.clar:171` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `k uint)) (let ( (total-lp-supply (unwrap-panic (contract-call? 'SP1Y5YSTAHZ88XYK1VPDH24GY0HPX5J4JECTMY4A1.ststx-aeusdc get-total-supply))) (user-wallet (unwrap-panic (contract-call? 'SP1Y5YS`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `block-info-nakamoto-v1.clar:171` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `lp-supply (unwrap-panic (contract-call? 'SP1Y5YSTAHZ88XYK1VPDH24GY0HPX5J4JECTMY4A1.ststx-aeusdc get-total-supply))) (user-wallet (unwrap-panic (contract-call? 'SP1Y5YSTAHZ88XYK1VPDH24GY0HPX5J4JECT`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-nakamoto-v1.clar:172` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `c get-total-supply))) (user-wallet (unwrap-panic (contract-call? 'SP1Y5YSTAHZ88XYK1VPDH24GY0HPX5J4JECTMY4A1.ststx-aeusdc get-balance account))) (user-staked (if (< block u143607) u0`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `block-info-nakamoto-v1.clar:172` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `er-wallet (unwrap-panic (contract-call? 'SP1Y5YSTAHZ88XYK1VPDH24GY0HPX5J4JECTMY4A1.ststx-aeusdc get-balance account))) (user-staked (if (< block u143607) u0 (get end (contract-call? 'S`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-nakamoto-v1.clar:175` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `u0 (get end (contract-call? 'SP1Y5YSTAHZ88XYK1VPDH24GY0HPX5J4JECTMY4A1.farming-ststx-aeusdc-core get-user-staked account)) )) (user-total (+ user-wallet user-staked)) (pool-in`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-nakamoto-v1.clar:179` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `taked)) (pool-info (contract-call? 'SP1Y5YSTAHZ88XYK1VPDH24GY0HPX5J4JECTMY4A1.univ2-core do-get-pool u8)) ) (/ (* user-total (get reserve0 pool-info)) total-lp-supply) ) ) ;;-----------`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-nakamoto-v1.clar:203` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `rincipal)) (let ( (token-balance (unwrap-panic (contract-call? 'SPZA22A4D15RKH5G8XDGQ7BPC20Q5JNMH0VQKSR6.token-ststx-earn-v1 get-balance account))) (ratio (contract-call? 'SPZA22A4D15RKH5G8X`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `block-info-nakamoto-v1.clar:203` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `n-balance (unwrap-panic (contract-call? 'SPZA22A4D15RKH5G8XDGQ7BPC20Q5JNMH0VQKSR6.token-ststx-earn-v1 get-balance account))) (ratio (contract-call? 'SPZA22A4D15RKH5G8XDGQ7BPC20Q5JNMH0VQKSR6.vault-`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-nakamoto-v1.clar:204` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `e account))) (ratio (contract-call? 'SPZA22A4D15RKH5G8XDGQ7BPC20Q5JNMH0VQKSR6.vault-ststx-earn-v1 get-underlying-per-token)) (wallet-amount (/ (* token-balance ratio) u1000000)) (queued-a`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-nakamoto-v1.clar:215` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `ims (get deposit-claims (contract-call? 'SPZA22A4D15RKH5G8XDGQ7BPC20Q5JNMH0VQKSR6.vault-ststx-earn-v1 get-claims-for-address account))) ) (fold + (map get-claim-iter deposit-claims) u0) ) ) (`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-nakamoto-v1.clar:223` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `t)) (let ( (claim (contract-call? 'SPZA22A4D15RKH5G8XDGQ7BPC20Q5JNMH0VQKSR6.vault-ststx-earn-v1 get-claim claim-id)) ) (get underlying-amount (unwrap-panic claim)) ) )`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-nakamoto-zest.clar:26` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `(account principal)) (contract-call? 'SP2VCQJGH7PHP2DJK7Z0V48AGBHQAW3R3ZW1QF4N.zststx get-balance account) ) (define-read-only (get-user-zest-helper-2 (account principal)) (contract-call? 'SP2VC`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-nakamoto-zest.clar:30` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `(account principal)) (contract-call? 'SP2VCQJGH7PHP2DJK7Z0V48AGBHQAW3R3ZW1QF4N.zststx-v1-0 get-balance account) ) (define-read-only (get-user-zest-helper-3 (account principal)) (contract-call? '`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-nakamoto-zest.clar:34` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `(account principal)) (contract-call? 'SP2VCQJGH7PHP2DJK7Z0V48AGBHQAW3R3ZW1QF4N.zststx-v1-2 get-balance account) ) (define-read-only (get-user-zest-helper-4 (account principal)) (ok (contract-cal`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-nakamoto-zest.clar:38` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `count principal)) (ok (contract-call? 'SP2VCQJGH7PHP2DJK7Z0V48AGBHQAW3R3ZW1QF4N.zststx-token get-balance account)) )`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-v10.clar:81` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `(let ( ;; Wallet (balance (unwrap-panic (contract-call? 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-token-v-1-1 get-balance account))) ;; Staked (user-data (contract-c`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `block-info-v10.clar:81` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `(balance (unwrap-panic (contract-call? 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-token-v-1-1 get-balance account))) ;; Staked (user-data (contract-call? 'SPQC38PW542EQJ5M11CR25P`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-v10.clar:84` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `; Staked (user-data (contract-call? 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.earn-stx-ststx-v-1-1 get-user-data .ststx-token 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-tok`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-v10.clar:86` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `get-user-data .ststx-token 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-token-v-1-1 account )) (staked (if (is-some user-data) (get total-currently-staked (`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-v10.clar:103` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `(let ( ;; Wallet (balance (unwrap-panic (contract-call? 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-token-v-1-2 get-balance account))) ;; Staked (user-data (contract-c`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `block-info-v10.clar:103` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `(balance (unwrap-panic (contract-call? 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-token-v-1-2 get-balance account))) ;; Staked (user-data (contract-call? 'SPQC38PW542EQJ5M11CR25P`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-v10.clar:106` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `; Staked (user-data (contract-call? 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.earn-stx-ststx-v-1-2 get-user-data .ststx-token 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-tok`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-v10.clar:108` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `get-user-data .ststx-token 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-token-v-1-2 account )) (staked (if (is-some user-data) (get total-currently-staked (`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-v11.clar:15` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `rincipal)) (let ( (token-balance (unwrap-panic (contract-call? 'SPZA22A4D15RKH5G8XDGQ7BPC20Q5JNMH0VQKSR6.token-ststx-earn-v1 get-balance account))) (ratio (contract-call? 'SPZA22A4D15RKH5G8X`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `block-info-v11.clar:15` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `n-balance (unwrap-panic (contract-call? 'SPZA22A4D15RKH5G8XDGQ7BPC20Q5JNMH0VQKSR6.token-ststx-earn-v1 get-balance account))) (ratio (contract-call? 'SPZA22A4D15RKH5G8XDGQ7BPC20Q5JNMH0VQKSR6.vault-`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-v11.clar:16` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `e account))) (ratio (contract-call? 'SPZA22A4D15RKH5G8XDGQ7BPC20Q5JNMH0VQKSR6.vault-ststx-earn-v1 get-underlying-per-token)) ) (/ (* token-balance ratio) u1000000) ) )`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-v17.clar:15` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `rincipal)) (let ( (token-balance (unwrap-panic (contract-call? 'SPZA22A4D15RKH5G8XDGQ7BPC20Q5JNMH0VQKSR6.token-ststx-earn-v1 get-balance account))) (ratio (contract-call? 'SPZA22A4D15RKH5G8X`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `block-info-v17.clar:15` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `n-balance (unwrap-panic (contract-call? 'SPZA22A4D15RKH5G8XDGQ7BPC20Q5JNMH0VQKSR6.token-ststx-earn-v1 get-balance account))) (ratio (contract-call? 'SPZA22A4D15RKH5G8XDGQ7BPC20Q5JNMH0VQKSR6.vault-`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-v17.clar:16` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `e account))) (ratio (contract-call? 'SPZA22A4D15RKH5G8XDGQ7BPC20Q5JNMH0VQKSR6.vault-ststx-earn-v1 get-underlying-per-token)) (wallet-amount (/ (* token-balance ratio) u1000000)) (queued-a`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-v17.clar:27` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `ims (get deposit-claims (contract-call? 'SPZA22A4D15RKH5G8XDGQ7BPC20Q5JNMH0VQKSR6.vault-ststx-earn-v1 get-claims-for-address account))) ) (fold + (map get-claim-iter deposit-claims) u0) ) ) (`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-v17.clar:35` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `t)) (let ( (claim (contract-call? 'SPZA22A4D15RKH5G8XDGQ7BPC20Q5JNMH0VQKSR6.vault-ststx-earn-v1 get-claim claim-id)) ) (get underlying-amount (unwrap-panic claim)) ) )`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-v5.clar:90` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `(let ( ;; Wallet (balance (unwrap-panic (contract-call? 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-token-v-1-1 get-balance account))) ;; Staked (user-data (contract-c`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `block-info-v5.clar:90` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `(balance (unwrap-panic (contract-call? 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-token-v-1-1 get-balance account))) ;; Staked (user-data (contract-call? 'SPQC38PW542EQJ5M11CR25P`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-v5.clar:93` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `; Staked (user-data (contract-call? 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.earn-stx-ststx-v-1-1 get-user-data .ststx-token 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-tok`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-v5.clar:95` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `get-user-data .ststx-token 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-token-v-1-1 account )) (staked (if (is-some user-data) (get total-currently-staked (`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-v5.clar:112` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `(let ( ;; Wallet (balance (unwrap-panic (contract-call? 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-token-v-1-2 get-balance account))) ;; Staked (user-data (contract-c`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `block-info-v5.clar:112` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `(balance (unwrap-panic (contract-call? 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-token-v-1-2 get-balance account))) ;; Staked (user-data (contract-call? 'SPQC38PW542EQJ5M11CR25P`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-v5.clar:115` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `; Staked (user-data (contract-call? 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.earn-stx-ststx-v-1-2 get-user-data .ststx-token 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-tok`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-v5.clar:117` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `get-user-data .ststx-token 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-token-v-1-2 account )) (staked (if (is-some user-data) (get total-currently-staked (`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-v5.clar:134` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `(let ( ;; Wallet (balance (unwrap-panic (contract-call? 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-token-v-1-2 get-balance account))) ;; Staked (user-data (contract-c`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `block-info-v5.clar:134` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `(balance (unwrap-panic (contract-call? 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-token-v-1-2 get-balance account))) ;; Staked (user-data (contract-call? 'SPQC38PW542EQJ5M11CR25P`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-v5.clar:137` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `; Staked (user-data (contract-call? 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.earn-stx-ststx-v-1-2 get-user-data .ststx-token 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-tok`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-v5.clar:139` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `get-user-data .ststx-token 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-token-v-1-2 account )) (staked (if (is-some user-data) (get total-currently-staked (u`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-v5.clar:151` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `; Total LP tokens (lp-total-supply (unwrap-panic (contract-call? 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-token-v-1-2 get-total-supply))) ;; Pool balance stSTX (lp-balance-s`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `block-info-v5.clar:151` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `al-supply (unwrap-panic (contract-call? 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-token-v-1-2 get-total-supply))) ;; Pool balance stSTX (lp-balance-ststx (unwrap-panic (contract-`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-v5.clar:154` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `ol balance stSTX (lp-balance-ststx (unwrap-panic (contract-call? .ststx-token get-balance 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stableswap-stx-ststx-v-1-2))) ;; User share (user-lp-sh`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `block-info-v5.clar:154` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `contract-call? .ststx-token get-balance 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stableswap-stx-ststx-v-1-2))) ;; User share (user-lp-share (/ (* user-total u1000000000000) lp-total-supply))`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-v6.clar:15` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `t principal)) (let ( (vault-info (unwrap-panic (contract-call? 'SP2C2YFP12AJZB4MABJBAJ55XECVS7E4PMMZ89YZR.arkadiko-vaults-data-v1-1 get-vault account .ststx-token))) ) (get collateral vaul`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `block-info-v6.clar:15` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `ault-info (unwrap-panic (contract-call? 'SP2C2YFP12AJZB4MABJBAJ55XECVS7E4PMMZ89YZR.arkadiko-vaults-data-v1-1 get-vault account .ststx-token))) ) (get collateral vault-info) ) )`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-v8.clar:15` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `ncipal)) (let ( (total-lp-supply (unwrap-panic (contract-call? 'SP1Y5YSTAHZ88XYK1VPDH24GY0HPX5J4JECTMY4A1.ststx-aeusdc get-total-supply))) (user-wallet (unwrap-panic (contract-call? 'SP1Y5YS`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `block-info-v8.clar:15` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `lp-supply (unwrap-panic (contract-call? 'SP1Y5YSTAHZ88XYK1VPDH24GY0HPX5J4JECTMY4A1.ststx-aeusdc get-total-supply))) (user-wallet (unwrap-panic (contract-call? 'SP1Y5YSTAHZ88XYK1VPDH24GY0HPX5J4JECT`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-v8.clar:16` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `c get-total-supply))) (user-wallet (unwrap-panic (contract-call? 'SP1Y5YSTAHZ88XYK1VPDH24GY0HPX5J4JECTMY4A1.ststx-aeusdc get-balance account))) (user-staked (get end (contract-call? 'SP1Y5YSTA`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `block-info-v8.clar:16` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `er-wallet (unwrap-panic (contract-call? 'SP1Y5YSTAHZ88XYK1VPDH24GY0HPX5J4JECTMY4A1.ststx-aeusdc get-balance account))) (user-staked (get end (contract-call? 'SP1Y5YSTAHZ88XYK1VPDH24GY0HPX5J4JECTMY`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-v8.clar:17` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `(user-staked (get end (contract-call? 'SP1Y5YSTAHZ88XYK1VPDH24GY0HPX5J4JECTMY4A1.farming-ststx-aeusdc-core get-user-staked account))) (user-total (+ user-wallet user-staked)) (pool-info (co`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-v8.clar:20` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `taked)) (pool-info (contract-call? 'SP1Y5YSTAHZ88XYK1VPDH24GY0HPX5J4JECTMY4A1.univ2-core do-get-pool u8)) ) (/ (* user-total (get reserve0 pool-info)) total-lp-supply) ) )`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-v9.clar:14` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `principal)) (let ( (user-wallet (unwrap-panic (contract-call? 'SP2VCQJGH7PHP2DJK7Z0V48AGBHQAW3R3ZW1QF4N.zststx-v1-0 get-balance account))) ) user-wallet ) )`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `block-info-v9.clar:14` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `er-wallet (unwrap-panic (contract-call? 'SP2VCQJGH7PHP2DJK7Z0V48AGBHQAW3R3ZW1QF4N.zststx-v1-0 get-balance account))) ) user-wallet ) )`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-velar-nakamoto-v1.clar:20` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `o uint)) (let ( (total-lp-supply (unwrap-panic (contract-call? 'SP20X3DC5R091J8B6YPQT638J8NR1W83KN6TN5BJY.curve-lp-token-v1_0_0_ststx-0001 get-total-supply))) (user-wallet (unwrap-panic (con`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `block-info-velar-nakamoto-v1.clar:20` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `lp-supply (unwrap-panic (contract-call? 'SP20X3DC5R091J8B6YPQT638J8NR1W83KN6TN5BJY.curve-lp-token-v1_0_0_ststx-0001 get-total-supply))) (user-wallet (unwrap-panic (contract-call? 'SP20X3DC5R091J8B`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-velar-nakamoto-v1.clar:21` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `1 get-total-supply))) (user-wallet (unwrap-panic (contract-call? 'SP20X3DC5R091J8B6YPQT638J8NR1W83KN6TN5BJY.curve-lp-token-v1_0_0_ststx-0001 get-balance account))) (user-staked (if (< block u2`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `block-info-velar-nakamoto-v1.clar:21` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `er-wallet (unwrap-panic (contract-call? 'SP20X3DC5R091J8B6YPQT638J8NR1W83KN6TN5BJY.curve-lp-token-v1_0_0_ststx-0001 get-balance account))) (user-staked (if (< block u243045) u0 (get en`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-velar-nakamoto-v1.clar:24` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `u0 (get end (contract-call? 'SP20X3DC5R091J8B6YPQT638J8NR1W83KN6TN5BJY.curve-farming-core-v1_1_1_ststx-0001 get-user-staked account)) )) (pool-info (contract-call? 'SP20X3DC5R091J8`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `block-info-velar-nakamoto-v1.clar:26` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `) )) (pool-info (contract-call? 'SP20X3DC5R091J8B6YPQT638J8NR1W83KN6TN5BJY.curve-pool-v1_0_0_ststx-0001 do-get-pool)) (reserve0 (get reserve0 pool-info)) (reserve0-ststx (/ (* reserve0`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `core/ststxbtc-token-v2.clar:77` — EFFECT_BEFORE_CHECK
- **Snippet:** `----------------------- ;; Mint method (define-public (mint-for-protocol (amount uint) (recipient principal)) (let ( (result (ft-mint? ststxbtc amount recipient)) ) (try! (contract-call?`
- **Why flagged:** In Clarity this is usually NOT exploitable on its own because transactions are atomic and a failed check rolls back the whole call (confirmed empirically in this project). Still worth fixing for gas efficiency / best practice, but do not report as Critical/High without a concrete exploit path.

### `core/ststxbtc-token-v2.clar:89` — EFFECT_BEFORE_CHECK
- **Snippet:** `ent))) result ) ) ;; Burn method (define-public (burn-for-protocol (amount uint) (sender principal)) (let ( (result (ft-burn? ststxbtc amount sender)) ) (try! (contract-call? .dao c`
- **Why flagged:** In Clarity this is usually NOT exploitable on its own because transactions are atomic and a failed check rolls back the whole call (confirmed empirically in this project). Still worth fixing for gas efficiency / best practice, but do not report as Critical/High without a concrete exploit path.

### `core/ststxbtc-token.clar:73` — EFFECT_BEFORE_CHECK
- **Snippet:** `----------------------- ;; Mint method (define-public (mint-for-protocol (amount uint) (recipient principal)) (let ( (result (ft-mint? ststxbtc amount recipient)) ) (try! (contract-call?`
- **Why flagged:** In Clarity this is usually NOT exploitable on its own because transactions are atomic and a failed check rolls back the whole call (confirmed empirically in this project). Still worth fixing for gas efficiency / best practice, but do not report as Critical/High without a concrete exploit path.

### `core/ststxbtc-token.clar:85` — EFFECT_BEFORE_CHECK
- **Snippet:** `ent))) result ) ) ;; Burn method (define-public (burn-for-protocol (amount uint) (sender principal)) (let ( (result (ft-burn? ststxbtc amount sender)) ) (try! (contract-call? .dao c`
- **Why flagged:** In Clarity this is usually NOT exploitable on its own because transactions are atomic and a failed check rolls back the whole call (confirmed empirically in this project). Still worth fixing for gas efficiency / best practice, but do not report as Critical/High without a concrete exploit path.

### `genesis-nft/stacking-dao-genesis-nft-minter-v2.clar:100` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `rop recipients)) ) ) (map-set claims 'SP2N3KC4CR7CC0JP592S9RBA9GHVVD30WRA5GXE8G true) (map-set claims 'SP1DJWJNKREHT3YGRB09DRCYD1QKGK5DKF8V868VX true) (map-set claims 'SPF7FJ9VFSVKNWH7JWSNFTTCG3P5Z`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter-v2.clar:101` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `9GHVVD30WRA5GXE8G true) (map-set claims 'SP1DJWJNKREHT3YGRB09DRCYD1QKGK5DKF8V868VX true) (map-set claims 'SPF7FJ9VFSVKNWH7JWSNFTTCG3P5Z0429R38KV7S true) (map-set claims 'SP3VTC5TNYC9ZJ5NZ9DG4HHZP5Z21Z`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter-v2.clar:102` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `D1QKGK5DKF8V868VX true) (map-set claims 'SPF7FJ9VFSVKNWH7JWSNFTTCG3P5Z0429R38KV7S true) (map-set claims 'SP3VTC5TNYC9ZJ5NZ9DG4HHZP5Z21ZM5JRSF6M5MD true) (map-set claims 'SP3J0Z8YSJD20TGEBE6M992CWFDG18`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter-v2.clar:103` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `CG3P5Z0429R38KV7S true) (map-set claims 'SP3VTC5TNYC9ZJ5NZ9DG4HHZP5Z21ZM5JRSF6M5MD true) (map-set claims 'SP3J0Z8YSJD20TGEBE6M992CWFDG18VB0PR599VY9 true) (map-set claims 'SP34455SJ4NJ7MCKV7CN64JJTVDP3`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter-v2.clar:104` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `P5Z21ZM5JRSF6M5MD true) (map-set claims 'SP3J0Z8YSJD20TGEBE6M992CWFDG18VB0PR599VY9 true) (map-set claims 'SP34455SJ4NJ7MCKV7CN64JJTVDP3VZPMVT54BH57 true) (map-set claims 'SP2EDRYCPGTS32HZAGWV54RAVA2GT`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter-v2.clar:105` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `WFDG18VB0PR599VY9 true) (map-set claims 'SP34455SJ4NJ7MCKV7CN64JJTVDP3VZPMVT54BH57 true) (map-set claims 'SP2EDRYCPGTS32HZAGWV54RAVA2GTW0WPBP4HGCXR true) (map-set claims 'SP3XD84X3PE79SHJAZCDW1V5E9EA8`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter-v2.clar:106` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `TVDP3VZPMVT54BH57 true) (map-set claims 'SP2EDRYCPGTS32HZAGWV54RAVA2GTW0WPBP4HGCXR true) (map-set claims 'SP3XD84X3PE79SHJAZCDW1V5E9EA8JSKRBPEKAEK7 true) (map-set claims 'SP1HHSDYJ0SGAM6K2W01ZF5K7AJFK`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter-v2.clar:107` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `VA2GTW0WPBP4HGCXR true) (map-set claims 'SP3XD84X3PE79SHJAZCDW1V5E9EA8JSKRBPEKAEK7 true) (map-set claims 'SP1HHSDYJ0SGAM6K2W01ZF5K7AJFKWMJNH365ZWS9 true) (map-set claims 'SPM5BVEBYCN2Z1AR2E06A69HF1W70`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter-v2.clar:108` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `E9EA8JSKRBPEKAEK7 true) (map-set claims 'SP1HHSDYJ0SGAM6K2W01ZF5K7AJFKWMJNH365ZWS9 true) (map-set claims 'SPM5BVEBYCN2Z1AR2E06A69HF1W70G7V5GZFDNPR true) (map-set claims 'SP331R3MQE82TBWV5R4WGZAD6FRDBN`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter-v2.clar:109` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `7AJFKWMJNH365ZWS9 true) (map-set claims 'SPM5BVEBYCN2Z1AR2E06A69HF1W70G7V5GZFDNPR true) (map-set claims 'SP331R3MQE82TBWV5R4WGZAD6FRDBN6S5ZN635CG2 true) (map-set claims 'SP3P1TCXN3FP3V79YWXC49F5X2HYKS`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter-v2.clar:110` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `HF1W70G7V5GZFDNPR true) (map-set claims 'SP331R3MQE82TBWV5R4WGZAD6FRDBN6S5ZN635CG2 true) (map-set claims 'SP3P1TCXN3FP3V79YWXC49F5X2HYKS39CMCP5FEHN true) (map-set claims 'SP1E8A3T3AW2HRFB5FXMYWB2DC0TS`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter-v2.clar:111` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `6FRDBN6S5ZN635CG2 true) (map-set claims 'SP3P1TCXN3FP3V79YWXC49F5X2HYKS39CMCP5FEHN true) (map-set claims 'SP1E8A3T3AW2HRFB5FXMYWB2DC0TSC6H1EGTHND1W true) (map-set claims 'SP25SF2MPZZS8Q20QA3VTYJXTHAHC`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter-v2.clar:112` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `X2HYKS39CMCP5FEHN true) (map-set claims 'SP1E8A3T3AW2HRFB5FXMYWB2DC0TSC6H1EGTHND1W true) (map-set claims 'SP25SF2MPZZS8Q20QA3VTYJXTHAHCRNM5MSZYDNB0 true) (map-set claims 'SP32ZYEZGWHHFQ5RX2WMFVDXR77C5`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter-v2.clar:113` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `DC0TSC6H1EGTHND1W true) (map-set claims 'SP25SF2MPZZS8Q20QA3VTYJXTHAHCRNM5MSZYDNB0 true) (map-set claims 'SP32ZYEZGWHHFQ5RX2WMFVDXR77C5WWQP4EK7E6HC true) (map-set claims 'SP2FA1H3K9FMY2CQ80WWT2JYMHZ5Z`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter-v2.clar:114` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `THAHCRNM5MSZYDNB0 true) (map-set claims 'SP32ZYEZGWHHFQ5RX2WMFVDXR77C5WWQP4EK7E6HC true) (map-set claims 'SP2FA1H3K9FMY2CQ80WWT2JYMHZ5Z2B810AT41APW true) (map-set claims 'SP2855G3MZ3WFS5P0NRK098T1DKQ3`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter-v2.clar:115` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `R77C5WWQP4EK7E6HC true) (map-set claims 'SP2FA1H3K9FMY2CQ80WWT2JYMHZ5Z2B810AT41APW true) (map-set claims 'SP2855G3MZ3WFS5P0NRK098T1DKQ3QH5MVJ14P70P true) (map-set claims 'SP3XMSJSV1TYRP69PAC0751P483QZ`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter-v2.clar:116` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `MHZ5Z2B810AT41APW true) (map-set claims 'SP2855G3MZ3WFS5P0NRK098T1DKQ3QH5MVJ14P70P true) (map-set claims 'SP3XMSJSV1TYRP69PAC0751P483QZ3E17R5GTV4CX true) (map-set claims 'SP2ZNGJ85ENDY6QRHQ5P2D4FXKGZW`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter-v2.clar:117` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `1DKQ3QH5MVJ14P70P true) (map-set claims 'SP3XMSJSV1TYRP69PAC0751P483QZ3E17R5GTV4CX true) (map-set claims 'SP2ZNGJ85ENDY6QRHQ5P2D4FXKGZWCKTB2T0Z55KS true) (map-set claims 'SP19WSDJWTH4CW3YG554XS5CAXJJG`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter-v2.clar:118` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `483QZ3E17R5GTV4CX true) (map-set claims 'SP2ZNGJ85ENDY6QRHQ5P2D4FXKGZWCKTB2T0Z55KS true) (map-set claims 'SP19WSDJWTH4CW3YG554XS5CAXJJGAN83P8CFZ4K1 true) (map-set claims 'SP1XY983C1MEXM83MGNJC2JAAEGYV`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter-v2.clar:119` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `XKGZWCKTB2T0Z55KS true) (map-set claims 'SP19WSDJWTH4CW3YG554XS5CAXJJGAN83P8CFZ4K1 true) (map-set claims 'SP1XY983C1MEXM83MGNJC2JAAEGYVYZY5BYW5KS4K true) (map-set claims 'SP2VG7S0R4Z8PYNYCAQ04HCBX1MH7`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter-v2.clar:120` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `AXJJGAN83P8CFZ4K1 true) (map-set claims 'SP1XY983C1MEXM83MGNJC2JAAEGYVYZY5BYW5KS4K true) (map-set claims 'SP2VG7S0R4Z8PYNYCAQ04HCBX1MH75VT11VXCWQ6G true) (map-set claims 'SP3XYP0HYZHKHJ96THQX8AV7TQYJW`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter-v2.clar:121` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `AEGYVYZY5BYW5KS4K true) (map-set claims 'SP2VG7S0R4Z8PYNYCAQ04HCBX1MH75VT11VXCWQ6G true) (map-set claims 'SP3XYP0HYZHKHJ96THQX8AV7TQYJWMF8PP30K0RX5 true) (map-set claims 'SP18P831TBGKSGMJEMJM0V29CMKJP`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter-v2.clar:122` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `X1MH75VT11VXCWQ6G true) (map-set claims 'SP3XYP0HYZHKHJ96THQX8AV7TQYJWMF8PP30K0RX5 true) (map-set claims 'SP18P831TBGKSGMJEMJM0V29CMKJP650ZT21YJ3XX true)`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter-v2.clar:123` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `TQYJWMF8PP30K0RX5 true) (map-set claims 'SP18P831TBGKSGMJEMJM0V29CMKJP650ZT21YJ3XX true)`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter.clar:100` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `rop recipients)) ) ) (map-set claims 'SP2N3KC4CR7CC0JP592S9RBA9GHVVD30WRA5GXE8G true) (map-set claims 'SP1DJWJNKREHT3YGRB09DRCYD1QKGK5DKF8V868VX true) (map-set claims 'SPF7FJ9VFSVKNWH7JWSNFTTCG3P5Z`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter.clar:101` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `9GHVVD30WRA5GXE8G true) (map-set claims 'SP1DJWJNKREHT3YGRB09DRCYD1QKGK5DKF8V868VX true) (map-set claims 'SPF7FJ9VFSVKNWH7JWSNFTTCG3P5Z0429R38KV7S true) (map-set claims 'SP3VTC5TNYC9ZJ5NZ9DG4HHZP5Z21Z`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter.clar:102` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `D1QKGK5DKF8V868VX true) (map-set claims 'SPF7FJ9VFSVKNWH7JWSNFTTCG3P5Z0429R38KV7S true) (map-set claims 'SP3VTC5TNYC9ZJ5NZ9DG4HHZP5Z21ZM5JRSF6M5MD true) (map-set claims 'SP3J0Z8YSJD20TGEBE6M992CWFDG18`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter.clar:103` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `CG3P5Z0429R38KV7S true) (map-set claims 'SP3VTC5TNYC9ZJ5NZ9DG4HHZP5Z21ZM5JRSF6M5MD true) (map-set claims 'SP3J0Z8YSJD20TGEBE6M992CWFDG18VB0PR599VY9 true) (map-set claims 'SP34455SJ4NJ7MCKV7CN64JJTVDP3`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter.clar:104` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `P5Z21ZM5JRSF6M5MD true) (map-set claims 'SP3J0Z8YSJD20TGEBE6M992CWFDG18VB0PR599VY9 true) (map-set claims 'SP34455SJ4NJ7MCKV7CN64JJTVDP3VZPMVT54BH57 true) (map-set claims 'SP2EDRYCPGTS32HZAGWV54RAVA2GT`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter.clar:105` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `WFDG18VB0PR599VY9 true) (map-set claims 'SP34455SJ4NJ7MCKV7CN64JJTVDP3VZPMVT54BH57 true) (map-set claims 'SP2EDRYCPGTS32HZAGWV54RAVA2GTW0WPBP4HGCXR true) (map-set claims 'SP3XD84X3PE79SHJAZCDW1V5E9EA8`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter.clar:106` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `TVDP3VZPMVT54BH57 true) (map-set claims 'SP2EDRYCPGTS32HZAGWV54RAVA2GTW0WPBP4HGCXR true) (map-set claims 'SP3XD84X3PE79SHJAZCDW1V5E9EA8JSKRBPEKAEK7 true) (map-set claims 'SP1HHSDYJ0SGAM6K2W01ZF5K7AJFK`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter.clar:107` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `VA2GTW0WPBP4HGCXR true) (map-set claims 'SP3XD84X3PE79SHJAZCDW1V5E9EA8JSKRBPEKAEK7 true) (map-set claims 'SP1HHSDYJ0SGAM6K2W01ZF5K7AJFKWMJNH365ZWS9 true) (map-set claims 'SPM5BVEBYCN2Z1AR2E06A69HF1W70`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter.clar:108` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `E9EA8JSKRBPEKAEK7 true) (map-set claims 'SP1HHSDYJ0SGAM6K2W01ZF5K7AJFKWMJNH365ZWS9 true) (map-set claims 'SPM5BVEBYCN2Z1AR2E06A69HF1W70G7V5GZFDNPR true) (map-set claims 'SP331R3MQE82TBWV5R4WGZAD6FRDBN`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter.clar:109` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `7AJFKWMJNH365ZWS9 true) (map-set claims 'SPM5BVEBYCN2Z1AR2E06A69HF1W70G7V5GZFDNPR true) (map-set claims 'SP331R3MQE82TBWV5R4WGZAD6FRDBN6S5ZN635CG2 true) (map-set claims 'SP3P1TCXN3FP3V79YWXC49F5X2HYKS`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter.clar:110` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `HF1W70G7V5GZFDNPR true) (map-set claims 'SP331R3MQE82TBWV5R4WGZAD6FRDBN6S5ZN635CG2 true) (map-set claims 'SP3P1TCXN3FP3V79YWXC49F5X2HYKS39CMCP5FEHN true) (map-set claims 'SP1E8A3T3AW2HRFB5FXMYWB2DC0TS`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter.clar:111` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `6FRDBN6S5ZN635CG2 true) (map-set claims 'SP3P1TCXN3FP3V79YWXC49F5X2HYKS39CMCP5FEHN true) (map-set claims 'SP1E8A3T3AW2HRFB5FXMYWB2DC0TSC6H1EGTHND1W true) (map-set claims 'SP25SF2MPZZS8Q20QA3VTYJXTHAHC`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter.clar:112` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `X2HYKS39CMCP5FEHN true) (map-set claims 'SP1E8A3T3AW2HRFB5FXMYWB2DC0TSC6H1EGTHND1W true) (map-set claims 'SP25SF2MPZZS8Q20QA3VTYJXTHAHCRNM5MSZYDNB0 true) (map-set claims 'SP32ZYEZGWHHFQ5RX2WMFVDXR77C5`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter.clar:113` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `DC0TSC6H1EGTHND1W true) (map-set claims 'SP25SF2MPZZS8Q20QA3VTYJXTHAHCRNM5MSZYDNB0 true) (map-set claims 'SP32ZYEZGWHHFQ5RX2WMFVDXR77C5WWQP4EK7E6HC true) (map-set claims 'SP2FA1H3K9FMY2CQ80WWT2JYMHZ5Z`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter.clar:114` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `THAHCRNM5MSZYDNB0 true) (map-set claims 'SP32ZYEZGWHHFQ5RX2WMFVDXR77C5WWQP4EK7E6HC true) (map-set claims 'SP2FA1H3K9FMY2CQ80WWT2JYMHZ5Z2B810AT41APW true) (map-set claims 'SP2855G3MZ3WFS5P0NRK098T1DKQ3`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter.clar:115` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `R77C5WWQP4EK7E6HC true) (map-set claims 'SP2FA1H3K9FMY2CQ80WWT2JYMHZ5Z2B810AT41APW true) (map-set claims 'SP2855G3MZ3WFS5P0NRK098T1DKQ3QH5MVJ14P70P true) (map-set claims 'SP3XMSJSV1TYRP69PAC0751P483QZ`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter.clar:116` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `MHZ5Z2B810AT41APW true) (map-set claims 'SP2855G3MZ3WFS5P0NRK098T1DKQ3QH5MVJ14P70P true) (map-set claims 'SP3XMSJSV1TYRP69PAC0751P483QZ3E17R5GTV4CX true) (map-set claims 'SP2ZNGJ85ENDY6QRHQ5P2D4FXKGZW`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter.clar:117` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `1DKQ3QH5MVJ14P70P true) (map-set claims 'SP3XMSJSV1TYRP69PAC0751P483QZ3E17R5GTV4CX true) (map-set claims 'SP2ZNGJ85ENDY6QRHQ5P2D4FXKGZWCKTB2T0Z55KS true) (map-set claims 'SP19WSDJWTH4CW3YG554XS5CAXJJG`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter.clar:118` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `483QZ3E17R5GTV4CX true) (map-set claims 'SP2ZNGJ85ENDY6QRHQ5P2D4FXKGZWCKTB2T0Z55KS true) (map-set claims 'SP19WSDJWTH4CW3YG554XS5CAXJJGAN83P8CFZ4K1 true) (map-set claims 'SP1XY983C1MEXM83MGNJC2JAAEGYV`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter.clar:119` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `XKGZWCKTB2T0Z55KS true) (map-set claims 'SP19WSDJWTH4CW3YG554XS5CAXJJGAN83P8CFZ4K1 true) (map-set claims 'SP1XY983C1MEXM83MGNJC2JAAEGYVYZY5BYW5KS4K true) (map-set claims 'SP2VG7S0R4Z8PYNYCAQ04HCBX1MH7`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter.clar:120` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `AXJJGAN83P8CFZ4K1 true) (map-set claims 'SP1XY983C1MEXM83MGNJC2JAAEGYVYZY5BYW5KS4K true) (map-set claims 'SP2VG7S0R4Z8PYNYCAQ04HCBX1MH75VT11VXCWQ6G true) (map-set claims 'SP3XYP0HYZHKHJ96THQX8AV7TQYJW`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter.clar:121` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `AEGYVYZY5BYW5KS4K true) (map-set claims 'SP2VG7S0R4Z8PYNYCAQ04HCBX1MH75VT11VXCWQ6G true) (map-set claims 'SP3XYP0HYZHKHJ96THQX8AV7TQYJWMF8PP30K0RX5 true) (map-set claims 'SP18P831TBGKSGMJEMJM0V29CMKJP`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter.clar:122` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `X1MH75VT11VXCWQ6G true) (map-set claims 'SP3XYP0HYZHKHJ96THQX8AV7TQYJWMF8PP30K0RX5 true) (map-set claims 'SP18P831TBGKSGMJEMJM0V29CMKJP650ZT21YJ3XX true)`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `genesis-nft/stacking-dao-genesis-nft-minter.clar:123` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `TQYJWMF8PP30K0RX5 true) (map-set claims 'SP18P831TBGKSGMJEMJM0V29CMKJP650ZT21YJ3XX true)`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `helpers/block-info-v1.clar:65` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `ce (at-block block-hash (contract-call? 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-token-v-1-1 get-balance account))) ;; Staked (user-data (at-block block-hash (contract-call? 'SP`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `helpers/block-info-v1.clar:68` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `ta (at-block block-hash (contract-call? 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.earn-stx-ststx-v-1-1 get-user-data .ststx-token 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-tok`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `helpers/block-info-v1.clar:70` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `get-user-data .ststx-token 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-token-v-1-1 account ))) ) (if (is-some user-data) ;; Has staked (ok (+ (unwra`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `helpers/cc-redemption-v1.clar:24` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `stx (unwrap-panic (try! (contract-call? 'SP8A9HZ3PKST0S42VM9523Z9NV42SZ026V4K39WH.ccd012-redemption-nyc redeem-nyc)))) ) (contract-call? .stacking-dao-core-v2 deposit reserve commission staking`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `helpers/token-metadata-update-notify.clar:6` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `ata ;; refreshed. (use-trait nft-trait 'SP2PABAF9FTAJYNFZH93XENAJ8FVY99RRM50D2JG9.nft-trait.nft-trait) (use-trait ft-trait 'SP3FBR2AGK5H9QBDH3EEN6DF8EK8JY7RX8QJ5SVTE.sip-010-trait-ft-standard.sip-010`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `helpers/token-metadata-update-notify.clar:7` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `ft-trait.nft-trait) (use-trait ft-trait 'SP3FBR2AGK5H9QBDH3EEN6DF8EK8JY7RX8QJ5SVTE.sip-010-trait-ft-standard.sip-010-trait) ;; Refresh the metadata for one or more NFTs from a specific contract. (def`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `keeper-jobs/return-stx-job-v1.clar:7` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `r contract to the reserve. (impl-trait 'SP3C0TCQS0C0YY8E0V3EJ7V4X9571885D44M8EFWF.arkadiko-automation-trait-v1.automation-trait) ;;------------------------------------- ;; Variables ;;--------------`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `keeper-jobs/rewards-job-v1.clar:7` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `be added to the protocol. (impl-trait 'SP3C0TCQS0C0YY8E0V3EJ7V4X9571885D44M8EFWF.arkadiko-automation-trait-v1.automation-trait) ;;------------------------------------- ;; Variables ;;--------------`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `keeper-jobs/tax-v1.clar:13` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `/keepers.arkadiko.finance/ (impl-trait 'SP3C0TCQS0C0YY8E0V3EJ7V4X9571885D44M8EFWF.arkadiko-automation-trait-v1.automation-trait) (use-trait ft-trait .sip-010-trait-ft-standard.sip-010-trait) ;;-----`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `keeper-jobs/tax-v1.clar:98` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `tx-sender))) (new-balance-sdao (unwrap-panic (contract-call? .sdao-token get-balance (as-contract tx-sender)))) ) (unwrap! (as-contract (contract-call? .swap add-liquidity`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `nakamoto/fomo-eoy.clar:193` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `cue-funds) (let ( (ststx-balance (unwrap-panic (contract-call? .ststx-token get-balance (as-contract tx-sender)))) (admin tx-sender) ) (try! (contract-call? .dao check-is-protocol tx-s`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `nakamoto/fomo.clar:193` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `cue-funds) (let ( (ststx-balance (unwrap-panic (contract-call? .ststx-token get-balance (as-contract tx-sender)))) (admin tx-sender) ) (try! (contract-call? .dao check-is-protocol tx-s`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `tests/pox-fast-pool-v2-mock.clar:63` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `cle-length (/ (get reward-cycle-length (unwrap-panic (contract-call? .pox-4-mock get-pox-info))) u2)) (define-constant err-unauthorized (err u401)) (define-constant err-forbidden (err u403)) (define-`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `tests/swap-lp-token.clar:5` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `dard.sip-010-trait) (use-trait lp-trait 'SPRP7MYBHSMFH5EGN3HGX6KNQ7QBHVTBPCE2RJDH.lp-trait.lp-trait) (define-fungible-token swap-lp-token) (define-constant CONTRACT-OWNER tx-sender) (define-consta`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `tests/swap.clar:14` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `dard.sip-010-trait) (use-trait lp-trait 'SPRP7MYBHSMFH5EGN3HGX6KNQ7QBHVTBPCE2RJDH.lp-trait.lp-trait) ;;;;;;;;;;;;;;; ;; Constants ;; ;;;;;;;;;;;;;;; ;; This contract address (define-constant this-co`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `tests/swap.clar:36` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `dress (define-constant protocol-address 'SP3GDP77BDSZ4VN2QQP057C9T6DRDDB6WGES6K9CP) ;; Convergence Threshold Constant (define-constant convergence-threshold u2) ;; Contract for Stableswap Staking an`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `tests/wstx-token.clar:124` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `protocol-addresses (list .swap 'SP3GDP77BDSZ4VN2QQP057C9T6DRDDB6WGES6K9CP )) (try! (ft-mint? wstx u100000000000 'ST1PQHQKV0RJXZFY1DGX8MNSNYVE3VGZJSRTPGZGM)) )`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `version-1/commission-v1.clar:43` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `epare-length (get prepare-cycle-length (unwrap-panic (contract-call? .pox-3-mock get-pox-info)))) ) (+ cycle-end-block pox-prepare-length) ) ) ;;------------------------------------- ;; Trait`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-1/stacker-1.clar:64` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `-info) ;; TODO: update for mainnet (unwrap-panic (contract-call? .pox-3-mock get-pox-info)) ) ;;------------------------------------- ;; Stacking helpers (error int to uint) ;;-------------------`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-1/stacking-dao-core-v1.clar:111` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `epare-length (get prepare-cycle-length (unwrap-panic (contract-call? .pox-3-mock get-pox-info)))) (start-block-next-cycle (contract-call? .pox-3-mock reward-cycle-to-burn-height (+ current-cycle u`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-1/stacking-dao-core-v1.clar:129` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `erve-trait>)) (let ( (stx-amount (unwrap-panic (contract-call? reserve-contract get-total-stx))) ) (try! (contract-call? .dao check-is-protocol (contract-of reserve-contract))) (ok (ge`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-1/stacking-dao-core-v1.clar:138` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `ount uint)) (let ( (ststx-supply (unwrap-panic (contract-call? .ststx-token get-total-supply))) ) (if (is-eq ststx-supply u0) u1000000 (/ (* stx-amount u1000000) ststx-supply)`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-1/stacking-dao-core-v1.clar:184` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `t stx-ststx) u1000000)) (total-stx (unwrap-panic (contract-call? reserve-contract get-total-stx))) (new-withdraw-init (+ (get withdraw-init current-cycle-info) stx-to-receive)) (nft-id (`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-1/stacking-dao-core-v1.clar:188` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `le-info) stx-to-receive)) (nft-id (unwrap-panic (contract-call? .ststx-withdraw-nft get-last-token-id))) ) (try! (contract-call? .dao check-is-enabled)) (try! (contract-call? .dao check`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-1/stacking-dao-core-v1.clar:216` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `epare-length (get prepare-cycle-length (unwrap-panic (contract-call? .pox-3-mock get-pox-info)))) (unlock-burn-height (+ pox-prepare-length start-block-cycle)) (withdrawal-cycle-info (get-cyc`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-1/strategy-v0.clar:63` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `efine-read-only (get-total-stacking) (unwrap-panic (contract-call? .reserve-v1 get-stx-stacking)) ) ;; Calculate STX outflow or inflow for next cycle. (define-read-only (get-outflow-inflow) (let`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-1/strategy-v0.clar:69` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `nflow) (let ( (total-withdrawals (unwrap-panic (contract-call? .reserve-v1 get-stx-for-withdrawals))) (total-idle (unwrap-panic (contract-call? .reserve-v1 get-stx-balance))) (outflow`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-1/strategy-v0.clar:70` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `stx-for-withdrawals))) (total-idle (unwrap-panic (contract-call? .reserve-v1 get-stx-balance))) (outflow (if (> total-withdrawals total-idle) (- total-withdrawals total-idle)`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-2/commission-v2.clar:129` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `-mainnet (get prepare-cycle-length (unwrap-panic (contract-call? 'SP000000000000000000002Q6VF78.pox-4 get-pox-info))) (get prepare-cycle-length (unwrap-panic (contract-call? .pox-4-mock get-po`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-2/commission-v2.clar:130` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `-info))) (get prepare-cycle-length (unwrap-panic (contract-call? .pox-4-mock get-pox-info))) ) )`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-2/data-core-v1.clar:30` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `ount uint)) (let ( (ststx-supply (unwrap-panic (contract-call? .ststx-token get-total-supply))) ) (if (is-eq ststx-supply u0) DENOMINATOR_6 (/ (* stx-amount DENOMINATOR_6) stst`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-2/direct-helpers-v1.clar:238` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `ces-unwrapped u0)) (wallet-ststx (unwrap-panic (contract-call? .ststx-token get-balance user))) (balance-ststx (+ wallet-ststx protocol-ststx)) (balance-stx (/ (* balance-ststx rati`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-2/direct-helpers-v2.clar:238` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `ces-unwrapped u0)) (wallet-ststx (unwrap-panic (contract-call? .ststx-token get-balance user))) (balance-ststx (+ wallet-ststx protocol-ststx)) (balance-stx (/ (* balance-ststx rati`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-2/native-stacking-pool-v1.clar:24` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `(err u609)) (define-constant pox-info (unwrap-panic (contract-call? 'SP000000000000000000002Q6VF78.pox-4 get-pox-info))) ;; Allowed contract-callers handling a user's stacking activity. (define-map`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-2/protocol-arkadiko-v1.clar:12` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `(user principal)) (let ( (vault (unwrap-panic (contract-call? 'SP2C2YFP12AJZB4MABJBAJ55XECVS7E4PMMZ89YZR.arkadiko-vaults-data-v1-1 get-vault user .ststx-token))) ) ;; Check status (if`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-2/protocol-arkadiko-v1.clar:12` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `(vault (unwrap-panic (contract-call? 'SP2C2YFP12AJZB4MABJBAJ55XECVS7E4PMMZ89YZR.arkadiko-vaults-data-v1-1 get-vault user .ststx-token))) ) ;; Check status (if (is-eq (get status vault) u1`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `version-2/protocol-bitflow-v1.clar:13` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `(let ( ;; Wallet (balance (unwrap-panic (contract-call? 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-token-v-1-2 get-balance user))) ;; Staked (user-data (contract-call`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-2/protocol-bitflow-v1.clar:13` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `(balance (unwrap-panic (contract-call? 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-token-v-1-2 get-balance user))) ;; Staked (user-data (contract-call? 'SPQC38PW542EQJ5M11CR25P7BS`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `version-2/protocol-bitflow-v1.clar:16` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `; Staked (user-data (contract-call? 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.earn-stx-ststx-v-1-2 get-user-data .ststx-token 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-tok`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `version-2/protocol-bitflow-v1.clar:18` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `get-user-data .ststx-token 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-token-v-1-2 user )) (staked (if (is-some user-data) (get total-currently-staked (unwr`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `version-2/protocol-bitflow-v1.clar:30` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `; Total LP tokens (lp-total-supply (unwrap-panic (contract-call? 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-token-v-1-2 get-total-supply))) ;; Pool balance stSTX (lp-balance-s`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-2/protocol-bitflow-v1.clar:30` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `al-supply (unwrap-panic (contract-call? 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stx-ststx-lp-token-v-1-2 get-total-supply))) ;; Pool balance stSTX (lp-balance-ststx (unwrap-panic (contract-`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `version-2/protocol-bitflow-v1.clar:33` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `ol balance stSTX (lp-balance-ststx (unwrap-panic (contract-call? .ststx-token get-balance 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stableswap-stx-ststx-v-1-2))) ;; User share (user-lp-sh`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-2/protocol-bitflow-v1.clar:33` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `contract-call? .ststx-token get-balance 'SPQC38PW542EQJ5M11CR25P7BS1CA6QT4TBXGB3M.stableswap-stx-ststx-v-1-2))) ;; User share (user-lp-share (/ (* user-total u1000000000000) lp-total-supply))`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `version-2/protocol-hermetica-v1.clar:12` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `rincipal)) (let ( (token-balance (unwrap-panic (contract-call? 'SPZA22A4D15RKH5G8XDGQ7BPC20Q5JNMH0VQKSR6.token-ststx-earn-v1 get-balance user))) (ratio (contract-call? 'SPZA22A4D15RKH5G8XDGQ`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-2/protocol-hermetica-v1.clar:12` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `n-balance (unwrap-panic (contract-call? 'SPZA22A4D15RKH5G8XDGQ7BPC20Q5JNMH0VQKSR6.token-ststx-earn-v1 get-balance user))) (ratio (contract-call? 'SPZA22A4D15RKH5G8XDGQ7BPC20Q5JNMH0VQKSR6.vault-sts`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `version-2/protocol-hermetica-v1.clar:13` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `ance user))) (ratio (contract-call? 'SPZA22A4D15RKH5G8XDGQ7BPC20Q5JNMH0VQKSR6.vault-ststx-earn-v1 get-underlying-per-token)) (wallet-amount (/ (* token-balance ratio) u1000000)) (queued-a`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `version-2/protocol-hermetica-v1.clar:24` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `ims (get deposit-claims (contract-call? 'SPZA22A4D15RKH5G8XDGQ7BPC20Q5JNMH0VQKSR6.vault-ststx-earn-v1 get-claims-for-address user))) ) (fold + (map get-claim-iter deposit-claims) u0) ) ) (def`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `version-2/protocol-hermetica-v1.clar:32` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `t)) (let ( (claim (contract-call? 'SPZA22A4D15RKH5G8XDGQ7BPC20Q5JNMH0VQKSR6.vault-ststx-earn-v1 get-claim claim-id)) ) (get underlying-amount (unwrap-panic claim)) ) )`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `version-2/protocol-velar-v1.clar:12` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `ncipal)) (let ( (total-lp-supply (unwrap-panic (contract-call? 'SP1Y5YSTAHZ88XYK1VPDH24GY0HPX5J4JECTMY4A1.ststx-aeusdc get-total-supply))) (user-wallet (unwrap-panic (contract-call? 'SP1Y5YS`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-2/protocol-velar-v1.clar:12` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `lp-supply (unwrap-panic (contract-call? 'SP1Y5YSTAHZ88XYK1VPDH24GY0HPX5J4JECTMY4A1.ststx-aeusdc get-total-supply))) (user-wallet (unwrap-panic (contract-call? 'SP1Y5YSTAHZ88XYK1VPDH24GY0HPX5J4JECT`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `version-2/protocol-velar-v1.clar:13` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `c get-total-supply))) (user-wallet (unwrap-panic (contract-call? 'SP1Y5YSTAHZ88XYK1VPDH24GY0HPX5J4JECTMY4A1.ststx-aeusdc get-balance user))) (user-staked (get end (contract-call? 'SP1Y5YSTAHZ8`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-2/protocol-velar-v1.clar:13` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `er-wallet (unwrap-panic (contract-call? 'SP1Y5YSTAHZ88XYK1VPDH24GY0HPX5J4JECTMY4A1.ststx-aeusdc get-balance user))) (user-staked (get end (contract-call? 'SP1Y5YSTAHZ88XYK1VPDH24GY0HPX5J4JECTMY4A1`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `version-2/protocol-velar-v1.clar:14` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `(user-staked (get end (contract-call? 'SP1Y5YSTAHZ88XYK1VPDH24GY0HPX5J4JECTMY4A1.farming-ststx-aeusdc-core get-user-staked user))) (user-total (+ user-wallet user-staked)) (pool-info (contr`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `version-2/protocol-velar-v1.clar:17` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `taked)) (pool-info (contract-call? 'SP1Y5YSTAHZ88XYK1VPDH24GY0HPX5J4JECTMY4A1.univ2-core do-get-pool u8)) ) (ok (/ (* user-total (get reserve0 pool-info)) total-lp-supply)) ) )`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `version-2/protocol-zest-v1.clar:11` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `nce (user principal)) (contract-call? 'SP2VCQJGH7PHP2DJK7Z0V48AGBHQAW3R3ZW1QF4N.zststx-v1-2 get-balance user) )`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `version-2/stacking-dao-core-v2.clar:129` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `tx-ststx) DENOMINATOR_6)) (nft-id (unwrap-panic (contract-call? .ststx-withdraw-nft-v2 get-last-token-id))) ) (try! (contract-call? .dao check-is-enabled)) (try! (contract-call? .dao ch`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-2/stacking-dao-core-v2.clar:307` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `n-mainnet (get reward-cycle-length (unwrap-panic (contract-call? 'SP000000000000000000002Q6VF78.pox-4 get-pox-info))) (get reward-cycle-length (unwrap-panic (contract-call? .pox-4-mock get-pox`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-2/stacking-dao-core-v2.clar:308` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `x-info))) (get reward-cycle-length (unwrap-panic (contract-call? .pox-4-mock get-pox-info))) ) ) ;;------------------------------------- ;; Migrate stSTX from V1 ;;----------------------------`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-2/stacking-dao-core-v2.clar:319` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `igrate-ststx) (let ( (balance-v1 (unwrap-panic (contract-call? .ststx-token get-balance .stacking-dao-core-v1))) ) (try! (contract-call? .dao check-is-protocol contract-caller)) (`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-2/stacking-dao-core-v3.clar:129` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `tx-ststx) DENOMINATOR_6)) (nft-id (unwrap-panic (contract-call? .ststx-withdraw-nft-v2 get-last-token-id))) ) (try! (contract-call? .dao check-is-enabled)) (try! (contract-call? .dao ch`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-2/stacking-dao-core-v3.clar:252` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `n-mainnet (get reward-cycle-length (unwrap-panic (contract-call? 'SP000000000000000000002Q6VF78.pox-4 get-pox-info))) (get reward-cycle-length (unwrap-panic (contract-call? .pox-4-mock get-pox`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-2/stacking-dao-core-v3.clar:253` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `x-info))) (get reward-cycle-length (unwrap-panic (contract-call? .pox-4-mock get-pox-info))) ) ) ;;------------------------------------- ;; Migrate stSTX from V1 ;;----------------------------`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-2/stacking-dao-core-v3.clar:264` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `igrate-ststx) (let ( (balance-v1 (unwrap-panic (contract-call? .ststx-token get-balance .stacking-dao-core-v1))) ) (try! (contract-call? .dao check-is-protocol contract-caller)) (`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-2/strategy-v3-pools-v1.clar:36` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `Currently stacking (total-stacking (unwrap-panic (contract-call? .reserve-v1 get-stx-stacking))) ;; New total amount to stack (total-idle (unwrap-panic (contract-call? .reserve-v1 get-stx`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-2/strategy-v3-pools-v1.clar:39` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `total amount to stack (total-idle (unwrap-panic (contract-call? .reserve-v1 get-stx-balance))) (total-withdrawals (unwrap-panic (contract-call? .reserve-v1 get-stx-for-withdrawals))) (new`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-2/strategy-v3-pools-v1.clar:40` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `-stx-balance))) (total-withdrawals (unwrap-panic (contract-call? .reserve-v1 get-stx-for-withdrawals))) (new-total-stacking (- (+ total-stacking total-idle) total-withdrawals)) ;; New tot`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-2/strategy-v4.clar:36` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `efine-read-only (get-total-stacking) (unwrap-panic (contract-call? .reserve-v1 get-stx-stacking)) ) ;; Calculate STX outflow or inflow for next cycle. (define-read-only (get-outflow-inflow) (let`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-2/strategy-v4.clar:42` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `nflow) (let ( (total-withdrawals (unwrap-panic (contract-call? .reserve-v1 get-stx-for-withdrawals))) (total-idle (unwrap-panic (contract-call? .reserve-v1 get-stx-balance))) (outflow (`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-2/strategy-v4.clar:43` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `stx-for-withdrawals))) (total-idle (unwrap-panic (contract-call? .reserve-v1 get-stx-balance))) (outflow (if (> total-withdrawals total-idle) (- total-withdrawals total-idle) u0`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/commission-btc-v1.clar:124` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `-mainnet (get prepare-cycle-length (unwrap-panic (contract-call? 'SP000000000000000000002Q6VF78.pox-4 get-pox-info))) (get prepare-cycle-length (unwrap-panic (contract-call? .pox-4-mock get-po`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/commission-btc-v1.clar:125` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `-info))) (get prepare-cycle-length (unwrap-panic (contract-call? .pox-4-mock get-pox-info))) ) )`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/data-core-v2.clar:22` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `get-total-stx))) (ststxbtc-supply (unwrap-panic (contract-call? .ststxbtc-token get-total-supply))) (stx-for-ststx (- total-stx-amount ststxbtc-supply)) ) (try! (contract-call? .dao che`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/data-core-v2.clar:32` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `ount uint)) (let ( (ststx-supply (unwrap-panic (contract-call? .ststx-token get-total-supply))) ) (if (is-eq ststx-supply u0) DENOMINATOR_6 (/ (* stx-amount DENOMINATOR_6) stst`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/data-core-v3.clar:22` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `get-total-stx))) (ststxbtc-supply (unwrap-panic (contract-call? .ststxbtc-token get-total-supply))) (ststxbtc-supply-v2 (unwrap-panic (contract-call? .ststxbtc-token-v2 get-total-supply)))`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/data-core-v3.clar:23` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `otal-supply))) (ststxbtc-supply-v2 (unwrap-panic (contract-call? .ststxbtc-token-v2 get-total-supply))) (stx-for-ststx (- total-stx-amount ststxbtc-supply ststxbtc-supply-v2)) ) (try! (c`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/data-core-v3.clar:33` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `ount uint)) (let ( (ststx-supply (unwrap-panic (contract-call? .ststx-token get-total-supply))) ) (if (is-eq ststx-supply u0) DENOMINATOR_6 (/ (* stx-amount DENOMINATOR_6) stst`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/direct-helpers-v3.clar:238` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `ces-unwrapped u0)) (wallet-ststx (unwrap-panic (contract-call? .ststx-token get-balance user))) (balance-ststx (+ wallet-ststx protocol-ststx)) (balance-stx (/ (* balance-ststx rati`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/direct-helpers-v4.clar:238` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `ces-unwrapped u0)) (wallet-ststx (unwrap-panic (contract-call? .ststx-token get-balance user))) (balance-ststx (+ wallet-ststx protocol-ststx)) (balance-stx (/ (* balance-ststx rati`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/position-zest-v2.clar:8` — HARDCODED_MAINNET_PRINCIPAL
- **Snippet:** `ate for new token (ok (contract-call? 'SP2VCQJGH7PHP2DJK7Z0V48AGBHQAW3R3ZW1QF4N.zststxbtc-token get-balance user)) )`
- **Why flagged:** Check this isn't accidentally left over from mainnet in a testnet/devnet build, or vice versa -- a classic deployment mistake.

### `version-3/rewards-v4.clar:327` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `n-mainnet (get reward-cycle-length (unwrap-panic (contract-call? 'SP000000000000000000002Q6VF78.pox-4 get-pox-info))) (get reward-cycle-length (unwrap-panic (contract-call? .pox-4-mock get-pox`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/rewards-v4.clar:328` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `x-info))) (get reward-cycle-length (unwrap-panic (contract-call? .pox-4-mock get-pox-info))) ) )`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/rewards-v5.clar:258` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `(let ( (ststxbtc-supply (unwrap-panic (contract-call? .ststxbtc-token get-total-supply))) (ststxbtc-supply-v2 (unwrap-panic (contract-call? .ststxbtc-token-v2 get-total-supply))`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/rewards-v5.clar:259` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `-supply))) (ststxbtc-supply-v2 (unwrap-panic (contract-call? .ststxbtc-token-v2 get-total-supply))) (total-supply (+ ststxbtc-supply ststxbtc-supply-v2)) (rewards-v1 (if (is-eq`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/rewards-v5.clar:381` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `n-mainnet (get reward-cycle-length (unwrap-panic (contract-call? 'SP000000000000000000002Q6VF78.pox-4 get-pox-info))) (get reward-cycle-length (unwrap-panic (contract-call? .pox-4-mock get-pox`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/rewards-v5.clar:382` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `x-info))) (get reward-cycle-length (unwrap-panic (contract-call? .pox-4-mock get-pox-info))) ) )`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/stacking-dao-core-btc-v1.clar:189` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `der tx-sender) (unlock-burn-height (unwrap-panic (contract-call? .stacking-dao-core-v4 get-withdraw-unlock-burn-height))) (nft-id (unwrap-panic (contract-call? .ststxbtc-withdraw-nft get-last`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/stacking-dao-core-btc-v1.clar:191` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `raw-unlock-burn-height))) (nft-id (unwrap-panic (contract-call? .ststxbtc-withdraw-nft get-last-token-id))) ) (try! (contract-call? .dao check-is-enabled)) (try! (contract-call? .dao ch`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/stacking-dao-core-btc-v1.clar:353` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `n-mainnet (get reward-cycle-length (unwrap-panic (contract-call? 'SP000000000000000000002Q6VF78.pox-4 get-pox-info))) (get reward-cycle-length (unwrap-panic (contract-call? .pox-4-mock get-pox`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/stacking-dao-core-btc-v1.clar:354` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `x-info))) (get reward-cycle-length (unwrap-panic (contract-call? .pox-4-mock get-pox-info))) ) )`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/stacking-dao-core-btc-v2.clar:198` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `der tx-sender) (unlock-burn-height (unwrap-panic (contract-call? .stacking-dao-core-v6 get-withdraw-unlock-burn-height))) (nft-id (unwrap-panic (contract-call? .ststxbtc-withdraw-nft get-last`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/stacking-dao-core-btc-v2.clar:200` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `raw-unlock-burn-height))) (nft-id (unwrap-panic (contract-call? .ststxbtc-withdraw-nft get-last-token-id))) ) (try! (contract-call? .dao check-is-enabled)) (try! (contract-call? .dao ch`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/stacking-dao-core-btc-v2.clar:372` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `n-mainnet (get reward-cycle-length (unwrap-panic (contract-call? 'SP000000000000000000002Q6VF78.pox-4 get-pox-info))) (get reward-cycle-length (unwrap-panic (contract-call? .pox-4-mock get-pox`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/stacking-dao-core-btc-v2.clar:373` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `x-info))) (get reward-cycle-length (unwrap-panic (contract-call? .pox-4-mock get-pox-info))) ) )`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/stacking-dao-core-btc-v3.clar:198` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `der tx-sender) (unlock-burn-height (unwrap-panic (contract-call? .stacking-dao-core-v6 get-withdraw-unlock-burn-height))) (nft-id (unwrap-panic (contract-call? .ststxbtc-withdraw-nft get-last`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/stacking-dao-core-btc-v3.clar:200` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `raw-unlock-burn-height))) (nft-id (unwrap-panic (contract-call? .ststxbtc-withdraw-nft get-last-token-id))) ) (try! (contract-call? .dao check-is-enabled)) (try! (contract-call? .dao ch`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/stacking-dao-core-btc-v3.clar:372` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `n-mainnet (get reward-cycle-length (unwrap-panic (contract-call? 'SP000000000000000000002Q6VF78.pox-4 get-pox-info))) (get reward-cycle-length (unwrap-panic (contract-call? .pox-4-mock get-pox`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/stacking-dao-core-btc-v3.clar:373` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `x-info))) (get reward-cycle-length (unwrap-panic (contract-call? .pox-4-mock get-pox-info))) ) )`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/stacking-dao-core-v4.clar:217` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `tx-ststx) DENOMINATOR_6)) (nft-id (unwrap-panic (contract-call? .ststx-withdraw-nft-v2 get-last-token-id))) ) (try! (contract-call? .dao check-is-enabled)) (try! (contract-call? .dao ch`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/stacking-dao-core-v4.clar:381` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `n-mainnet (get reward-cycle-length (unwrap-panic (contract-call? 'SP000000000000000000002Q6VF78.pox-4 get-pox-info))) (get reward-cycle-length (unwrap-panic (contract-call? .pox-4-mock get-pox`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/stacking-dao-core-v4.clar:382` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `x-info))) (get reward-cycle-length (unwrap-panic (contract-call? .pox-4-mock get-pox-info))) ) )`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/stacking-dao-core-v5.clar:226` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `tx-ststx) DENOMINATOR_6)) (nft-id (unwrap-panic (contract-call? .ststx-withdraw-nft-v2 get-last-token-id))) ) (try! (contract-call? .dao check-is-enabled)) (try! (contract-call? .dao ch`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/stacking-dao-core-v5.clar:400` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `n-mainnet (get reward-cycle-length (unwrap-panic (contract-call? 'SP000000000000000000002Q6VF78.pox-4 get-pox-info))) (get reward-cycle-length (unwrap-panic (contract-call? .pox-4-mock get-pox`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/stacking-dao-core-v5.clar:401` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `x-info))) (get reward-cycle-length (unwrap-panic (contract-call? .pox-4-mock get-pox-info))) ) )`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/stacking-dao-core-v6.clar:226` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `tx-ststx) DENOMINATOR_6)) (nft-id (unwrap-panic (contract-call? .ststx-withdraw-nft-v2 get-last-token-id))) ) (try! (contract-call? .dao check-is-enabled)) (try! (contract-call? .dao ch`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/stacking-dao-core-v6.clar:400` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `n-mainnet (get reward-cycle-length (unwrap-panic (contract-call? 'SP000000000000000000002Q6VF78.pox-4 get-pox-info))) (get reward-cycle-length (unwrap-panic (contract-call? .pox-4-mock get-pox`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/stacking-dao-core-v6.clar:401` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `x-info))) (get reward-cycle-length (unwrap-panic (contract-call? .pox-4-mock get-pox-info))) ) )`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/ststxbtc-migration-v1.clar:26` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `ress principal)) (let ( (balance (unwrap-panic (contract-call? .ststxbtc-token get-balance address))) (supported-position (contract-call? .ststxbtc-tracking-data get-supported-positions addr`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/ststxbtc-migration-v1.clar:43` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `c (migrate-self) (let ( (balance (unwrap-panic (contract-call? .ststxbtc-token get-balance contract-caller))) ) (if (> balance u0) (begin (try! (contract-call? .ststxbtc-toke`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/swap-ststx-ststxbtc-v1.clar:32` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `-amount tx-sender)) (asserts! (>= (unwrap-panic (contract-call? .ststx-token get-total-supply)) u1000000) (err ERR_LOW_SUPPLY)) (asserts! (>= (unwrap-panic (contract-call? .ststxbtc-token get`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/swap-ststx-ststxbtc-v1.clar:33` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `err ERR_LOW_SUPPLY)) (asserts! (>= (unwrap-panic (contract-call? .ststxbtc-token get-total-supply)) u1000000) (err ERR_LOW_SUPPLY)) (ok stx-amount) ) ) (define-public (swap-ststxbtc-for-st`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/swap-ststx-ststxbtc-v1.clar:49` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `-amount tx-sender)) (asserts! (>= (unwrap-panic (contract-call? .ststx-token get-total-supply)) u1000000) (err ERR_LOW_SUPPLY)) (asserts! (>= (unwrap-panic (contract-call? .ststxbtc-token get`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/swap-ststx-ststxbtc-v1.clar:50` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `err ERR_LOW_SUPPLY)) (asserts! (>= (unwrap-panic (contract-call? .ststxbtc-token get-total-supply)) u1000000) (err ERR_LOW_SUPPLY)) (ok ststx-amount) ) )`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/swap-ststx-ststxbtc-v2.clar:32` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `-amount tx-sender)) (asserts! (>= (unwrap-panic (contract-call? .ststx-token get-total-supply)) u1000000) (err ERR_LOW_SUPPLY)) (asserts! (>= (unwrap-panic (contract-call? .ststxbtc-token-v2`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/swap-ststx-ststxbtc-v2.clar:33` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `err ERR_LOW_SUPPLY)) (asserts! (>= (unwrap-panic (contract-call? .ststxbtc-token-v2 get-total-supply)) u1000000) (err ERR_LOW_SUPPLY)) (ok stx-amount) ) ) (define-public (swap-ststxbtc-for`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/swap-ststx-ststxbtc-v2.clar:49` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `-amount tx-sender)) (asserts! (>= (unwrap-panic (contract-call? .ststx-token get-total-supply)) u1000000) (err ERR_LOW_SUPPLY)) (asserts! (>= (unwrap-panic (contract-call? .ststxbtc-token-v2`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-3/swap-ststx-ststxbtc-v2.clar:50` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `err ERR_LOW_SUPPLY)) (asserts! (>= (unwrap-panic (contract-call? .ststxbtc-token-v2 get-total-supply)) u1000000) (err ERR_LOW_SUPPLY)) (ok ststx-amount) ) )`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-x/strategy-v3-wip.clar:244` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `t)) (let ( (current-stx-stacking (unwrap-panic (contract-call? .reserve-v1 get-stx-stacking))) (new-stx-stacking (+ current-stx-stacking inflow)) (new-stx-stacking-list (list-30-uint new`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-x/strategy-v3-wip.clar:352` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `nflow) (let ( (total-withdrawals (unwrap-panic (contract-call? .reserve-v1 get-stx-for-withdrawals))) (total-idle (unwrap-panic (contract-call? .reserve-v1 get-stx-balance))) (outflow`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).

### `version-x/strategy-v3-wip.clar:353` — UNWRAP_PANIC_EXTERNAL_CALL
- **Snippet:** `stx-for-withdrawals))) (total-idle (unwrap-panic (contract-call? .reserve-v1 get-stx-balance))) (outflow (if (> total-withdrawals total-idle) (- total-withdrawals total-idle)`
- **Why flagged:** unwrap-panic aborts the whole transaction on error, which is often fine, but check whether a graceful (err ...) would be more appropriate here (e.g. to avoid griefing via a malicious/broken trait implementation).


## INFO (3)

### `version-3/rewards-v3.clar:135` — AS_CONTRACT_WITH_CONTRACT_CALLER
- **Snippet:** `(if (> pool-owner-amount u0) (as-contract (stx-transfer? pool-owner-amount contract-caller (get receiver pool-owner-commission))) (ok true) ) ) ) (define-public (add-rewards-sbt`
- **Why flagged:** Note: as-contract overrides BOTH tx-sender and contract-caller to the contract's own principal (confirmed empirically in this project) -- this pattern is usually NOT a bug, but worth a second look if the surrounding logic assumes the ORIGINAL caller's identity.

### `version-3/rewards-v4.clar:129` — AS_CONTRACT_WITH_CONTRACT_CALLER
- **Snippet:** `(if (> pool-owner-amount u0) (as-contract (stx-transfer? pool-owner-amount contract-caller (get receiver pool-owner-commission))) (ok true) ) ) ) (define-public (add-rewards-sbt`
- **Why flagged:** Note: as-contract overrides BOTH tx-sender and contract-caller to the contract's own principal (confirmed empirically in this project) -- this pattern is usually NOT a bug, but worth a second look if the surrounding logic assumes the ORIGINAL caller's identity.

### `version-3/rewards-v5.clar:137` — AS_CONTRACT_WITH_CONTRACT_CALLER
- **Snippet:** `(if (> pool-owner-amount u0) (as-contract (stx-transfer? pool-owner-amount contract-caller (get receiver pool-owner-commission))) (ok true) ) ) ) (define-public (add-rewards-sbt`
- **Why flagged:** Note: as-contract overrides BOTH tx-sender and contract-caller to the contract's own principal (confirmed empirically in this project) -- this pattern is usually NOT a bug, but worth a second look if the surrounding logic assumes the ORIGINAL caller's identity.
