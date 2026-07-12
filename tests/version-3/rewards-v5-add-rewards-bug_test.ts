import { describe, it, expect } from "vitest";
import { Cl } from "@stacks/transactions";
import { DataPools } from "../wrappers/data-pools-helpers";

const accounts = simnet.getAccounts();
const deployer = accounts.get("deployer")!;
const caller = accounts.get("wallet_1")!;
const poolOwnerReceiver = accounts.get("wallet_2")!;

const dataPools = new DataPools(deployer);

const POOL = `${deployer}.stacking-pool-v1`;

describe("rewards-v5 add-rewards — contract-caller/tx-sender mismatch bug", () => {
  it("REPRO: add-rewards reverts once the pool has a nonzero owner-commission share", () => {
    const setShareResult = dataPools.setPoolOwnerCommission(
      deployer,
      POOL,
      poolOwnerReceiver,
      0.5,
    );
    expect(setShareResult).toBeOk(Cl.bool(true));

    const ownerCommission = dataPools.getPoolOwnerCommission(POOL);
    console.log("pool-owner-commission after set:", Cl.prettyPrint(ownerCommission));

    const addRewardsResult = simnet.callPublicFn(
      "rewards-v5",
      "add-rewards",
      [Cl.principal(POOL), Cl.uint(1_000_000)],
      caller,
    );

    console.log(
      "add-rewards result (owner-share > 0):",
      Cl.prettyPrint(addRewardsResult.result),
    );

    expect(addRewardsResult.result).toBeErr(Cl.uint(1));
  });

  it("CONTROL: add-rewards succeeds when owner-commission share is 0 (default)", () => {
    const POOL_NO_OWNER_SHARE = `${deployer}.pox-fast-pool-v2-mock`;

    const addRewardsResult = simnet.callPublicFn(
      "rewards-v5",
      "add-rewards",
      [Cl.principal(POOL_NO_OWNER_SHARE), Cl.uint(1_000_000)],
      caller,
    );

    console.log(
      "add-rewards result (owner-share == 0, control):",
      Cl.prettyPrint(addRewardsResult.result),
    );

    expect(addRewardsResult.result).toBeOk(Cl.bool(true));
  });
});