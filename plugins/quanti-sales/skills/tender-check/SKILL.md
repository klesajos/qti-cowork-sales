---
name: tender-check
description: Check the requirements of a Czech public tender (veřejná zakázka, výběrové řízení, zadávací dokumentace, NEN, ZZVZ, OP TAK) and a draft bid against them. Use when someone shares tender documents, asks "co musíme splnit", "go/no-go", "kontrola nabídky" or "požadavky výběrového řízení".
---

# Tender check

Work only from the documents provided. A requirement without a source in them does not exist;
general knowledge of ZZVZ goes in a separate, labelled section.

## 1. Inventory

List every document with its date and type: zadávací dokumentace (ZD), přílohy, vysvětlení /
změny zadávacích podmínek, updated annexes ("aktualizovaná"). Order them by date. **A later
clarification or updated annex overrides the earlier text.** Say which version of each annex is
current.

## 2. Requirements matrix

Produce an XLSX (and a short markdown preview in the chat) with one row per requirement:

| ID | Kategorie | Požadavek | Zdroj (dokument, článek, strana) | Změněno (vysvětlení č., co) | Doklad v nabídce | Splníme? | Poznámka |

Categories: Lhůty a podání, Kvalifikace (základní, profesní, technická), Hodnocení, Cena,
Smlouva a obchodní podmínky, Technické zadání, Formální náležitosti.

Rules:

- Quote the key wording in Czech; keep amounts, dates, percentages and counts exact.
- One requirement per row; split "a" lists.
- Flag **traps** in Poznámka: requirements that change between documents, unusual submission
  form (paper, envelope marking, copies), price consistency rules, mandatory forms, things that
  exclude the bid rather than lower the score.
- The "Splníme?" column stays empty unless you were given company facts; then use Ano / Ne /
  Ověřit, with the reason.

## 3. Evaluation

Explain the scoring: criteria, weights, formula, and what earns points. Show with a small
example how price and quality trade off.

## 4. Go / no-go

Summarise in at most 10 lines: deadline (current one), knock-out requirements, effort to
prepare, the biggest risks in the contract (penalties, retention, liability, IP), and questions
to send to the contracting authority before the clarification deadline. Mark your opinion as
opinion.

## 5. Checking a draft bid

When given a draft bid, go through the matrix row by row and report per row: OK / Chybí /
Nesoulad, with where in the draft. Check especially: the current deadline and annex versions,
the same price everywhere (form, contract, price table), every mandatory form and signature,
the team roles and documents per role, formal marking of the submission. List blocking issues
first.
