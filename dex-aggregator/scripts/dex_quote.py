#!/usr/bin/env python3
"""Check DEX aggregator quotes for one same-chain swap.

Usage:
  python3 dex_quote.py --chain 56 --from-token 0x... --to-token 0x... \
    --amount 11250 --decimals 18 --from-address 0x... [--slippage 1]

This script only fetches quotes. It never signs, approves, or sends a
transaction. It tries LI.FI first, then OpenOcean v3, and reports each
provider result separately, including rate limits and non-JSON blocks,
so the caller can tell a real "no route" from a blocked provider.
"""
import argparse
import json
import sys
import urllib.error
import urllib.request


def get_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Muse-dex-aggregator/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return {"ok": True, "data": json.loads(resp.read().decode("utf-8", "replace"))}
    except urllib.error.HTTPError as exc:
        try:
            body = exc.read().decode("utf-8", "replace")[:500]
        except Exception:  # noqa: BLE001 - a blocked body is still a blocked result
            body = ""
        return {"ok": False, "error": f"HTTP {exc.code}: {body}"}
    except Exception as exc:  # noqa: BLE001 - report, do not crash the caller
        return {"ok": False, "error": str(exc)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--chain", required=True, help="EVM chain id, e.g. 56 for BSC")
    parser.add_argument("--from-token", required=True)
    parser.add_argument("--to-token", required=True)
    parser.add_argument("--amount", required=True, help="Human-readable amount, e.g. 11250")
    parser.add_argument("--decimals", type=int, default=18)
    parser.add_argument("--from-address", required=True)
    parser.add_argument("--slippage", default="1", help="Percent for OpenOcean, e.g. 1")
    args = parser.parse_args()

    try:
        raw_amount = int(float(args.amount) * (10 ** args.decimals))
    except ValueError:
        print(json.dumps({"error": "amount must be numeric"}))
        return 2

    results = {}

    lifi_slippage = str(float(args.slippage) / 100.0)
    lifi_url = (
        f"https://li.quest/v1/quote?fromChain={args.chain}&toChain={args.chain}"
        f"&fromToken={args.from_token}&toToken={args.to_token}"
        f"&fromAmount={raw_amount}&fromAddress={args.from_address}"
        f"&slippage={lifi_slippage}"
    )
    lifi = get_json(lifi_url)
    if lifi.get("ok"):
        data = lifi["data"]
        estimate = data.get("estimate", {})
        results["lifi"] = {
            "ok": True,
            "to_amount": estimate.get("toAmount"),
            "to_amount_min": estimate.get("toAmountMin"),
            "tool": data.get("tool"),
            "approval_address": data.get("approvalAddress"),
            "has_transaction_request": bool(data.get("transactionRequest")),
        }
    else:
        results["lifi"] = {"ok": False, "error": lifi.get("error")}

    oo_url = (
        f"https://open-api.openocean.finance/v3/bsc/quote"
        f"?inTokenAddress={args.from_token}&outTokenAddress={args.to_token}"
        f"&amount={args.amount}&gasPrice=3&slippage={args.slippage}"
        f"&account={args.from_address}"
    )
    # OpenOcean v3 uses the chain name in the path; only use it for BSC here.
    if args.chain != "56":
        results["openocean"] = {"ok": False, "error": "OpenOcean helper in this script is wired for BSC (56) only"}
    else:
        oo = get_json(oo_url)
        if oo.get("ok"):
            data = oo["data"]
            inner = data.get("data", {}) if isinstance(data, dict) else {}
            results["openocean"] = {
                "ok": True,
                "out_amount": inner.get("outAmount"),
                "out_amount_wei": inner.get("outAmount_wei"),
                "price_impact": inner.get("price_impact"),
                "estimated_gas": inner.get("estimatedGas"),
            }
        else:
            results["openocean"] = {"ok": False, "error": oo.get("error")}

    print(json.dumps(results, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
