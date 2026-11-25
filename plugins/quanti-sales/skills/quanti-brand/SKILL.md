---
name: quanti-brand
description: Quanti visual identity and tone of voice from the Quanti brand manual. Use whenever you create or edit anything a Quanti client or partner will see (a presentation, offer, one-pager, email, PPTX, DOCX, PDF or HTML page) or when someone asks for "Quanti brand", "naše barvy", "v našem stylu" or "on-brand".
---

# Quanti brand

Source: QUANTI Brand manuál 2024. Exact values are in `assets/tokens.json`. Apply this on top
of the file skills (pptx, docx, pdf): those handle the file mechanics, this skill decides how
the result looks and sounds.

## Colours

| Colour | Hex | Use |
|---|---|---|
| Pink | `#DF2686` | Primary. The signature panel, the one highlight per slide or section. |
| Purple | `#4D1254` | Primary. Backgrounds of title, divider and closing slides; headings on white. |
| Black | `#040505` | Body text on white. |
| White | `#FFFFFF` | Backgrounds of content slides; **all small text on pink or purple**. |

- The basic combination is **PINK/PURPLE** (pink panel on purple, or purple on pink).
- Tints 100–20 % of any colour are allowed (purple 20 % `#DBD0DD`, pink 20 % `#F9D4E7` for
  cards and table headers).
- Secondary colours (green `#A1C854`, blue `#74C9E3`, dark blue `#43358B`, orange `#F18C78`,
  yellow `#FDC643`, grey `#CAC8C1`) are for special occasions only, not for regular client
  materials. Use them only when asked, and then only in the manual's combinations with
  enough contrast.
- Nothing else: no other blues, greens or oranges, no gradients, no template palettes.
- Charts: purple, pink, then their tints; label series directly.

## Type

- **Montserrat** for client materials; **Arial** is the system font (e-mail, documents that
  will be opened where Montserrat is missing).
- Headings: **Montserrat Bold, sentence case** ("Název prezentace", not "NÁZEV PREZENTACE").
  Subtitles Bold or SemiBold, smaller. Body Regular.
- Slides: title 40–48 pt, slide headings 28–32 pt, body 18–22 pt. One message per slide,
  heading at most 6 words.
- In PPTX and DOCX the font name is exactly `Montserrat` (with bold on) or `Arial`. Never
  `Montserrat Bold` or `Montserrat Medium` as a font name: on many machines those names fall
  back to a serif.
- DOCX: set the font on every style you use, including Title and Heading 1–3, and remove their
  theme-font links (`asciiTheme`/`hAnsiTheme`). PPTX: set the theme's major and minor Latin
  fonts too.

## The basic shape and layout

- The signature element is the **základní tvar**: a panel with the top-right and bottom-left
  corners cut on the diagonal, echoing the hexagon of the logo. Cards use the same shape with
  only the top-right corner cut. No rounded "app" cards, no shadows, no clip art.
- **The logo is always in the bottom-right corner.**
- Margins: A = the shorter side; outer margin A/25, text inset A/15.
- DOCX: cover page in purple with a pink panel and the white logo; headings purple Bold;
  tables with a purple header row (white text) and pink 20 % or purple 20 % zebra rows.

## Presentations: build on the official template

Every PPTX starts from the official PowerPoint template, never from a blank deck:

- `assets/quanti-template-cz.potx`: Czech labels; the English twin is
  `brand/templates/Quanti_PPT_Template_ENG.potx` in the workshop folder. 26 layouts and 46 sample
  slides (charts, Gantt charts, timelines, organisation diagrams, tables, icons), all in the brand
  colours. `references/template-guide.md` lists every layout and sample slide.
- `decks/Quanti_intro_2026_CZ.pptx` in the workshop folder: the approved company story (facts,
  services, technologies, certifications, 30 references, offices). `references/intro-deck.md`
  indexes it. Company slides are **copied** from it, not rewritten.

Workflow (pptx skill, section "Editing existing decks and templates"):

1. Copy the `.potx` to `<name>.pptx`. Read `template-guide.md` (and `thumbnail.py` once if you
   need to see a slide) and map each section of the deck to a layout or a sample slide.
2. Unpack. `add_slide.py` the layouts and sample slides you need: duplicate a sample slide for a
   chart, timeline, phases or table, it keeps the brand colours. Delete the template's
   instruction slides (2–5, 7, 28, 40) and every unused sample slide; run `clean.py`.
3. Edit the slide XML: one `<a:p>` per list item, keep the placeholders' run properties (that is
   how Montserrat and the sizes arrive). Replace every sample text and chart value, then
   `slide_text.py | grep` for leftovers ("Text", "Insert text", "Lorem").
4. „Kdo jsme“, „Co umíme“, references and „Kontakt“ come from the intro deck: take 3–5 reference
   slides that fit the client's industry. Facts in your own words only from
   `../quanti-offer/references/approved-claims.md`.
5. `validate.py --original <template>`, render, and look at every slide: overflow, leftover
   sample shapes, the logo on every slide.

The sales deck for a first meeting, in this order unless asked otherwise: Intro (client, topic,
date) → the client's situation in their words → what we propose → how we would do it (a
phases or timeline sample slide) → why Quanti (intro-deck slides) → next step → Outro with the
salesperson's contact. One message per slide, at most 3 cards in a row, charts in purple, pink
and their tints only.

## Logo

Official logo files (`assets/`, SVG and PNG; print CMYK PDFs are in the workshop repo):

| Files | Variants | Use |
|---|---|---|
| `quanti-logo[-black\|-pink\|-white]` | horizontal, with ® | The default: bottom-right on slides and documents |
| `quanti-logo-square[-black\|-pink\|-white]` | square (stacked) | Covers, square formats, social posts |
| `quanti-symbol[-black\|-white]` | symbol alone | Small spaces, or where the name is already on the page |
| `quanti-icon-1…5-<colours>` | app icon (symbol in a rounded square) | Avatars, favicons, app tiles only |

- Default is the colour version (pink symbol, black wordmark) on white or light tints, and the
  **white** version on pink, purple or photos. Black and all-pink versions only where colour
  printing or contrast requires it.
- PPTX and DOCX take the PNG; HTML takes the SVG.
- Keep the original proportions; the safe zone is built into the files.
- Never change the shape or colour, rearrange symbol and wordmark, rotate, slant or outline it.

## Tone of voice (Czech by default)

- Claim: **„Technologická řešení, která hýbou světem."** (EN: "World-moving tech solutions.")
  Use it on title or closing slides and covers, not in every paragraph.
- Vision: „Jsme spolehlivý technologický partner pro digitální evoluci." Write as that partner:
  start from the client's goal, not from our capabilities.
- Talk to the reader as **vy**, directly. Short sentences. Active verbs in the first person
  plural: "Navrhneme. Postavíme. Ohlídáme."
- Concrete over grand: name the platform, the number, the deadline. No "inovativní",
  "komplexní řešení na klíč", "synergie", "world-class". No exclamation marks in client documents.

## Claims

Use a number, client name or certificate only if it appears in the material you were given for
this task or in `../quanti-offer/references/approved-claims.md`. Otherwise write
`[DOPLNIT: …]` and list it at the end for the salesperson to confirm. Never invent references,
figures or certificates.

## Before you hand over

Check the result with code where you can, fix it, then say what you checked:

1. Colours used are only primary colours and their tints (secondary only if asked).
2. Fonts found in the file (theme, styles, runs): only `Montserrat` (or `Arial`); headings bold,
   sentence case.
3. PPTX: built on the official template (Quanti Theme layouts), no leftover sample text or shapes;
   the basic shape is used; the logo is bottom-right, correct variant, not distorted.
4. Every claim is sourced or marked `[DOPLNIT]`.
5. Text reads as Quanti: vy, short, concrete, no exclamation marks.
