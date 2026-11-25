> 🌍 Read this in: **English** | [Česky](07-hubspot.cs.md)

# 07 · HubSpot: from a deal to an offer and back

Quanti's CRM is HubSpot. In Claude the **HubSpot connector** (Plugins → HubSpot → Connect, with
your own HubSpot login) lets Claude read companies, contacts, deals and every logged activity, and
write notes, tasks and stage changes after you confirm each one. The `deal-brief` skill turns that
into a sales workflow.

## What the skill does

1. **Collect**: the deal, its company and contacts, and all activities oldest first (e-mails,
   calls, meetings, notes, tasks). Full texts, not summaries.
2. **Brief**: one page in Czech: client in short, people and roles, timeline, requirements with
   sources, dates (newer source wins, both shown), budget vs our estimate, competition,
   contradictions, risks, next step. Gaps are `[DOPLNIT]`, never guessed.
3. **Hand over** to `quanti-offer` (the offer) or `quanti-brand` (the deck).
4. **Log back**: a note, a follow-up task and the stage move, each behind the connector's
   confirmation table. Never Closed Won/Lost, never e-mails from HubSpot.

## Two ways to run it

| | Facilitator demo | Participants |
|---|---|---|
| Data | `sample-data/hubspot/`: an export of the fictional deal Bylinkárna Vltava, in the connector's shape | Their own open deal through the connector |
| Prompt | "…ve složce hubspot/" | "…v HubSpotu" |
| Write-back | Not possible (no write rights): Claude gives the note text to paste | Real, with confirmation |
| Answer key | `solutions/deal-brief-key.md` | None; compare with what you know about the deal |

## What to watch

- **Sources on every fact.** A brief without "(e-mail 18. 11.)" after a date is a guess.
- **Newer beats older.** The export has two deadline e-mails; the brief must show both and
  use the later one.
- **Client's words vs our notes.** The deal amount in HubSpot is usually the salesperson's first
  guess; the brief must say so.
- **Confirmation before writing.** Claude shows a table (object, property, old value, new
  value). Read it; a wrong stage move is visible to the whole team.
- **Personal data.** Names, roles and work e-mails only. Private notes about people stay in CRM.

## Prerequisites

- HubSpot connector connected in Claude (participants: the day before, see [prep](prep.md)).
- HubSpot rights to edit deals for the write-back part. Without them, the read part still works.
- A deal of your own with at least one logged e-mail or call. If you have none, pick a colleague's
  deal for the read part only and skip the write-back.
