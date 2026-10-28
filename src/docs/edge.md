# Edge Cases and Validation Plan

Seventeen edge cases and six tests, each tied to the assumptions (A1 to A15) in the Hypothesis and Assumptions document. Cases 11 to 17 and the courier trust test cover courier mode.

## Edge-case list

| # | Edge case | Why it matters | Expected behaviour | Assumption |
|---|---|---|---|---|
| 1 | No pharmacy on the route has stock | The core goal (prescription as soon as possible) fails | Widen the search, show it on screen, ask only if the detour breaks spare time | A4 |
| 2 | Spare time goes negative | On-time arrival is the main promise | Show the fixes, cheapest first, such as asking the restaurant to hold the table (V2); the strip turns red | A8, A12 |
| 3 | **Ambient false positive** (a child says "let's go to the park") | The riskiest assumption | Act only on high confidence, otherwise ask; chime, heard phrase, and Undo | A3 |
| 4 | The chime is missed | Michael does not know the plan changed | The change stays in the ledger, and the strip repeats it once | A9 |
| 5 | Florist cannot deliver before 19:00 | The gift is part of the on-time story | Try the next florist; otherwise offer a pickup stop | A4 |
| 6 | Pharmacist refuses an AI caller | Depends on staff cooperation | Next pharmacy, with the refusal logged | A4 |
| 7 | Child not at the pickup point | Safety and delay | Alert on the tablet, wait window, school call | |
| 8 | Connectivity loss | Everything backstage runs in the cloud | Keep the current plan, strip shows "Offline", edits queue | |
| 9 | Dinner time or place changes by message | Same pattern as the wife's call | Ambient update from messages, same chime and Undo | A3 |
| 10 | Several people speak | Whose voice counts? | Commands only from the signed-in user; other speech is context only | A3, A11 |
| 11 | Shop not ready, or nobody comes to the car | The car can't wait for ever, and the return time is the promise | Wait within a set window, then leave so the car is back on time; the report (C3) says what happened, and the errand goes back to Errands (C4) to try again | A13 |
| 12 | Wrong item loaded, or more than one | The cabin camera is the only witness | The camera checks the item against the order before the door locks; if it doesn't match, Maya texts the shop and waits within the window for a fix; the report shows what the camera saw | A14 |
| 13 | Someone or something left in the cabin (a person, a pet, a bag) | Courier mode needs an empty cabin; safety first | A person or a pet stops courier mode from starting. A bag gets "Please take your belongings", said once with a caption, and a note on the phone | A14 |
| 14 | Car needed earlier | Plans change during dinner | Michael calls the car, as he did at 17:15. It is the same car, because his suit is inside: it comes from the charging station near the restaurant, or finishes the handover first if it is still mid-errand, and the phone says when it will arrive | A14 |
| 15 | Return time at risk (traffic, a slow handover) | Being back on time is the courier promise | Tell Michael early on the phone, with the new time; never late in silence | A14 |
| 16 | Wrong door, or the code is shared or reused | The car and what's inside must stay safe | The code opens only the agreed door, once, at the agreed place and time; a wrong code opens nothing, and the code expires when the door closes | A13 |
| 17 | Item not allowed (too big, dangerous, an animal, or needing a signature or ID) | Not every errand suits an empty car | Maya checks while booking and declines before anything is booked: no handoff, no commitment | A13, A15 |

Cases 1, 3 and 4 appear in the prototype, and case 2 has its own screen (V2); the rest stay as a list.

## Validation plan

| Test | What it checks | Method | Success signal | Assumptions |
|---|---|---|---|---|
| Wizard of Oz briefing (if I had a month) | Questions needed, natural language | A person plays Maya's voice with a prototype tablet, 5 participants | Completion without confusion; count of questions | A1, A6 |
| **Ambient-intent false positives** | Trust and creepiness | Scripted audio clips (true changes and decoys), measure Undo and reaction | Few false positives; chime and heard phrase understood | A3, A9 |
| Glance test | Strip and tablet readability | 5-second exposure: "What's next? How much spare time?" | 80% or more correct | A8, A10 |
| Replan legibility | Before and after understanding | Show it, ask "what changed?" | Understood in under 5 seconds | A9 |
| Touch-only run | Parity | Complete briefing and a plan edit without speaking | Same completion as voice | A11 |
| **Courier trust test** | Willingness to send the empty car; trust in the report | Clickable courier flow (S18 to C3) with 5 participants: what would they send, and what would stop them? | 4 of 5 would send it for an everyday errand; the report is understood without help | A14 |

**Solo-friendly:** the glance, legibility, touch-only and courier trust tests can run remotely on a clickable prototype. The Wizard of Oz briefing moves to the one-month list. Retailer cooperation (A4, and A13 for courier handovers) would be tested with scripted calls to a few local shops if I had a month.
