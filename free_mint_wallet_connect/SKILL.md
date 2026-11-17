---
name: free_mint_wallet_connect
description: "Connect a wallet for a timed free mint"
---
# Connect a wallet for a timed free mint

## Prepare the connect step before the window

- Verify the mint price, the chain, the contract and the start time from the live project page before you prepare any connect step.

- Confirm which wallet route the mint site can actually use before the window opens, because a route that looks available can fail when the window starts.

- Prepare the exact connect step in advance for a mint with a fixed start time, so the user does not wait for instructions while the window is open.

- Keep the mint unexecuted when price, contract or preview checks fail, and report the failed check instead of giving a connect step.

## Give an actionable connect step first

- Give the user a direct sign link into the wallet app as the first connect step when the site offers one, because a plain project link leaves the user to find the connect button alone.

- Give a QR code for the wallet app as the fallback when no direct sign link exists, and say that the user scans it in the wallet app.

- Never present a plain project link alone as the connect step for a timed mint.

- Name the exact action the user takes next, such as opening the sign link in the wallet app or scanning the QR code, instead of saying only to connect.

## Separate the wallet routes

- Use the wallet command line route when the wallet offers one and the mint can run through it, and keep that route separate from any browser route.

- Use the browser sign route only when the mint site needs a browser wallet connection, and say clearly that connection and signing stay with the user in the wallet app.

- Do not claim a browser site can see a wallet that is not a browser extension wallet, and say which route remains when the site cannot see it.

- Stop at the connection or signing step when that step belongs to the user, and report the step as waiting for the user instead of claiming the mint is underway.

## Report a stalled or missed window plainly

- Report the connect result at once, with whether the wallet connected, whether the mint ran, and the transaction hash when one exists.

- Report a missed window at once with the time it closed and the connect step that failed, instead of leaving the mint as pending.

- Keep a timed mint held for its start time only when the start time is verified, and say the exact time you will return to it.

- Do not retry a failed connection or signing step repeatedly without a new route, and say what changed before you try again.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Offer the wallet command line route as an alternative when the browser route cannot see the wallet, and say what that route can and cannot do.

- Ask the user before the window which route they prefer when both routes exist, so the first attempt uses their chosen route.

- Check the project page again at the window start when the connect button or mint button was not visible earlier, because a site can enable it only at start time.
