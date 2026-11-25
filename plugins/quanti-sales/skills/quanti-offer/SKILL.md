---
name: quanti-offer
description: Write a Quanti commercial offer (nabídka) or proposal from a client brief, call notes or an RFP, priced from the rate card. Use when someone asks for a "nabídka", "cenová nabídka", "proposal", "offer" or "kalkulace" for a client.
---

# Quanti offer

## Inputs

Before writing, collect and list what you have:

- the client brief, email, call notes or RFP;
- the rate card (`rate-card.xlsx` or a table in the brief). Without it, stop and ask; never
  guess day rates;
- anything the salesperson says about scope, timing, discounts or payment terms.

If the goal, the deadline or the budget range is missing, ask once, in one message, before you
write. Otherwise proceed and mark gaps as `[DOPLNIT: …]`.

## Build

1. Follow `references/offer-structure.md` section by section.
2. Estimate in man-days (MD) per role and phase. Show the estimate table and its assumptions
   before the price. Round to half days.
3. Price = MD × rate from the rate card, per role, then totals excl. VAT, VAT 21 %, incl. VAT.
   Calculate with code, not in your head, and show the sums in the table.
4. References and numbers only from the brief or `references/approved-claims.md`.
5. Apply the `quanti-brand` skill to the text and the file.
6. Output a DOCX (or PPTX if asked) named `YYYY-MM-DD_Quanti_nabidka_<klient>.docx`, plus a
   one-paragraph cover email in the chat.

## Before you hand over

Report briefly:

- the price total and how it was computed (MD × rate, rounding);
- every `[DOPLNIT]` left in the document;
- assumptions that change the price;
- any part of the brief the offer does not answer.
