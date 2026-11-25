> 🌍 Read this in: **English** | [Česky](05-tenders.cs.md)

# 05 · Public tenders

The exercise tender is real and public: T.S.BOHEMIA a.s., *Technická modernizace a optimalizace
webové aplikace tsbohemia.cz* ([NEN N006/26/V00032057](https://nen.nipez.cz/verejne-zakazky/detail-zakazky/N006-26-V00032057)).
It is an OP TAK grant procurement, explicitly **not** under ZZVZ, but it borrows ZZVZ
qualification rules. `sample-data/tender/` holds all ten documents published on NEN.

## Why it is a good exercise

The requirements change over time. A bidder who reads only the main document gets several
things wrong:

| Main document says | Later documents say |
|---|---|
| Deadline 2. 11. 2026 | 20. 11. (clarification 1), then **27. 11. 2026 10:00** (clarification 2) |
| "at least 1 reference" | **3 references**, each e-commerce, ≥ 4 M Kč excl. VAT, last 5 years (clarification 1, Ad 5) |
| Contract and team annex of 22. 9. | **Updated** annexes of 19. 10.: liability cap 8 M Kč, licence split |
| Core Web Vitals "measure before and after" | Targets are an **acceptance condition** on CrUX field data, third parties included (clarification 1, Ad 3) |

And some rules are unusual for a digital agency: **paper submission** in a sealed envelope with
the tender name and "NEOTEVÍRAT", the contract in 3 copies (2 removable), ISO 9001 **and**
ISO 27001 valid on the submission date, and "if the price in the form and the contract
differ, the lower one counts".

## How `tender-check` works

1. **Inventory**: every document, its date, which version of each annex is current. Later
   overrides earlier.
2. **Matrix** (XLSX): one requirement per row, with source (document, article, page), what
   changed it, the evidence needed in the bid, and traps.
3. **Evaluation**: criteria, weights and formula, with a worked example. Here: price 70 %,
   team expertise 30 % (5 roles, points for references and technologies).
4. **Go / no-go**: knock-outs, effort, contract risks (10 % retention until the last defect,
   penalties, no acceptance deadline), questions to send before the clarification cut-off.
5. **Draft-bid check**: row by row, OK / Chybí / Nesoulad, blocking issues first.

## What stays your job

- Check the knock-outs against facts only you know: certificates, references, people.
- Read the contract risks with someone who signs contracts.
- Re-check NEN on the day you submit; a new clarification can arrive an hour before the deadline
  (it happened here).
