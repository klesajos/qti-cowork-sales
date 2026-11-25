# Dry run, 2026-11-25

**What was run.** Exercises 3–7, with the exact prompts from [exercises.cs.md](../docs/exercises.cs.md),
each in a fresh copy of `sample-data/`. The runs used `claude -p` (Claude Code 2.1.311), with the
plugin loaded from `plugins/quanti-sales` (`--plugin-dir`); the model chose the skills itself.
This tests the plugin, the prompts and the outputs; it does **not** show the Cowork window. The
screenshots are of the produced files (rendered with macOS Quick Look and Montserrat installed)
and of each run's prompt and final answer.

Exercises 3–5 were run three times: with brand rules derived from quanti.cz, after a font fix,
and finally against the **QUANTI Brand manuál 2024**. The screenshots show the final run.

**Exercises 0, 1, 2 and 8** were run later the same day in the Claude app UI; see
[the second section](#dry-run-in-the-claude-app-2026-11-25) below.

**Differences from Cowork.** The CLI answered in English, and put the tester's name on closing
slides, because of personal instructions on the test machine; in Cowork the answer follows the
prompt language and uses the participant's details. In the CLI runs Claude could not render its
own PPTX/DOCX output (no LibreOffice); Cowork's sandbox can.

Cost: 10 runs, US$ 16.58 in total (US$ 0.8–3.6 per run), 1.5–6.5 min each.

## Brand template

Until 2026-11-25 (plugin 1.2.0) `quanti-brand` shipped its own `quanti_slides.py` helpers and a
hand-made template after the manual's pp. 49–51. Plugin 1.3.0 replaced them with the official
Quanti PowerPoint template (`assets/quanti-template-cz.potx`) and the intro deck; see the third
section below.

## Results

| Exercise | Result | Screenshots |
|---|---|---|
| 3 · deck from a brief | passes: 6 slides on the manual's template, pink/purple and tints only, Montserrat only, bold sentence-case headings, logo bottom-right, brief quoted, approved claims, closing slide with next step and claim | [deck](../docs/screenshots/ex3-01-deck.png) · [run](../docs/screenshots/ex3-02-run.png) · [first run: font fallback](../docs/screenshots/ex3-00-run1-font-fallback.png) |
| 4 · deck review | passes: every row of the [key](../solutions/deck-review-key.md) (claims, logo, colours, fonts, basic shape, tone, structure); Dr.Max/BAT/ProEx kept; rebuilt with the brand helpers | [before](../docs/screenshots/ex4-01-before.png) · [run](../docs/screenshots/ex4-02-run.png) · [after](../docs/screenshots/ex4-03-after.png) |
| 5 · priced offer | passes: all 9 sections, MD × rate per role, PM 12 %, QA 15 %, reserve 10 %, VAT; licences `[DOPLNIT]`; three costed budget cuts; purple cover with the pink panel | [cover](../docs/screenshots/ex5-00-cover.png) · [offer](../docs/screenshots/ex5-01-offer.png) · [price](../docs/screenshots/ex5-02-price.png) · [run](../docs/screenshots/ex5-03-run.png) |
| 6 · tender matrix | passes: 83 rows with sources, every "Done when" item, document inventory, scoring example, conditional go/no-go | [matrix](../docs/screenshots/ex6-01-matrix.png) · [run](../docs/screenshots/ex6-02-run.png) |
| 7 · draft bid check | passes: all 9 blocking errors, plus E11–E15 from the key; ISO 9001 and 30. 6. 2027 correctly OK | [matrix](../docs/screenshots/ex7-01-matrix.png) · [run](../docs/screenshots/ex7-02-run.png) |

The offer arithmetic was checked by hand in all three runs: 460 MD / 6,696,250 Kč, 557.5 MD /
8,064,750 Kč and 386 MD / 5,606,000 Kč excl. VAT. Every line is MD × rate, the PM, QA and
reserve rules hold, and the VAT is exact.

The offer's cover is a full-page background in its own section. Quick Look's preview cannot
place it, so in [offer](../docs/screenshots/ex5-01-offer.png) the cover looks faded and overlaps the summary; the
background itself is in [cover](../docs/screenshots/ex5-00-cover.png). Open the DOCX in Word to see the real page.

## Fixed after the runs

- **Brand manual.** Rules first came from quanti.cz (uppercase headings, rounded cards, black
  `#151515`). `quanti-brand`, `tokens.json`, `brand-brief.md` and the deck-review key now follow
  the manual: Montserrat Bold sentence-case headings, the cut-corner basic shape, logo always
  bottom-right, black `#040505`, secondary colours only for special occasions, Arial as the
  system font, the claim and vision.
- **Fonts.** The first run set headings in "Montserrat Medium", and the offer's Word heading
  styles kept the theme font; both fell back to a serif ([screenshot](../docs/screenshots/ex3-00-run1-font-fallback.png)).
  The skill now requires the font name `Montserrat` exactly, set on the theme, the styles and the
  runs, and checks the fonts found in the file.
- **Font files.** The variable `Montserrat.ttf` rendered headings at weight 100 in Quick Look.
  It was replaced by the static Regular, Medium, SemiBold and Bold files.

## Still open

1. **The estimate varies.** The same prompt priced the offer at 386, 460 and 557.5 MD; the
   arithmetic is right every time, but the effort per deliverable is a judgement. In the room,
   compare the MD tables, not the totals ([prep](../docs/prep.md) lists this trap).
2. **Penalty wording.** Exercise 7 summarised penalties as "0.1 % per day". That rate applies only
   to the final deadline; milestones are 2,000 Kč/day ([answer key](../solutions/tender-answer-key.md), SoD čl. 7).
3. **Exercise 4** did not add the missing client-problem slide, only named it, because the skill
   says to keep the content and order. That is intended.
4. **Exercises 0, 1, 2 and 8**: see the next section.

# Dry run in the Claude app, 2026-11-25

**What was run.** Exercises 0, 1, 2 and 8 in the Claude web app (claude.ai in Chrome, the same UI
the desktop app shows), on a personal Ultra account, model Fable 5.2, permission mode *Manual*.
The plugin was uploaded as `dist/quanti-sales.zip` (version 1.2.0). Exercise prompts were typed
without diacritics (a limitation of the automation, not of the app); Claude answered in Czech
with diacritics anyway.

**Differences from the desktop app.** The web app has no local folders, so exercise 1 got the
corpus as `tone-corpus.zip` attached to the chat and Claude unpacked it itself; in the desktop app
you grant the `sample-data` folder instead. Exercise 1 saved `tone-of-voice.md` as a downloadable
file, not into `brand/`.

## Results

| Exercise | Result | Screenshots |
|---|---|---|
| 0 · setup | passes: **Plugins → Add → Upload plugin** shows a preview (name, description), then the plugin page "Quanti sales · Added · v1.2.0" with the four skills; the smoke test named `#DF2686`, `#4D1254`, Montserrat, Arial as system font and "logo vždy v pravém dolním rohu", plus the font-name trap from the skill | [add menu](../docs/screenshots/ex0-00-add-menu.jpg) · [upload](../docs/screenshots/ex0-01-upload.jpg) · [added](../docs/screenshots/ex0-02-plugin-added.jpg) · [smoke test](../docs/screenshots/ex0-03-smoke-test.jpg) |
| 1 · tone of voice | passes: 7 principles, each with "ano/ne" quotes machine-checked against the corpus (57 usable texts, one is a 404 page), word list in three groups, addressing rules, a comparison table with the skill and a complete replacement for the skill's Tone of voice section; the activity panel lists `quanti-brand` as used | [tone-of-voice.md](../docs/screenshots/ex1-01-tone-of-voice.jpg) |
| 2 · design system | passes with one follow-up: **Settings → Capabilities → Design systems → Manage → New design system → Using Claude** opens a chat with an empty artifact; brand files attached, built in about 5 min, header "Quanti · Design System · Only you". **Design → Slides → Choose design system → Quanti**: in Manual mode Claude asks to copy `tokens.json` into the deck (Allow once). Slides: purple, pink cut-corner panel, Montserrat Bold sentence case, only brand colours; but the logo was an empty placeholder because the Slides agent could not read the logo files at the path the design system's README gives. Attaching `quanti-logo-white.svg` and asking for it fixed the title slide; Claude correctly refused to put a white logo on the white content slide and asked for the colour one | [new](../docs/screenshots/ex2-00-new-design-system.jpg) · [files](../docs/screenshots/ex2-01-upload-brand-files.jpg) · [built](../docs/screenshots/ex2-02-design-system-built.jpg) · [prompt](../docs/screenshots/ex2-03-permission-prompt.jpg) · [run](../docs/screenshots/ex2-04-slides-run.jpg) · [title before](../docs/screenshots/ex2-05-title-slide.png) · [title after](../docs/screenshots/ex2-07-title-slide-logo.png) · [content](../docs/screenshots/ex2-06-content-slide.png) |
| 8 · own skill | passes: example "Friday pipeline report for management" (four fictional deals); Claude returned a **Save plugin** card, `SKILL.md` for download (name, description in the team's words, 7 fields, rules, final check) and a test run with `[DOPLNIT]` where the notes had no data; it also wrote "Memory updated", so the account memory now knows about the skill | [skill](../docs/screenshots/ex8-01-skill.jpg) · [rules](../docs/screenshots/ex8-02-skill-rules.jpg) |

## Found and fixed in the docs

- **Menu paths.** The plugin upload is **Plugins → Add → Upload plugin**, and installed plugins
  are under **Settings → Plugins**; there is no "Customize" menu any more. Design systems are
  created from a chat ("Using Claude"), not from a form. Both are corrected in
  [01-setup](../docs/01-setup.md), [prep](../docs/prep.md) and [exercises](../docs/exercises.md).
- **Permission prompt.** In *Manual* mode the slide deck stops at "Allow Claude to copy files
  into this artifact?" until someone clicks. Added to the traps table and to exercise 2.
- **Logo in Slides.** The design-system README points the Slides agent at
  `assets/Logos/quanti-logo.svg`, which it could not read. Exercise 2 now tells participants to
  attach the logo file if the placeholder appears.

## Still open

1. **Logo path in the design system.** Ask the design-system chat to move the logos where the
   Slides agent reads them (or embed them as components), then re-run exercise 2 without the
   follow-up.
2. **Quanti account.** This run used a personal Ultra account. On the Quanti Team or Enterprise
   plan check that Cowork, Skills and design systems are enabled and that the plugin can be
   set *Installed by default* (see [prep](../docs/prep.md)).
3. **Exercise 1 decisions** are the participants' to make in the room: keep the ban on
   "komplexní" and add "špičkový"? one exclamation mark per blog post? The skill was not changed.

# Dry run on the official template and the HubSpot export, 2026-11-25

Plugin **1.3.0**: decks are built on the official Quanti PowerPoint template, company slides are
copied from the intro deck, and the new `deal-brief` skill reads a HubSpot deal. Exercises 3 and
9a were run headless (`claude -p --plugin-dir`, Claude Code 2.1.311, no LibreOffice) in a fresh
copy of `sample-data/`. Exercise 9c (write-back) cannot be run without HubSpot edit rights.

| Exercise | Result | Output / screenshots |
|---|---|---|
| 3 · deck on the official template | passes: 8 slides on the Quanti Theme layouts (Intro, Title and Content, the Gantt sample slide for the timeline, Outro); only purple, pink, black, white and the 20 % tints (the Gantt sample's secondary colours were recoloured); fonts Montserrat + the template's Arial; logo bottom-right on every slide; „Kdo jsme“ copied from intro-deck slide 3 unchanged; claims only from the brief and the approved list; second retail reference left as `[DOPLNIT]` because the intro deck has only Dr. Max; `validate.py --original` passes. 81 turns, US$ 4.28, 10.7 min | [deck](../docs/screenshots/ex3-03-template-deck.jpg) · [Bylinkarna_uvod_example.pptx](../solutions/Bylinkarna_uvod_example.pptx) |
| 9a · HubSpot brief | passes every row of the [key](../solutions/deal-brief-key.md): 10 sections, every fact with (type, date); both deadline e-mails shown, newer used; Marie Vltavská flagged as second-hand; deal amount labelled as our guess; competitor price with its two caveats; app left as an open question; `[DOPLNIT]` list for the offer. It also spotted that the e-mail's „pátek 5. 12.“ is a Saturday, which is now a documented trap. 19 turns, US$ 0.75, 90 s | [brief](../docs/screenshots/ex9-01-brief.jpg) · [deal-brief-example.md](../solutions/deal-brief-example.md) |

## Caveats of this run

- **Rendering.** The deck screenshot is a macOS Quick Look preview rendered in Chrome: it draws
  headings in a serif fallback and skips some preset shapes (the number panel on slide 2, parts
  of the Gantt). Open the example PPTX in PowerPoint with Montserrat installed for the real look;
  the file itself has only Montserrat and Arial.
- **Font names in the template.** The layouts use the font names `Montserrat SemiBold` and
  `Montserrat ExtraBold`. The workshop font pack has Regular, Medium, SemiBold and Bold, so
  ExtraBold headings fall back on a machine without it. Add `Montserrat-ExtraBold.ttf` to
  `sample-data/brand/fonts/` (SIL OFL) and to the prep step.
- **Closing slide.** The CLI put the tester's name on the Outro (personal instructions on the
  test machine); in Cowork it is the participant's.
- **Time.** Building on the template takes about 10 minutes of Claude time against 2–6 minutes
  for the earlier hand-drawn route: more turns for unpacking, duplicating and validating.
  Exercise 3 keeps 25 minutes; start the prompt first, then explain while it runs.

## Still open

1. `Montserrat-ExtraBold.ttf` in the font pack and the prep checklist.
2. Exercise 9c (note, task, stage move) tested on a real deal by someone with HubSpot edit rights.
3. Exercise 4 re-run with plugin 1.3.0: the fix now rebuilds the deck on the template.
4. Exercise 2 with the `.potx` uploaded to the design system (added to the file list, not run).
