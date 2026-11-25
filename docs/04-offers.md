> 🌍 Read this in: **English** | [Česky](04-offers.cs.md)

# 04 · Offers

An offer is where a wrong number costs real money. The `quanti-offer` skill is built around
that:

1. **Inputs first.** Claude lists what it has (brief, rate card, your notes) and stops if the
   rate card is missing. It never guesses day rates.
2. **Estimate before price.** Man-days per role and phase, with assumptions, then the price.
3. **Arithmetic in code.** MD × rate, the rules from the rate card (PM and QA percentages, risk
   reserve), VAT: computed with Python, not "in the head" of the model.
4. **Claims only from sources.** References and numbers from the brief or `approved-claims.md`;
   everything else becomes `[DOPLNIT: …]`.
5. **Brand.** `quanti-brand` shapes the DOCX and the wording.
6. **Hand-over report.** Total and how it was computed, open `[DOPLNIT]`s, price-changing
   assumptions, parts of the brief not answered.

## Your job in the loop

Claude drafts; you own the offer. Before anything goes to a client:

- Recompute one line of the price table yourself.
- Read every `[DOPLNIT]` and fill it or delete the sentence.
- Check the scope boundary ("what is not included"): this is where disputes start.
- Check the dates against the client's deadline.

## Rate card

`sample-data/offer/rate-card.xlsx` is **fictional**. In real use, keep the real rate card in one
place the whole team reads (a Drive or SharePoint file through a connector, or inside the
plugin), so nobody pastes an old version into a conversation.
