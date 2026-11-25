> 🌍 Read this in: **English** | [Česky](README.cs.md)

# Quanti sales × Claude Cowork

A half-day (4 h) hands-on workshop for the Quanti sales team. By the end, everyone can:

1. **Keep the brand**: Claude knows Quanti's colours, type, logo and tone of voice and applies
   them to every output.
2. **Make presentations**: a client deck in PPTX from a brief, and a review of an off-brand one.
3. **Write offers**: a priced offer in DOCX from a client email and the rate card, with no
   invented numbers.
4. **Check tender requirements**: a requirements matrix from a real Czech public tender, a
   go/no-go, and a check of a draft bid.

Everything runs in Claude (Cowork) with one plugin, `quanti-sales`, that holds the brand and
the three workflows as skills.

## What's in the repo

| Path | What it is |
|---|---|
| [`docs/`](docs/README.md) | Guides, exercises, prep, facilitator notes (CS + EN) |
| [`plugins/quanti-sales/`](plugins/quanti-sales) | The plugin: skills `quanti-brand`, `quanti-offer`, `deck-review`, `tender-check` |
| [`dist/quanti-sales.zip`](dist/quanti-sales.zip) | The plugin ready to upload in Claude |
| [`sample-data/`](sample-data) | Brand assets, tone corpus, a fictional client brief and rate card, an off-brand deck, a real NEN tender |
| [`solutions/`](solutions) | Answer keys for the facilitator |
| [`scripts/`](scripts) | `build-plugin.sh` (zip the plugin), sample-data generators |

## Agenda (4 h)

| Time | Block | Exercises |
|---|---|---|
| 0:00 | Intro, setup | 0 |
| 0:20 | Brand: voice and design system | 1, 2 |
| 1:00 | Presentations | 3, 4 |
| 1:45 | *Break* | |
| 2:00 | Offers | 5 |
| 2:40 | Tenders | 6, 7 |
| 3:35 | Your own workflow as a skill, wrap-up | 8 |

Start with [docs/README.md](docs/README.md). Facilitators: [docs/prep.md](docs/prep.md) first.

## Data and sources

- Brand values come from the QUANTI Brand manuál 2024 (`sample-data/brand/`); the logo files
  are from quanti.cz. Montserrat is under the SIL Open Font License (`sample-data/brand/fonts/OFL.txt`).
- The tone corpus is public quanti.cz text (blog, references, services), staff contacts removed.
- The client "Bylinkárna Vltava" and the rate card are **fictional**.
- The tender is public: T.S.BOHEMIA a.s., *Technická modernizace a optimalizace webové aplikace
  tsbohemia.cz*, [NEN N006/26/V00032057](https://nen.nipez.cz/verejne-zakazky/detail-zakazky/N006-26-V00032057).
