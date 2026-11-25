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
- Slide types follow the manual's PowerPoint template (pp. 49–51):
  1. **Title**: purple background, pink panel, white bold title and subtitle,
     "Software / Hardware / Infrastruktura" bottom-left, white logo bottom-right.
  2. **Chapter divider**: pink panel on purple, purple bold title.
  3. **Content**: white background, purple bold heading, black text, colour logo bottom-right,
     at most 3 cards in a row.
  4. **Closing**: same colours as the title slide, the salesperson's name, role, e-mail, phone.
- For PPTX use `assets/quanti_slides.py` (python-pptx helpers: `new_deck`, `title_slide`,
  `chapter_slide`, `content_slide`, `cards`, `closing_slide`). `assets/quanti-template.pptx`
  shows each slide type. Add your own shapes only in the same style.
- DOCX: cover page in purple with a pink panel and the white logo; headings purple Bold;
  tables with a purple header row (white text) and pink 20 % or purple 20 % zebra rows.

## Logo

- `assets/quanti-logo.svg|png` (pink symbol, black wordmark) on white or light tints;
  `assets/quanti-logo-white.svg|png` on pink, purple or photos. PPTX and DOCX take the PNG.
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
3. The basic shape is used; the logo is bottom-right, correct variant, not distorted.
4. Every claim is sourced or marked `[DOPLNIT]`.
5. Text reads as Quanti: vy, short, concrete, no exclamation marks.
