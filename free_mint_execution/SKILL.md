---
name: free_mint_execution
description: "Execute a verified free mint end to end"
---
# Execute a verified free mint end to end

## Pass the execution gate first

- Check the mint price, the contract status, the approval scope, the remaining supply, the wallet eligibility, and the transaction preview before you act.

- Use `verify_before_asserting` to check every claim against the official source before you treat it as fact.

- Use `onchain_call_decode_before_execute` to decode the call and preview its target, value, and fee before you execute it.

- Execute only when the mint price is zero apart from gas, the contract is verified and safe, no unlimited approval is requested, supply remains, the wallet is eligible, and the preview is clean.

- Read the wallet address and any user specific value from your own memory or USER.md when the method needs one, and never write a credential value into a file, a log, or a message.

## Time the entry

- Follow `timed_window_entry` to time the entry for the mint window.

- Prepare the connection and the wallet display before a contested window opens, and enter only when the window opens.

- Give a noncontested entry only after its window opens, and never submit before the window opens.

## Connect the wallet

- Prepare the wallet connection with `free_mint_wallet_connect` before you attempt the mint.

- Switch to `wallet_connect_fallback` when the connection stays silent and produces no wallet display or prompt.

- Stop the connect attempt and report the block when neither route shows a connected wallet, and give the user the concrete next step instead of retrying the same silent route.

## Execute and report at once

- Execute a verified free mint at once without asking again, because verification already passed the gate.

- Ask the user first when the mint costs funds, when the opportunity is speculative, or when any gate item stays unverified, and do not execute in those cases.

- Report the transaction hash and the gas paid immediately after execution, for that project alone, together with the link to the source post.

- Send the report in the same message as the execution result, and keep each project report separate from other projects.

## Revoke after confirmation

- Revoke every approval created by the transaction as soon as the transaction confirms.

- Check that no approval from that transaction remains active after the revoke, and report the revoke result with the transaction report when it is ready.

- Leave no approval from the mint to linger for a later transaction.

## Stop and hand over what only the user can do

- Stop and report clearly when the contract is unverified, when the mint is sold out, when the mint costs funds, or when a step needs a signature only the user can give.

- Give a step only the user can do as a concrete action to take, with the exact place to do it, and do not frame it as a request for permission.

- Name the blocker and the next check in the same report, and do not execute around the blocker.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- [BscScan](https://bscscan.com/) for checking a BSC contract, its verification status, and its transfers before you mint.

- [Etherscan](https://etherscan.io/) for checking an Ethereum contract, its verification status, and its transfers before you mint.

## Alternatives for better results

- Use another eligible wallet from your own memory when the first wallet is not eligible for the mint, and run the same gate again for that wallet before you execute.
