# Dry run, 2026-11-25

**What was run.** Exercises 3–7, with the exact prompts from [exercises.cs.md](../exercises.cs.md),
each in a fresh copy of `sample-data/`. The runs used `claude -p` (Claude Code 2.1.311), with the
plugin loaded from `plugins/quanti-sales` (`--plugin-dir`); the model chose the skills itself.
This tests the plugin, the prompts and the outputs; it does **not** show the Cowork window. The
screenshots are of the produced files (rendered with macOS Quick Look and Montserrat installed)
and of each run's prompt and final answer.

Exercises 3–5 were run three times: with brand rules derived from quanti.cz, after a font fix,
and finally against the **QUANTI Brand manuál 2024**. The screenshots show the final run.

**Not run here:** exercises 0, 1, 2 and 8. They need the Claude app UI (plugin upload, design
systems). Cowork UI screenshots for them are still to be added.

**Differences from Cowork.** The CLI answered in English, and put the tester's name on closing
slides, because of personal instructions on the test machine; in Cowork the answer follows the
prompt language and uses the participant's details. In the CLI runs Claude could not render its
own PPTX/DOCX output (no LibreOffice); Cowork's sandbox can.

Cost: 10 runs, US$ 16.58 in total (US$ 0.8–3.6 per run), 1.5–6.5 min each.

## Brand template

`quanti-brand` ships `quanti_slides.py` and [quanti-template.pptx](../../plugins/quanti-sales/skills/quanti-brand/assets/quanti-template.pptx),
built after the manual's PowerPoint template (pp. 49–51): title, chapter divider, content with
cut-corner cards, closing ([screenshot](brand-template.png)).

## Results

| Exercise | Result | Screenshots |
|---|---|---|
| 3 · deck from a brief | passes: 6 slides on the manual's template, pink/purple and tints only, Montserrat only, bold sentence-case headings, logo bottom-right, brief quoted, approved claims, closing slide with next step and claim | [deck](ex3-01-deck.png) · [run](ex3-02-run.png) · [first run: font fallback](ex3-00-run1-font-fallback.png) |
| 4 · deck review | passes: every row of the [key](../../solutions/deck-review-key.md) (claims, logo, colours, fonts, basic shape, tone, structure); Dr.Max/BAT/ProEx kept; rebuilt with the brand helpers | [before](ex4-01-before.png) · [run](ex4-02-run.png) · [after](ex4-03-after.png) |
| 5 · priced offer | passes: all 9 sections, MD × rate per role, PM 12 %, QA 15 %, reserve 10 %, VAT; licences `[DOPLNIT]`; three costed budget cuts; purple cover with the pink panel | [cover](ex5-00-cover.png) · [offer](ex5-01-offer.png) · [price](ex5-02-price.png) · [run](ex5-03-run.png) |
| 6 · tender matrix | passes: 83 rows with sources, every "Done when" item, document inventory, scoring example, conditional go/no-go | [matrix](ex6-01-matrix.png) · [run](ex6-02-run.png) |
| 7 · draft bid check | passes: all 9 blocking errors, plus E11–E15 from the key; ISO 9001 and 30. 6. 2027 correctly OK | [matrix](ex7-01-matrix.png) · [run](ex7-02-run.png) |

The offer arithmetic was checked by hand in all three runs: 460 MD / 6,696,250 Kč, 557.5 MD /
8,064,750 Kč and 386 MD / 5,606,000 Kč excl. VAT. Every line is MD × rate, the PM, QA and
reserve rules hold, and the VAT is exact.

The offer's cover is a full-page background in its own section. Quick Look's preview cannot
place it, so in [offer](ex5-01-offer.png) the cover looks faded and overlaps the summary; the
background itself is in [cover](ex5-00-cover.png). Open the DOCX in Word to see the real page.

## Fixed after the runs

- **Brand manual.** Rules first came from quanti.cz (uppercase headings, rounded cards, black
  `#151515`). `quanti-brand`, `tokens.json`, `brand-brief.md` and the deck-review key now follow
  the manual: Montserrat Bold sentence-case headings, the cut-corner basic shape, logo always
  bottom-right, black `#040505`, secondary colours only for special occasions, Arial as the
  system font, the claim and vision.
- **Fonts.** The first run set headings in "Montserrat Medium", and the offer's Word heading
  styles kept the theme font; both fell back to a serif ([screenshot](ex3-00-run1-font-fallback.png)).
  The skill now requires the font name `Montserrat` exactly, set on the theme, the styles and the
  runs, and checks the fonts found in the file.
- **Font files.** The variable `Montserrat.ttf` rendered headings at weight 100 in Quick Look.
  It was replaced by the static Regular, Medium, SemiBold and Bold files.

## Still open

1. **The estimate varies.** The same prompt priced the offer at 386, 460 and 557.5 MD; the
   arithmetic is right every time, but the effort per deliverable is a judgement. In the room,
   compare the MD tables, not the totals ([prep](../prep.md) lists this trap).
2. **Penalty wording.** Exercise 7 summarised penalties as "0.1 % per day". That rate applies only
   to the final deadline; milestones are 2,000 Kč/day ([answer key](../../solutions/tender-answer-key.md), SoD čl. 7).
3. **Exercise 4** did not add the missing client-problem slide, only named it, because the skill
   says to keep the content and order. That is intended.
4. **Logo variants.** Horizontal, square, symbol and icon are in the repo as PNG (white square
   and symbol versions generated from the colour files); the vertical logo and SVGs of the new
   variants are still missing.
5. **Exercises 0, 1, 2 and 8** need a run in the Claude app, with screenshots.
