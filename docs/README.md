> 🌍 Read this in: **English** | [Česky](README.cs.md)

# Workshop docs

| # | Guide | In short |
|---|---|---|
| 01 | [Setup](01-setup.md) | Cowork, the plugin, the working folder |
| 02 | [Brand](02-brand.md) | Tone of voice from texts, a design system from assets, the `quanti-brand` skill |
| 03 | [Presentations](03-decks.md) | A deck from a brief; review and fix an off-brand deck |
| 04 | [Offers](04-offers.md) | Brief + rate card → priced DOCX, without invented numbers |
| 05 | [Tenders](05-tenders.md) | Requirements matrix, clarifications, go/no-go, checking a draft bid |
| 06 | [Your own skill](06-own-skill.md) | Turn a repeated task into a skill; roll it out to the team |
| 07 | [HubSpot](07-hubspot.md) | A sales brief from a deal through the HubSpot connector; the offer logged back |

- [Exercises](exercises.md): prompts and "Done when" for every exercise.
- [Cheat sheet](cheatsheet.md): one page to keep open.

## How the pieces fit

```
You ── prompt ──▶ Claude (Cowork session, working folder on your Mac)
                    │
                    ├─ skill quanti-brand   ← loaded when the output is client-facing
                    ├─ skill quanti-offer   ← "nabídka", "kalkulace"
                    ├─ skill deck-review    ← "zkontroluj prezentaci"
                    ├─ skill tender-check   ← "zadávací dokumentace", "go/no-go"
                    ├─ skill deal-brief     ← "podklady k dealu", "zapiš do HubSpotu" (HubSpot connector)
                    └─ built-in file skills (pptx, docx, xlsx, pdf) write the files
```

A **skill** is a folder with a `SKILL.md`: a description (when to use it) and instructions
(how). Claude reads only the descriptions up front and loads the full instructions when a
request matches. A **plugin** bundles skills so the whole team gets the same ones.
