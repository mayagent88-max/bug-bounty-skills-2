# Sell an NFT Across Markets

Use this skill when the user wants to sell an NFT from the Binance Agentic Wallet, or when a single marketplace shows no listing, no floor, or no buyer. Check several markets before you say an NFT cannot be sold, and never say a global no-sale result from one marketplace alone.

## Verify ownership and transferability first

- Confirm the NFT on chain before any sale step. Use `baw wallet tx-history` and the chain explorer for the contract address and token id, and confirm the wallet address in the result is the user's wallet.

- Check whether the token is soulbound, non-transferable, or locked by its contract. If it is soulbound, stop and say it cannot be sold, with the contract evidence, instead of searching for a buyer.

- Check the token standard and the chain. BSC NFTs need BSC markets and BSC gas in BNB. Do not list an ETH-only market as a route for a BSC token, or a BSC market as a route for an ETH token.

## Check several markets, not one

- Check floor price, recent sales, and active listings for the exact collection contract on each market that supports the chain. For BSC, check OpenSea, Element, NFTrade, and tofuNFT, plus the project's own marketplace when one exists. For ETH, check OpenSea, Blur, and Magic Eden.

- Compare the same collection, not a similarly named collection. Match the full contract address every time, because cloned names are a real scam route.

- Record for each market: floor, best listing for this token id when one exists, royalty, marketplace fee, and estimated gas. A floor from a different token tier or a different collection is not a floor for this token.

- If one market has no listing, check the next market before reporting. If every market has no buyer, report the per-market result, not a single-market failure.

## Choose the net best route and execute only when verified

- Choose the route with the highest net received amount after royalty, marketplace fee, and gas, not the highest headline floor alone.

- Show the user the chosen market, the listing price, the royalty, the fee, the gas estimate, and the net received amount before execution, unless the user has already given full control for NFT sales and the route is live verified. Even with full control, report the transaction hash, the market, the price, and the net amount immediately after execution.

- Never approve an unlimited marketplace approval. Approve only the specific token id for the specific marketplace contract in the confirmed listing, and only after the contract-call preview is shown and checked.

- For a sale through the Binance Agentic Wallet, use its contract call preview and execute flow, with Developer Mode on, and only after the preview shows the exact marketplace contract, token id, and price. That NFT marketplace execution path is untested in this workspace as of 31 October 2026, so label it untested and do not claim a listing succeeded until the marketplace shows it live and the wallet history confirms the transaction.

- If a listing fails, a buyer never appears, or the net is below the user's threshold for that NFT, hold the NFT and report the market check. Do not lower the price without a new instruction, and do not move the NFT to another wallet just to try a different market unless the user confirms that move and its gas cost.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- [OpenSea](https://opensea.io/) for multi-chain NFT listings, floors, and sales, after matching the full collection contract.

- [Element](https://element.market/) for BSC and multi-chain NFT markets.

- [Magic Eden](https://magiceden.io/) for multi-chain NFT markets, including ETH collections.

## Alternatives for better results

- Check a lower listing price only as a separate, confirmed choice, with the new net amount shown first, because a lower price can create a sale that a high floor never will.

- Check the project's own marketplace and social channels for a buyer or a task reward tied to holding the NFT, because selling can lose a reward that holding would keep.
