> 🌍 Read this in: **English** | [Česky](03-decks.cs.md)

# 03 · Presentations

Two routes to a deck. Pick by where it goes next:

| Route | Output | Best for |
|---|---|---|
| **Cowork + pptx skill** | A `.pptx` file in your folder | Decks you will edit in PowerPoint, send as a file or reuse as a template |
| **Claude Slides** | A slide artifact; export to PPTX or PDF | Fast visual drafts, live editing with Claude, decks from the published design system |

Both follow the brand: Cowork through the `quanti-brand` skill, Slides through the published
design system.

## A deck from a brief

A good prompt names: the audience, the goal of the meeting, the number of slides, the structure,
the source files, and the file name. Claude then plans the slides, writes them with code
(python-pptx), renders them to check the layout, and fixes what overflows.

The sales structure that works for a first meeting:
1. Title: client, topic, date.
2. Your situation: their problem in their words (quote the brief).
3. What we propose: three outcomes, not technologies.
4. How we'd do it: phases and the one date that matters to them.
5. Why Quanti: two or three relevant references from the approved claims.
6. Next step: one concrete action with a date.

## Reviewing a deck

`deck-review` reads the file itself, not a picture of it: it lists the colours and fonts used in
every shape, so it catches a Calibri title or a `#1F4E9C` fill that looks "almost right". Then
it checks the sales structure. Ask it to fix only after you have read the report; the fix keeps
the content and saves a new `_opraveno` file.

## Typical misses to check yourself

- Text overflowing a box (Claude checks a render, but look anyway).
- Montserrat not installed on the machine that opens the file: PowerPoint falls back to another
  font. Install it from `sample-data/brand/fonts/` or embed fonts when exporting.
- A claim that sounds right but is not in `approved-claims.md`.
