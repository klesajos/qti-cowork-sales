> 🌍 Read this in: **English** | [Česky](exercises.cs.md)

# Exercises

Each exercise: a prompt to paste (in Czech, as you would work), what to watch, and **Done
when**. Start a **new conversation** for each exercise and grant it the folder
`~/Documents/qti-cowork-sales/sample-data`. Answer keys are in `solutions/` (facilitator).

## 0. Setup (10 min)

Follow [01-setup](01-setup.md): plugin, folder, smoke test.

**Done when**
- `quanti-sales` with five skills is listed in Settings → Plugins.
- The smoke-test answer names `#DF2686`, `#4D1254`, Montserrat and "logo bottom-right".

<details><summary>What good looks like</summary>

*Plugins → Add → Upload plugin*

![Add menu](screenshots/ex0-00-add-menu.jpg)

*Plugin added with four skills*

![Plugin added](screenshots/ex0-02-plugin-added.jpg)

*Smoke test*

![Smoke test](screenshots/ex0-03-smoke-test.jpg)

</details>

## 1. Tone of voice from real texts (20 min)

```
Ve složce tone-corpus/ je 58 veřejných textů Quanti. Popiš náš tón: 5–7 zásad, ke každé
dvojici „takhle ano / takhle ne“ s citací z korpusu, seznam slov, kterým se vyhýbáme, a jak
oslovujeme čtenáře. Pak to porovnej se sekcí Tone of voice ve skillu quanti-brand a navrhni
konkrétní úpravy skillu. Ulož jako brand/tone-of-voice.md.
```

With the `brand-voice` plugin installed, try `/brand-voice:generate-guidelines` on the same
folder and compare.

**Done when**
- Every principle has at least one real quote (search the corpus for one to verify).
- There is a list of concrete edits to the skill, not "looks good".

<details><summary>What good looks like</summary>

*tone-of-voice.md: seven principles, each with verified quotes, and a rewritten skill section*

![Tone of voice](screenshots/ex1-01-tone-of-voice.jpg)

</details>

## 2. Design system from brand assets (20 min)

In **Settings → Capabilities → Design systems → Manage**, choose **New design system → Using
Claude**. A chat opens with an empty design-system artifact; pick **Upload brand files** (or the
`+` in the reply box) and attach from `brand/`: `QUANTI_Brand_Manual_2024.pdf`, `brand-brief.md`,
`tokens.json`, `quanti-logo.svg`, `quanti-logo-white.svg`, `fonts/Montserrat-*.ttf` and
`templates/Quanti_PPT_Template_CZ.potx`. Then send:

```
Postav design systém z přiložených souborů. Pojmenuj ho „Quanti“. Dodrž manuál: růžová #DF2686
a fialová #4D1254 jako jediné primární barvy, Montserrat Bold nadpisy v sentence case, základní
tvar s useknutým rohem, logo vždy vpravo dole. Nepublikuj ho.
```

The artifact header must say **Quanti · Design System · Only you**; *Only you* means it is not
published. Building takes about 5 minutes.

Then open **Design → Slides**, pick **Choose design system… → Quanti** under the prompt box, and
send:

```
Udělej jeden titulní slide a jeden obsahový slide pro úvodní schůzku s Bylinkárnou Vltava.
```

In *Manual* permission mode Claude first asks **Allow Claude to copy files into this artifact?**
(the design system's tokens); press **Allow once**. If the slides come back with an empty logo
placeholder, attach `brand/quanti-logo-white.svg` and send:

```
Vlož přiložené bílé logo vpravo dole místo zástupného místa.
```

**Done when**
- The preview uses pink `#DF2686` and purple `#4D1254` only, Montserrat with bold
  sentence-case headings.
- The title slide has the pink panel with cut corners on purple, and the white logo bottom-right.

<details><summary>What good looks like</summary>

*New design system → Using Claude*

![New design system](screenshots/ex2-00-new-design-system.jpg)

*Design system built: Quanti · Only you*

![Design system](screenshots/ex2-02-design-system-built.jpg)

*Permission prompt in Manual mode*

![Permission prompt](screenshots/ex2-03-permission-prompt.jpg)

*Title slide after the logo follow-up, and the content slide*

![Title slide](screenshots/ex2-07-title-slide-logo.png)

![Content slide](screenshots/ex2-06-content-slide.png)

</details>

## 3. A deck from a brief (25 min)

```
Použij skill quanti-brand. Z podkladu offer/client-brief.md připrav úvodní prezentaci Quanti
pro Bylinkárnu Vltava na oficiální šabloně: 8 slidů, 16:9, PPTX. Struktura: titulní slide, jak
rozumíme vaší situaci, co navrhujeme, jak bychom postupovali (časová osa), proč Quanti (slidy
z intro prezentace decks/Quanti_intro_2026_CZ.pptx, jen schválená tvrzení), 2 reference
z retailu, další krok, závěrečný slide. Ulož jako Bylinkarna_uvod.pptx a na konci vypiš, co
jsi zkontroloval.
```

**Done when**
- `Bylinkarna_uvod.pptx` opens with 8 slides on the **Quanti Theme** layouts (Intro, Title and
  Content, Jenom nadpis with a timeline, Outro…), Montserrat, bold sentence-case headings, only
  pink, purple, black, white and their tints.
- The title and closing slides are the template's Intro and Outro; the logo is bottom-right on
  every slide; no sample text ("Text", "Insert text here") left anywhere.
- "Proč Quanti" and the references are slides copied from the intro deck, not rewritten.
- Slide 2 quotes the brief (14 prodejen, Money S5, 30. 9. 2027).
- "Proč Quanti" uses only claims from `approved-claims.md`; anything else is `[DOPLNIT]`.
- The last slide has one concrete next step.

<details><summary>What good looks like</summary>

*Deck, second run*

![Deck, second run](screenshots/ex3-01-deck.png)

*Prompt and answer*

![Prompt and answer](screenshots/ex3-02-run.png)

</details>

## 4. Review and fix an off-brand deck (20 min)

```
Zkontroluj prezentaci decks/Bylinkarna_uvodni_prezentace.pptx skillem deck-review.
```

Read the report, then:

```
Oprav ji podle zprávy a ulož s příponou _opraveno.
```

**Done when**
- The report finds at least 12 of the errors in `solutions/deck-review-key.md`, including the
  stretched logo, the colour logo on purple and the unapproved claims (200 mil. Kč, ISO 27001).
- The fixed deck has no blue, green, orange, Calibri or Times; claims are removed or `[DOPLNIT]`.

<details><summary>What good looks like</summary>

*Before*

![Before](screenshots/ex4-01-before.png)

*Review report*

![Review report](screenshots/ex4-02-run.png)

*After the fix*

![After the fix](screenshots/ex4-03-after.png)

</details>

## 5. A priced offer (35 min)

```
Skillem quanti-offer připrav nabídku pro Bylinkárnu Vltava podle offer/client-brief.md a ceníku
offer/rate-card.xlsx (dodržuj pravidla na listu Pravidla). První fáze: e-shop B2C + B2B
napojený na Money S5 a věrnostní program bez nativní mobilní aplikace; platformu doporuč.
Výstup DOCX.
```

Answer Claude's questions if it asks (budget, deadline are in the brief).

**Done when**
- The DOCX follows the offer structure: summary, understanding, solution, plan, team, price,
  why Quanti, next steps.
- The price table shows MD × rate per role; PM = 12 % and QA = 15 % of the right base;
  totals excl. VAT, VAT 21 %, incl. VAT. Recompute one line yourself.
- Licences are `[DOPLNIT]`, not a guessed number.
- The hand-over report lists open `[DOPLNIT]`s and price-changing assumptions.

<details><summary>What good looks like</summary>

*Offer DOCX, all pages*

![Offer DOCX, all pages](screenshots/ex5-01-offer.png)

*Price section*

![Price section](screenshots/ex5-02-price.png)

*Prompt and answer*

![Prompt and answer](screenshots/ex5-03-run.png)

</details>

## 6. Tender requirements matrix and go/no-go (30 min)

```
Skillem tender-check zpracuj zakázku ve složce tender/ (všechny dokumenty včetně vysvětlení;
složku draft/ zatím ignoruj). Udělej soupis dokumentů, matici požadavků do Matice_TSB.xlsx,
vysvětli hodnocení a dej go/no-go pro Quanti.
```

**Done when** the matrix and the summary contain:
- the current deadline **27. 11. 2026 10:00** and how it moved;
- **3** references ≥ 4 M Kč excl. VAT (not the ZD's "1");
- the **updated** contract and Odborná úroveň (19. 10.) as the current versions;
- paper submission, envelope with tender name + "NEOTEVÍRAT", contract 3× (2 removable);
- ISO 9001 + ISO 27001, 5 different people, PM certificate;
- evaluation 70 % price / 30 % team, and the lower-price rule;
- CWV targets as an acceptance condition on CrUX data;
- each row with a source (document + article).

Compare with `solutions/tender-answer-key.md` (68 rows): what did Claude miss, what did it
add that is not in the documents?

<details><summary>What good looks like</summary>

*Requirements matrix*

![Requirements matrix](screenshots/ex6-01-matrix.png)

*Prompt and answer*

![Prompt and answer](screenshots/ex6-02-run.png)

</details>

## 7. Check a draft bid (20 min)

```
Skillem tender-check zkontroluj rozpracovanou nabídku tender/draft/Quanti_nabidka_TSB_pracovni.docx
proti zadávacím podmínkám ve složce tender/. Blokující problémy první.
```

**Done when**
- All blocking rows of `solutions/draft-bid-key.md` are found: old deadline, electronic
  submission, price mismatch (lower price prevails), "indicative" price, 2 references instead
  of 3, a reference under 4 M Kč, one person in two roles, missing PM certificate, ISO 27001
  in progress.
- ISO 9001 and the 30. 6. 2027 date are **not** flagged.

<details><summary>What good looks like</summary>

*Draft check in the matrix*

![Draft check in the matrix](screenshots/ex7-01-matrix.png)

*Prompt and answer*

![Prompt and answer](screenshots/ex7-02-run.png)

</details>

## 9. HubSpot: from a deal to a brief and back (30 min)

Participants work on **their own open deal** through the HubSpot connector; the facilitator shows
the same prompts on `hubspot/`, an export of the fictional deal Bylinkárna Vltava.

**9a · Brief** (participants: replace "ve složce hubspot/" with "v HubSpotu" and name your deal)

```
Skillem deal-brief připrav podklady k nabídce pro deal Bylinkárna Vltava ve složce hubspot/:
kdo je kdo, co chtějí, termíny, rozpočet, konkurence, rozpory a otevřené otázky, rizika,
další krok. Ke každému faktu zdroj (typ aktivity + datum). Ulož jako brief_Bylinkarna.md.
```

**9b · Hand-over** (optional, if time allows)

```
Z briefu udělej client-brief pro quanti-offer a připrav nabídku ve dvou variantách:
bez mobilní aplikace a s ní. Ceník offer/rate-card.xlsx. Výstup DOCX.
```

**9c · Write-back** (participants only, on their own deal)

```
Zapiš do HubSpotu k tomuto dealu poznámku se shrnutím nabídky a otevřenými body, založ úkol
„Follow-up nabídka“ na 3 pracovní dny po odeslání a posuň deal do fáze Sent Offer. Před každým
zápisem mi ukaž, co přesně změníš.
```

**Done when**
- The brief has every fact with a source; the two deadline e-mails are both shown and the newer
  one is used (B2B by 30. 6. 2027, full by 30. 9. 2027); the brief notices that the e-mail's
  "pátek 5. 12." is a Saturday.
- Marie Vltavská (owner, known only from the call) is in "Lidé a role"; the deal amount is
  labelled as our guess; the competitor's 2,4 mil. carries its caveat; the mobile app is an
  open question, not a decision. Key: `solutions/deal-brief-key.md`.
- In 9c Claude showed a confirmation table before each write; the note is under 150 words;
  the task has a date and owner; the stage moved one step forward.

## 8. Your own skill (15 min)

Pick a task you repeat every week. With Claude:

```
Chci z tohoto postupu udělat skill pro náš tým: <popis, příklad dobrého výstupu, pravidla>.
Navrhni SKILL.md (název, popis, kroky, závěrečná kontrola) a vyzkoušej ho na tomto příkladu: <…>.
```

**Done when** you have a `SKILL.md` whose description uses the words your team actually says,
and one test run. Rollout: [06-own-skill](06-own-skill.md).

<details><summary>What good looks like</summary>

*Example: a Friday pipeline report for management. Claude returns a "Save plugin" card, the
SKILL.md and a test run on four deals.*

![SKILL.md](screenshots/ex8-01-skill.jpg)

*Rules for values: nothing recomputed, `[DOPLNIT]` for gaps*

![Rules](screenshots/ex8-02-skill-rules.jpg)

</details>
