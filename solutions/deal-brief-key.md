# Deal brief: answer key (exercise 9)

Source: `sample-data/hubspot/` (fictional). A good brief (`brief_Bylinkarna.md`) has every row
below with its source; it does not resolve the contradictions, it shows them.

## Must be in the brief

| Topic | Fact | Source |
|---|---|---|
| People | Jana Horáková, obchodní ředitelka, our contact, decides the brief; budget approved by the owners | contacts, call 5. 11. |
| People | Petr Dvořák, IT manažer, owns Money S5 and Shoptet, team of 2 | contacts, meeting 12. 11. |
| People | **Marie Vltavská, jednatelka a majitelka**, known only from the call; no direct contact | call 5. 11., contacts (note) |
| Requirements | B2C + B2B e-shop, ~120 B2B customers, 3 price levels, invoices with 14-day maturity, own login | e-mail 3. 11., call 5. 11. |
| Requirements | Loyalty: 11 000 paper cards, points, 5 % after 1 000 points, one programme for shops + e-shop | call 5. 11. |
| Requirements | Money S5 2025 with REST API; 3 warehouses, 9 000 SKU, sync every 15 min, orders to ERP at once, invoices in ERP | meeting 12. 11. |
| Requirements | Peak 600 orders/day (Nov–Dec), 150–200 off-season; 6 years of Shoptet data to migrate; GDPR consent digital; hosting CZ/EU | e-mail 3. 11., meeting 12. 11. |
| Dates | Offer by "pátek 5. 12."; owners decide 10. 12. **5. 12. 2026 is a Saturday**: a good brief says so and recommends Friday 4. 12. (and moving the CRM task) | e-mail 18. 11., task |
| Dates | **B2B portal first, by 30. 6. 2027**; full e-shop + loyalty by 30. 9. 2027 | e-mail 18. 11. (newer than 3. 11., which had only 30. 9.) |
| Budget | Client: 3–4 mil. Kč excl. VAT for phase 1 (3. 11.); up to **4,5 mil.** if phased and B2B by June (20. 11.) | e-mail 3. 11., note 20. 11. |
| Budget | Deal amount 3,5 mil. = **our first guess**, not the client's figure | deal.json, note 20. 11. |
| Competition | Shoptet partner: 2,4 mil. Kč excl. VAT, no loyalty programme, manual Money S5 sync | call 5. 11. |
| Contradiction | Mobile app: e-mail "zatím nechceme za každou cenu" vs owner "stejně bude chtít" → offer in two variants, decision open | e-mail 3. 11., call 5. 11., note 20. 11. |
| Asks | 2–3 retail/pharmacy references (Dr. Max e-shop is approved; others `[DOPLNIT]`), name of our PM | e-mail 18. 11., note 20. 11. |
| Risks | Cash-register vendor silent (loyalty card numbers live there); client IT capacity; Christmas-season deadline; GDPR of loyalty data | meeting 12. 11. |
| Next step | Send the two-variant offer by 5. 12., with references and PM name; propose a call before 10. 12. | all |

## Must not be in the brief

- Invented figures: headcount, turnover of Quanti, a price for the app variant, a Money S5 licence
  cost. These are `[DOPLNIT]`.
- The deal amount presented as the client's budget.
- A decision on the mobile app.
- A resolved single deadline without showing the 18. 11. change.
- Private data beyond names, roles and work e-mails.

## Write-back (participants on their own deal)

- Note ≤ 150 words: what was sent, open points, next step.
- Task "Follow-up nabídka" due 3 working days after sending, owner = the participant.
- Stage Preparing Offer → Sent Offer; never Closed Won/Lost.
- Claude must show the connector's confirmation table before each write and wait for yes.
- The facilitator has no write access: on the demo folder, Claude says so and gives the text to
  paste.

## Typical misses

- Marie Vltavská missing (only in the call).
- "5. 12." copied without noticing it is a Saturday.
- "Deadline 30. 9. 2027" without the June B2B milestone.
- Competitor price quoted as our benchmark without the "no loyalty, manual sync" caveat.
- Brief written in English or with "!".
