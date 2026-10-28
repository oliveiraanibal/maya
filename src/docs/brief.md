# Hypothesis and Assumptions

*Futuristic use case · Level 5 autonomous vehicle · UX exercise*

## Context

Maya is an AI concierge inside a fully autonomous (Level 5) car. She plans and runs the logistics of a single trip: routing, stops and calls to retailers. Michael, the user in our story, is in the car and either talks to her or uses the tablet; a passive LED strip at the base of the windscreen shows glanceable status. Maya acts with full delegated trust, like an executive assistant, within the limits Michael sets, and he can see and undo everything. Maya belongs to Michael, not to the car: she is in any car he signs in to, his own or a robotaxi. When nobody is in the car, Maya can also send it to run errands on its own (courier mode).

## Problem

Navigation handles routes, not commitments. Even in a driverless car the passenger still has to work out the sequence of stops, phone businesses, and re-plan by hand whenever something changes, so the freed-up time is not really free.

## Vision

*I share my needs and goals; everything else just happens, and I can see it happening.*

*With me in the car, Maya runs my trip. Without me, my car runs my errands.*

## Hypothesis

We believe that time-poor people will hand over trip logistics entirely to an AI that asks only what it cannot know (as many questions as needed, no more), acts on its own, follows the conversation (ambient intent), and makes every action visible and reversible. We will know we are right when users arrive on time, rarely undo what Maya did, and trust her with more over time.

Courier mode extends the bet: people will also let an empty car run errands on its own, as long as every handover is agreed before it leaves and reported when it's done.

## Hero scenario: the family dinner run

At 17:15 the car collects Michael at work and heads home by default. He tells Maya his needs: a family birthday dinner at 19:00, the kids and his wife to collect, and a new prescription from his messages as soon as possible. Maya asks only for the restaurant and the time, phones two pharmacies first (the first has no stock) and replans silently, then offers flowers and phones the florist. When his wife calls from the hair salon, Maya hears it, moves the pickup, and chimes. After that pickup, a message says his suit is ready at the dry cleaner: Maya offers to collect it on her own once the family is at the restaurant, he says yes, and she phones the shop to pay and agree the handover. The family arrives at 18:55 with 5 minutes of spare time, the flowers arrive first, and the empty car leaves in courier mode, collects the suit and charges nearby, ready to be back for them at 21:30. Three reroutes: default to plan, pharmacy (the world), pickup (the conversation). Plus one courier errand, run by the empty car.

## Scope

- **In:** sign-in by face (PIN or password as fallback) with a default route; Maya's access settings; briefing in needs and goals; a proactive suggestion tied to a known occasion; plan overview with spare time (5 min); live calls to retailers with payment from Maya Wallet; automatic reroutes; ambient intent; plan editing; two-screen UI (tablet plus passive strip); voice and touch parity; courier mode: errands that Maya suggests or that are scheduled from the Errands button, run by the empty car with an agreed handover, followed live on the phone (view only) and reported at the end.
- **Assumed, not designed:** payments happen automatically from Maya Wallet, up to the limit set in Maya's access (top-ups and statements are not designed); schools release the children to the car; the same car, with the suit, charges near the restaurant until Michael calls it, as he did at 17:15.
- **If I had a month:** other errand types beyond pick-ups and drop-offs, the bento menu's contents, a full activity log, wallet top-ups and statements, trust that grows over time, multi-passenger conflicts, merchant onboarding, support escalation to a human, competitive and analogous review, a proto-persona, a Wizard of Oz session, accessibility research and a study of real family trips.

## Success metrics (illustrative targets)

| Metric | Target |
|---|---|
| On-time arrival (within the 5-minute spare time) | 95% or more |
| Replans that keep spare time at or above zero | 90% or more |
| Questions Maya could have answered herself | Under 10% |
| Undo rate on automatic and ambient changes | Under 10% |
| Time from a change to a visible adapted plan | 3 seconds or less |
| Proactive suggestion acceptance | 50% or more |
| "Feels like a great assistant" rating | 4 / 5 or more |
| Courier errands completed without the user stepping in | 90% or more |
| Car back by the promised time after a courier run | 95% or more |

## Assumptions, ranked by risk

| # | Assumption | Risk | Confidence | How we would test it |
|---|---|---|---|---|
| A1 | Pre-trusted users accept "do first, show clearly, undo easily" | High | Medium | Wizard of Oz session (if I had a month) |
| A2 | Maya can predict the likely destination and learn the user's day and recurring places from habit and data (calendar, messages) | High | Medium | Prototype with a scripted calendar |
| A3 | **Ambient intent:** listening to cabin talk and calls is welcome, and false positives are cheap to undo | High | Low | Ambient-intent test |
| A4 | Retailers cooperate with a self-identified AI caller (hold, stock, payment, timing) | High | Low | Scripted calls to local shops (if I had a month) |
| A13 | Shops will hand items to, or take them from, an empty car that opens one door with a one-time code | High | Low | Scripted calls to local shops (if I had a month) |
| A14 | People will let their empty car run an errand, and accept a cabin camera that checks the cabin and the handover | High | Medium | Courier trust test |
| A15 | An empty Level 5 car may legally drive and stop on its own to run errands | High | Medium | Assumed; regulation review (if I had a month) |
| A5 | Automatic payments from Maya Wallet, up to a limit, are acceptable | Medium | Medium | Out of scope for now |
| A6 | Users accept as many questions as needed when each is clearly necessary | Medium | Medium | Wizard of Oz session (if I had a month) |
| A7 | A proactive suggestion tied to a known occasion (a birthday) is welcome | Medium | Medium | Concept test |
| A8 | Spare time (5 min) gives at-a-glance confidence | Medium | Medium | Glance test |
| A9 | Silent changes with a chime, heard phrase and Undo are understood in a noisy cabin | Medium | Medium | Replan legibility test |
| A10 | A passive strip carries enough glanceable information while the tablet holds all interaction | Medium | Medium | Glance test |
| A11 | Voice and touch parity is achievable for every task | Medium | Medium | Touch-only run |
| A12 | On-time arrival is the dominant success criterion | Medium | Medium | Short survey |

## Design principles

1. **Ask only what she can't know,** as many times as needed.
2. **Ambient intent:** the plan follows the conversation.
3. **Speak only when needed;** the screen is the confirmation.
4. **Do first, show clearly, undo easily** (no countdown).
5. **The plan is alive:** the world, the conversation or the user can reshape it, and the ripple is visible.
6. **Spare time is the promise:** 5 minutes, always visible; green above 4, amber 0 to 4, red below 0.
7. **Tablet for interaction, strip for glances** (the strip carries nothing unique).
8. **Voice and touch are equals.**
9. **With you or without you:** when the car is empty it works for you, but only with an agreed handover (no handoff, no commitment).
