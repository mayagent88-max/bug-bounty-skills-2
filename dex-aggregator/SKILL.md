# DEX Aggregator Quote Check

Use this skill when a swap through one router fails, especially when the Binance Agentic Wallet CLI says "No liquidity available", and the user still wants to sell a token on the same chain. It checks other DEX aggregators before you tell the user a token cannot be sold.

## Never report a global no-liquidity result from one router

- Say exactly which route failed, with its exact error, and which routes you still have to check. A "No liquidity available" answer from one router means no liquidity on that router, not no liquidity anywhere.

- Check in this order after the first router fails: LI.FI, OpenOcean, a browser check on PancakeSwap for BSC, and a listing check on a centralized exchange where the token may be listed. Only after all of those checks can you report that no verified sale route was found at that time.

- For a token that is listed on a centralized exchange, say that route by name, with its transfer gas, deposit time, and price risk during the move, instead of leaving the user to discover it alone.

## Check the first router, then the aggregators

- Run the wallet's own quote first, so you know the baseline failure. For the Binance Agentic Wallet, that is `baw market-order quote` with the full from token, to token, amount, and chain id.

- If that quote fails, do not stop there. Run the helper script below for the same pair, amount, and sender address. It only fetches quotes and never signs, approves, or sends a transaction.

- Run `python3 ~/workspace/custom-skills/dex-aggregator/scripts/dex_quote.py --chain 56 --from-token <from> --to-token <to> --amount <human amount> --decimals <decimals> --from-address <wallet> --slippage 1` for BSC. Change the chain, tokens, amount, and decimals for other chains, and remember the OpenOcean part of the helper is wired for BSC only.

- Read each provider result separately. A rate limit, a Cloudflare block, or a non-JSON reply is a blocked provider, not proof that no route exists. A clean quote with a to amount, a minimum amount, and a price impact is a real route. No route from every provider is a stronger no-liquidity result than one router alone.

## Compare routes and present the result

- Compare the wallet quote, the LI.FI quote, and the OpenOcean quote on the same amount. Report the output amount, the minimum amount after slippage, the price impact, and the gas or fee estimate when the provider returns one.

- Reject a route on the spot when its price impact is very high or its output value is far below the wallet price for the same amount. Show the loss in plain numbers instead of only naming the percentage.

- Tell the user which providers were blocked and why, instead of hiding a blocked check behind a general "cannot sell" answer. Name the exact error, such as a LI.FI 429 rate limit or an OpenOcean 403 block.

- If every DEX route fails or is too loss-making, say so and offer the centralized exchange route as a separate option: move the token to an exchange where it is listed and sell it there, with its own transfer gas, deposit time, and price risk during the move. Do not present that move as a DEX swap.

## Execution is separate and untested

- A quote is not an execution. Do not execute an aggregator route from a quote alone.

- If the user confirms a specific aggregator quote, show the full transaction request first, including the destination contract, the data, the value, the approval address when one is needed, and the gas estimate. Get a clear confirmation for that exact quote before any signing step.

- Execution through the Binance Agentic Wallet would use its contract call preview and execute flow, with Developer Mode on, and only after the preview is shown. That aggregator execution path is untested in this workspace as of 31 October 2026, so label it untested and do not claim it works until a preview succeeds for a real pair.

- Never approve an unlimited token spend. Approve only the amount in the confirmed quote when an approval is needed.

## Known limits observed 31 October 2026

- LI.FI at `https://li.quest/v1/quote` needs no API key for basic use, but unauthenticated quotes are limited to 75 requests per 2 hours, and a shared IP can hit that limit. On 31 October 2026 the shared IP returned code 1005, "Rate limit exceeded, retry in 47 minutes", for both a WBNB to USDT test and an IAO to WBNB test.

- OpenOcean v3 at `https://open-api.openocean.finance/v3/bsc/quote` needs no API key in its docs, but a direct call from this workspace returned a Cloudflare challenge page and then HTTP 403 on 31 October 2026. When that happens, use a browser task on the aggregator site as the fallback check instead of repeating the blocked call.

- SwapAPI at `https://api.swapapi.dev/v1/swap/<chain>` returned HTTP 404 "Application not found" on 31 October 2026, so do not rely on it until it is re-verified.

- This skill does not fix a wallet that a DEX website cannot see. A Binance Agentic Wallet is not a browser extension wallet, so a web DEX may list no connector for it. In that case the in-app swap, the wallet's own CLI, or a move to a listed centralized exchange are the remaining routes, and each carries its own gas and price risk.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- [LI.FI](https://li.quest/) for same-chain and cross-chain aggregator quotes without an API key at basic limits.

- [OpenOcean](https://openocean.finance/) for DEX aggregator quotes across many chains, with a browser fallback when its API is blocked.

- [PancakeSwap](https://pancakeswap.finance/) for a manual BSC DEX check in a browser, after confirming the wallet that site can actually connect to.

## Alternatives for better results

- Check the token on a second to token, such as USDT and then USDC, before concluding there is no route, because one pair can be empty while another has depth.

- Check a smaller amount as well as the full amount, because a large amount can fail on price impact while a smaller amount routes, and that split changes the advice you give the user.
