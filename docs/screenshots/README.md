# Dry run, 2026-11-25

**What was run.** Exercises 3–7, with the exact prompts from [exercises.cs.md](../exercises.cs.md),
each in a fresh copy of `sample-data/`. The runs used `claude -p` (Claude Code 2.1.311), with the
plugin loaded from `plugins/quanti-sales` (`--plugin-dir`); the model chose the skills itself.
This tests the plugin, the prompts and the outputs; it does **not** show the Cowork window. The
screenshots are of the produced files (rendered with macOS Quick Look and Montserrat installed)
and of each run's prompt and final answer.

**Not run here:** exercises 0, 1, 2 and 8. They need the Claude app UI (plugin upload, design
systems). Cowork UI screenshots for them are still to be added.

**Differences from Cowork.** The CLI answered in English because of a personal instruction on the
test machine; in Cowork the answer follows the prompt language. Package installs were not
allowed in the CLI run, so Claude sometimes wrote PPTX/XLSX with the Python standard library and
could not render its own output; Cowork's sandbox has python-pptx, openpyxl and a renderer.

Cost: 7 runs, US$ 12.92 in total (US$ 1.0–3.6 per run), 2–6.5 min each.

## Results

| Exercise | Result | Screenshots |
|---|---|---|
| 3 · deck from a brief | passes on the second run: 6 slides, palette only, Montserrat only, brief quoted, approved claims, one call to action | [deck](ex3-01-deck.png) · [run](ex3-02-run.png) · [first run: font fallback](ex3-00-run1-font-fallback.png) |
| 4 · deck review | passes: every row of the [key](../../solutions/deck-review-key.md) (claims, logo, colours, fonts, shapes, tone, structure); Dr.Max/BAT/ProEx kept | [before](ex4-01-before.png) · [run](ex4-02-run.png) · [after](ex4-03-after.png) |
| 5 · priced offer | passes: all 9 sections, MD × rate per role, PM 12 %, QA 15 %, reserve 10 %, VAT; licences `[DOPLNIT]`; two budget options | [offer](ex5-01-offer.png) · [price](ex5-02-price.png) · [run](ex5-03-run.png) |
| 6 · tender matrix | passes: 83 rows with sources, every "Done when" item, document inventory, scoring example, conditional go/no-go | [matrix](ex6-01-matrix.png) · [run](ex6-02-run.png) |
| 7 · draft bid check | passes: all 9 blocking errors, plus E11–E15 from the key; ISO 9001 and 30. 6. 2027 correctly OK | [matrix](ex7-01-matrix.png) · [run](ex7-02-run.png) |

The arithmetic in both offer runs was checked by hand: run 1 is 460 MD, 6,696,250 Kč excl. VAT;
run 2 is 557.5 MD, 8,064,750 Kč excl. VAT. Every line is MD × rate and the VAT is exact.

## Fixed after this run

- **Fonts.** Run 1 of exercise 3 set headings in "Montserrat Medium", and the offer's Word
  heading styles kept the theme font. Both fell back to a serif ([screenshot](ex3-00-run1-font-fallback.png)).
  `quanti-brand` now requires the font name `Montserrat` exactly and has Claude set it on the theme,
  the styles and the runs, then list the fonts found as a final check. Run 2 used only `Montserrat`.
- **Font files.** The variable `Montserrat.ttf` rendered headings at weight 100 in Quick Look.
  It was replaced by the static Regular, Medium, SemiBold and Bold files.

## Still open

1. **The estimate varies.** The same prompt priced the offer at 460 MD and at 557.5 MD; the
   arithmetic is right both times, but the effort per deliverable is a judgement. In the room,
   compare the MD tables, not the totals ([prep](../prep.md) lists this trap).
2. **Penalty wording.** Exercise 7 summarised penalties as "0.1 % per day". That rate applies only
   to the final deadline; milestones are 2,000 Kč/day ([answer key](../../solutions/tender-answer-key.md) R-rows on SoD čl. 7).
3. **Exercise 4** did not flag the missing client-problem slide as an error to fix, only in the
   structure notes, because the skill says to keep the content and order. That is intended.
4. **Exercises 0, 1, 2 and 8** need a run in the Claude app, with screenshots.
