# Hero Scenario and Conversation Script

One evening, ten scenes, three reroutes and one courier errand: Maya takes Michael, a father of two, from work to a 19:00 family dinner, then sends the empty car to collect his suit, speaking only when she needs him and showing everything else on screen.

## The scenario

A Level 5 car collects Michael at work at 17:15. His needs: collect his son (school), daughter (kindergarten) and wife (home), and get a new prescription from his text messages as soon as possible, all before a family birthday dinner at 19:00 at "the usual Italian on Main Street". Maya plans to arrive at 18:55, which leaves **5 minutes of spare time**.

**What Maya knows:** both schools, home, the calendar (a birthday of a female family member), Michael's messages. **What she doesn't know:** the restaurant, the dinner time, and which pharmacy can fill the prescription.

**Assumptions:** payments happen automatically from Maya Wallet; the schools release the children to the car (pre-authorised); the florist delivers to the restaurant (no stop); Michael is in the car for the pharmacy, so he can collect in person. In courier mode, the dry cleaner's staff open one door of the car with a code that Maya texts them.

## Three reroutes

| # | Reroute | Cause | Michael's involvement |
|---|---|---|---|
| 1 | Default route (home) to the real plan | Habit prediction, then the briefing | The briefing itself |
| 2 | First pharmacy to a second pharmacy | The world: no stock | None, visible on screen |
| 3 | Pickup moved from home to the hair salon | The conversation: the wife's call (ambient intent) | None, chime and Undo |

Plus one courier errand, which is not a reroute: after dropping the family at the restaurant, the empty car collects a suit from the dry cleaner and is back for them at 21:30.

## The day in numbers

Spare time stays at 5 minutes in every version of the plan.

| Stop | Plan v1 | After reroute 2 | After reroute 3 |
|---|---|---|---|
| Leave work | 17:15 | 17:15 | 17:15 |
| School (son) | 17:35 | 17:35 | 17:35 |
| Pharmacy 1 (no stock) | 17:50 | removed | removed |
| Kindergarten (daughter) | 18:10 | 17:55 | 17:55 |
| Pharmacy 2 | none | 18:10 | 18:10 |
| Wife | 18:33 (home) | 18:33 (home) | 18:30 (hair salon) |
| Restaurant (dinner 19:00) | 18:55 | 18:55 | 18:55 |
| Flowers delivered | 18:45 | 18:45 | 18:45 |
| Dry cleaner (car alone, courier mode) | none | none | 19:20 (booked at 18:34) |
| Car back for the family | none | none | 21:30 (promised; after the story ends) |

## Script

Screen tags (S01 to S20, C1 to C5) refer to the Screen Plan. Anything not in quotes happens on screen only.

**Scene 1: Boarding and sign-in (17:15)** [S01, S02]

- Michael gets in. The car expects him and signs him in by face; if his face isn't recognised he uses his PIN or password, and anyone else can tap "Not Michael? Switch profile". [S01]
- The car starts moving straight away towards the most probable destination. Screen: "Welcome back, Michael" and "Going home, 17:48". [S02]
- **Maya:** "Hi, I'm Maya, your concierge for the trip. How can I assist you?"
- Touch twin: Adjust opens Maya's access, where Michael chooses what she may do on her own. [S03]

**Scene 2: Briefing, in needs and goals** [S04 to S07]

- **Michael:** "Hi Maya. Family dinner tonight. Let's get the kids and my wife, and I need that new prescription from my messages as soon as possible." [S04]
- **Maya:** "Where is the dinner?" [S06]
- **Michael:** "The usual Italian on Main Street."
- **Maya:** "What time?"
- **Michael:** "Seven."
- Screen: the "New plan" card fills in as they talk, including the prescription reference (RX-48317). Maya does not read it back. Then "Building the plan", with every detail still editable. [S07]
- Touch twin: Michael taps Maya's bar to type [S05], and answers Maya's questions in the search field [S06].

**Scene 3: Pharmacy search (17:19), screen only** [S08, S09]

- The prescription is the urgent to-do, so the first call goes to the nearest pharmacy on the route. The pharmacy pin on the map is dotted until confirmed.
- Call 1. **Maya:** "Hello, I'm Maya, an AI assistant calling to ask about a prescription's availability, reference RX-48317. Do you have it, and how soon can we pick it up?" **Pharmacist:** "One moment, please hold." (on hold 0:35) **Pharmacist:** "Sorry, we don't have it." **Maya:** "Thank you."
- Call 2. **Maya:** (same question) **Pharmacist:** "One moment, please hold." (on hold 0:28) **Pharmacist:** "Yes, we have it." **Maya:** "I'd like to pay now and have it ready in ten minutes, please. We'll collect it at 18:10." **Pharmacist:** "OK. I'm sending the payment reference now. Thank you." [S08]
- Screen: "Paid", then a quiet "Plan updated" banner: pharmacy 1 crossed out, pharmacy 2 after the kindergarten, spare time still +5 min. No input needed. [S09]

**Scene 4: Flowers (17:22)** [S10, S11]

- **Maya:** "It's a birthday dinner. Would you like flowers waiting at the restaurant before we arrive?" [S10]
- **Michael:** "Yes. White roses."
- Screen: until Michael answers, the suggestion shows the florist but no bouquet choices, and the florist pin is dotted. Then, with Maya silent: (1) "Called Main St Florist" (2) live transcript: **Maya:** "Hello, I'm Maya, an AI assistant calling for a customer. I'd like white roses delivered to the Italian restaurant on Main Street before seven tonight. Can you do that?" **Florist:** "Yes, we can deliver by 18:45." **Maya:** "Perfect. I'll pay now. Please leave the bouquet at reception for Michael to collect." (3) "Delivery agreed: 18:45" (4) "Payment successful" (5) "Delivery committed: restaurant, before 19:00". The pin becomes solid, 300 m from the restaurant. [S11]
- Touch twin: Yes, order or No thanks on the suggestion. [S10]

**Scene 5: The plan appears (17:24)** [S12]

- No speech. The "Going home" route is replaced by the full plan: work already done, school next, pharmacy 2 at 18:10, wife, dinner, spare time +5 min. The car never stops moving.

**Scene 6: Pickups, screen only** [S13, S14]

- Before each stop the screen says what the car is about to do: "Stopping at School in 1 min. Doors unlock on the right." [S13]
- "Son on board", then "Arriving at kindergarten, 17:55", "Daughter on board", "Arriving at pharmacy, 18:10", "Prescription collected". Maya says nothing. [S14]
- Branch: Michael can also reorder stops by hand, for example picking up his wife before the pharmacy; Edit plan shows the ripple before he applies it. [S15]

**Scene 7: The wife's call (18:03), ambient intent** [S16, S17]

- Screen: incoming-call overlay. [S16]
- **Wife:** "Change of plan: pick me up at the hair salon, not at home."
- **Michael:** "Sure, we'll be there."
- Maya hears it and changes the pickup with **no spoken line**. A soft chime sounds. Screen: "Heard in your call: Pick me up at the hair salon." The wife's pickup moves to the hair salon at 18:30, home is crossed out, the hair salon is marked new, and spare time stays +5 min. Undo and Dismiss sit on the change. [S17]
- Touch twin: Michael taps Undo, or changes the pickup by hand in Edit plan. [S17, S15]

**Scene 8: The errand (18:32)** [S18, S19]

- Screen: a message from the dry cleaner arrives: "Your suit is ready for collection (order 2231). We're open until 20:00." Maya doesn't read it aloud.
- **Maya:** "Your suit is ready at the dry cleaner. After I drop you at the restaurant, I can collect it on my own and be back for you at 21:30. Shall I?" [S18]
- **Michael:** "Yes, please."
- Screen, with Maya silent: (1) "Calling the dry cleaner..." (2) live transcript: **Maya:** "Hello, I'm Maya, an AI assistant calling for a customer about order 2231. I'd like to pay now and collect it at 19:20 with his car, which will arrive with nobody inside. Could someone hang it in the back? I'll text you a code that opens only the rear right door." **Dry cleaner:** "No problem. It'll be ready at 19:20." **Maya:** "Thank you. Paying now." (3) "Payment successful" (4) "Handover agreed: 19:20, rear right door, on a hanger, code sent" (5) a new row joins the plan after the restaurant: "19:20 Dry cleaner · car alone · back 21:30". Only now is the errand booked: no handoff, no commitment. [S19]
- Touch twin: Yes or No thanks on the suggestion card. [S18]

**Scene 9: Arrival (18:55)** [S20, C1]

- **Maya:** "We're here, five minutes early. I'll collect your suit and be back for you at 21:30."
- Screen: a full-screen arrival report: arrived 18:55 with 5 minutes to spare, then a list of what was done (son, daughter, prescription 18:10, wife at the hair salon 18:30, flowers delivered 18:44), and "Next: courier · dry cleaner 19:20, back for you at 21:30". [S20]
- Then the courier hand-off: "Leaving in courier mode. Please take your belongings." Once everyone is out, the car checks that the cabin is empty and nothing is left behind, then drives off. [C1]

**Scene 10: The courier run (from 18:58), car alone** [C1 to C3]

- 18:58: cabin empty, nothing left behind. The tablet and the strip turn off, and the car leaves. Michael's phone shows the run live, view only: to the dry cleaner, then back at 21:30. [C2]
- 19:20: at the dry cleaner, the car stops and flashes the rear right door. A member of staff types the code; only that door opens. They hang the suit and close the door. The cabin camera checks it: "1 garment bag, rear right". The door locks.
- 19:24: a report on the phone with a photo, the receipt and the times. A notification, no voice. [C3]
- The car drives to a charging station near the restaurant and charges. Charging is not an errand, so it isn't in the plan. The story ends here, with the car ready to be back for the family at 21:30.
- Errands can also be scheduled by hand: the box icon beside Settings opens Errands and a New errand form. [C4, C5]

## Conversation design rules

1. **Ask only what she can't know, as many times as needed.** Here that is two questions and one suggestion.
2. **Speak only when she needs Michael:** a question, the result of something he asked, or when the car leaves. Everything else is on screen.
3. **The screen is the confirmation.** The "New plan" card replaces reading back.
4. **Changes caused by the world happen silently and visibly.** Changes caused by conversation get a chime, the heard phrase, and Undo.
5. **Calls to staff are screen-only and transparent:** live transcript, always opening with "Hello, I'm Maya, an AI assistant calling...".
6. **Every voice action has a touch twin** (chips, pickers, drag).
7. **Maya's voice:** calm, competent, short, female. She says "we" for the trip.
8. **Medication names stay off the shared screen:** transcripts say "your prescription" and show the reference number only.
9. **Courier errands are booked only once the handover is agreed.** Maya says once what the car will do and when it will be back; the run itself is followed on the phone.
