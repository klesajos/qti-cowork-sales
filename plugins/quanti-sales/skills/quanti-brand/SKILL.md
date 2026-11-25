---
name: quanti-brand
description: Quanti visual identity and tone of voice. Use whenever you create or edit anything a Quanti client or partner will see (a presentation, offer, one-pager, email, PPTX, DOCX, PDF or HTML page) or when someone asks for "Quanti brand", "naše barvy", "v našem stylu" or "on-brand".
---

# Quanti brand

Apply this on top of the file skills (pptx, docx, pdf): those handle the file mechanics, this
skill decides how the result looks and sounds. The values come from `assets/tokens.json`; read it
when you need an exact number.

## Colours

| Token | Hex | Use |
|---|---|---|
| magenta | `#DF2686` | The one accent: key number, highlight, call to action. At most one magenta element per slide or page section. |
| purple | `#4D1254` | Dark surfaces: title slide, section dividers, cover page, footer band. |
| black | `#151515` | Text on light backgrounds. Never pure `#000000`. |
| lavender | `#F3F0F6` | Cards, tables, callouts on light backgrounds. |
| off-white | `#FAFAFA` | Slide and page background. |
| line | `#E6E6E6` | Hairlines and table borders. |
| white | `#FFFFFF` | Text on purple or magenta. |

No other colours: no blue, no green, no gradients, no stock palette from a template. Charts use
purple, magenta, then black at 60 % and lavender; label the series directly.

## Type

- **Montserrat** for everything, fallback Arial. Never Calibri, Times or the Office default.
- Headings: weight 500, **UPPERCASE**, tight letter spacing (−1 %), line height 1.1.
- Body: weight 400, sentence case, line height 1.5. Slides: body 18–24 pt, headings 32–44 pt.
- One heading per slide, at most 6 words. A slide says one thing.
- In PPTX and DOCX the font name is exactly `Montserrat`. Never `Montserrat Medium` or
  `Montserrat SemiBold`: on many machines those names do not resolve and fall back to a serif.
  Headings use `Montserrat` regular (uppercase carries the weight) or bold.
- DOCX: set `Montserrat` on every style you use, including Title and Heading 1–3, and remove
  their theme-font links (`asciiTheme`/`hAnsiTheme`); otherwise headings inherit the Office
  theme font. PPTX: set the theme's major and minor Latin fonts to `Montserrat` as well.

## Shapes and layout

- Rounded corners, large radius (16–40 px; in PPTX use a rounded rectangle with a visible but
  soft corner). No sharp boxes, no drop shadows, no clip art.
- Generous white space; align to a left edge; at most 3 cards in a row.
- 16:9 slides. Slide 1 and section dividers on purple with the white logo; content slides on
  off-white with the colour logo small in a corner.

## Logo

- `assets/quanti-logo.svg|png` on light backgrounds, `assets/quanti-logo-white.svg|png` on purple,
  magenta or photos. PPTX and DOCX take the PNG.
- Minimum width 120 px. Clear space on every side equal to the height of the hexagon mark.
- Never recolour, stretch, rotate, outline or put the colour logo on purple.

## Tone of voice (Czech by default)

- Talk to the reader as **vy**, directly. Short sentences. Active verbs in the first person
  plural: "Navrhneme. Postavíme. Ohlídáme."
- Partner, not vendor: start from the client's goal, not from our capabilities.
  "Návrh neodvozujeme od aktuálního stavu, ale od vašeho cíle."
- Concrete over grand: name the platform, the number, the deadline. No "inovativní",
  "komplexní řešení na klíč", "synergie", "world-class".
- Confident without superlatives; no exclamation marks in client documents.
- English documents follow the same rules: plain, direct, "we" and "you".

## Claims

Use a number, client name or certification only if it appears in the material you were given
for this task or in `../quanti-offer/references/approved-claims.md`. If a claim you want is not
there, write `[DOPLNIT: …]` and list it at the end for the salesperson to confirm. Never invent
references, figures or certificates.

## Before you hand over

Check the result against this list and fix it, then say what you checked:

1. Only the colours above; one magenta accent per slide or section.
2. Montserrat everywhere, headings uppercase: list the font names actually in the file
   (theme, styles, runs) with code; the only Latin font is `Montserrat`.
3. Correct logo variant for the background, not distorted.
4. Every claim is sourced or marked `[DOPLNIT]`.
5. Text reads as Quanti: vy, short, concrete.
