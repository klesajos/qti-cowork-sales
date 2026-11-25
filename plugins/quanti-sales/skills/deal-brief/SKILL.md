---
name: deal-brief
description: Sales brief from a HubSpot deal (company, contacts, deal, e-mails, calls, meetings, notes, tasks) through the HubSpot connector or from an export folder, and logging the result back (note, task, stage). Use when someone asks for "podklady k dealu", "co víme o klientovi", "příprava na schůzku", "shrň deal z HubSpotu", "call prep", or to "zapsat do HubSpotu" a note, task or stage change.
---

# Deal brief

## 1. Collect

- **HubSpot connector**: find the deal by name or client (`search_crm_objects` on deals; if more
  than one matches, ask). Then read the associated company and contacts, and every activity
  (`search_communications` and the engagement objects: e-mails, calls, meetings, notes, tasks),
  oldest first. Read full texts, not only summaries, before you state a number or a date.
- **Export folder** (e.g. `hubspot/`): read every file; `engagements/` holds one activity per
  file, named by date.
- Never invent CRM data. What is not in the records is `[DOPLNIT]`.

## 2. Write `brief_<klient>.md`

Czech, one page, in this order:

1. **Klient v kostce**: who they are, size, systems, in two or three sentences.
2. **Lidé a role**: who decides, who signs the budget, who owns IT, who is our contact. Mark
   people known only second-hand (e.g. from a call) as such.
3. **Časová osa**: every interaction, date, type, one line each.
4. **Co chtějí**: requirements and numbers, each with its source (type + date).
5. **Termíny**: all dates found; when sources disagree, the **newer source wins**, and you show
   both.
6. **Rozpočet a cena**: the client's words and our own estimates kept apart and labelled
   (a deal amount is usually our guess).
7. **Konkurence**: what we know, with its source.
8. **Rozpory a otevřené otázky**: quote both sides; do not resolve them yourself.
9. **Rizika**: for delivery and for the sale.
10. **Doporučený další krok**: one action, one date, one owner.

Rules: every fact traceable to a record; client's words in quotes; no assumptions filled in;
personal data kept to names, roles and the contact channel actually needed; no copying of private
phone numbers or private notes about people into documents that leave the company.

## 3. Hand over

If the user wants the offer or the deck next, pass the brief to `quanti-offer` or `quanti-brand`
(section "Presentations"); keep the `[DOPLNIT]` list.

## 4. Log back to HubSpot (only when asked)

- **Note** on the deal: at most 150 words, what was sent or agreed, open points, next step.
- **Task**: subject, owner (the current user unless told), due date (three working days after
  the send date unless told), priority.
- **Stage**: only forward along the sales pipeline (e.g. Preparing Offer → Sent Offer). Never
  Closed Won or Closed Lost, never a different pipeline.
- The connector shows a confirmation table before every write; present it and wait for the
  user's yes. Never create companies or contacts, never send e-mails from HubSpot, never change
  amounts or close dates unless the user dictates the value.
- Without write access (the connector reports it), say so and give the user the note text to
  paste.
