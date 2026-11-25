> 🌍 Read this in: **English** | [Česky](prep.cs.md)

# Workshop prep

## Participants: the day before (10 min)

1. Install the **Claude desktop app** and sign in with your Quanti account.
2. Install the font **Montserrat**: double-click each `sample-data/brand/fonts/Montserrat-*.ttf`
   (4 files) → Install. Without it, PowerPoint and Word show the decks in a fallback font.
3. Unzip the workshop package you received (`qti-cowork-sales.zip`) to
   `~/Documents/qti-cowork-sales`.
4. In Claude, open **Settings → Plugins** and check that `quanti-sales` is there. If it is not,
   tell the facilitator; you will upload it in exercise 0.
5. Have PowerPoint, Word and Excel (or Keynote, Pages, Numbers) ready to open the outputs.

## Facilitator: before the day

- [ ] **Org owner:** Organization settings → Cowork and Skills enabled (plugins need both).
- [ ] **Org owner:** Organization settings → Plugins & skills → Add → Upload a plugin →
      `dist/quanti-sales.zip`; set it *Installed by default* for the participants' group.
- [ ] **Enterprise only:** design systems are off until enabled in Organization settings →
      Artifacts. Decide who may *Publish* a design system; in the workshop participants create
      but do not publish.
- [ ] Optional: install Anthropic's `brand-voice` plugin from the plugin catalogue for exercise 1.
- [ ] The repository is private. Send participants a zip: `git archive -o qti-cowork-sales.zip
      --prefix=qti-cowork-sales/ HEAD`, or add them as collaborators.
- [ ] Run the dry run yourself (exercises 0, 3, 6 at least). The last recorded run is in
      [screenshots/](screenshots/README.md).
- [ ] Re-check the tender on [NEN](https://nen.nipez.cz/verejne-zakazky/detail-zakazky/N006-26-V00032057):
      new clarifications change the answer key in `solutions/tender-answer-key.md`. After the
      deadline the tender stays a valid exercise; say so in the room.
- [ ] Print or share `solutions/` only after the exercises.

## Known traps

| Symptom | Cause | Fix |
|---|---|---|
| Answers about the brand are generic | Plugin not installed or disabled | Settings → Plugins; or name the skill: "Použij skill quanti-brand" |
| Deck opens in Arial/Calibri | Montserrat not installed on this machine | Install the font (step 2) |
| Claude asks for access to a folder every time | New conversation, folder not granted | Grant `sample-data` once at the start of each conversation |
| The offer total differs between runs | The estimate (MD) is a judgement, the arithmetic is not | Compare the MD table, not only the total; recompute one line |
| Tender matrix misses the extended deadline | Clarifications not read or old annexes used | Point Claude at the whole `tender/` folder and ask for the document inventory first |
| Slides stop at "Allow Claude to copy files into this artifact?" | Permission mode *Manual*: copying the design system's tokens into the deck needs a click | Press **Allow once**, or switch the conversation to *Auto* |
