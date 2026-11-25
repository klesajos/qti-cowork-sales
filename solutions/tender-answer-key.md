# Answer key: T.S.BOHEMIA, "Technická modernizace a optimalizace webové aplikace tsbohemia.cz"

Contracting authority: T.S.BOHEMIA a.s., IČ 62304381, Olomouc. Contact person: Patrik Prikrt, pprikrt@tsbohemia.cz.
Regime: selection procedure under the OP TAK "Pravidla pro výběr dodavatelů" (rules in force from 1. 5. 2025). It is explicitly **not** a procedure under ZZVZ 134/2016 (ZD p. 1). Contract type: "Dodávky" (supplies). Co-financed by an OP TAK grant ("Digitální podnik").

**Source abbreviations**
- **ZD**: 261001_ZD_signed.pdf (Zadávací dokumentace, signed 1. 10. 2026; published on the profile 2. 10. 2026 20:30 per zdlist.html)
- **FN**: Příloha 1, Formulář nabídky (260922)
- **SoD**: Příloha 2, Smlouva o dílo. "SoD-orig" is the 260922 version; "SoD-upd" is 261019_…_aktualizovana. Clause numbers were rebuilt from the DOCX auto-numbering, because the text extraction loses them. They match the cross-references in VZD 1 (e.g. "bod 3.3.1", "bod 4.4", "bod 5.2", "bod 5.3").
- **SoD-P1 / SoD-P2**: SoD annex 1 (Účel a popis díla = TS text) and annex 2 (Položkový rozpočet)
- **TS**: Příloha 3, Technická specifikace (260703 PDF). Section numbers are the TS's own (1 = GA, 2 = Redesign, 3 = Projekt 1, 4 = Projekt 2, 5 = Košík, 6 = Logování, 7 = Přístupnost).
- **OU**: Příloha 4, Odborná úroveň. "OU-orig" is 260922; "OU-upd" is 261019_…_aktualizovana.
- **VZD 1 / 2 / 3**: Vysvětlení zadávacích podmínek. Dates as stated inside the documents: VZD 1 is dated 19. 10. 2026, VZD 2 is dated 19. 11. 2026, VZD 3 is dated 20. 11. 2026. The filename "261020" of VZD 3 is wrong: the text and the signature say **20. 11. 2026**.

---

## 1. Requirements matrix

| ID | Category | Requirement | Source | Changed by | Trap? |
|---|---|---|---|---|---|
| R01 | Deadline & submission | Submission deadline. Originally **2. 11. 2026, 10:00**. Now **27. 11. 2026, 10:00**. | ZD čl. 10 (p. 5) | VZD 1 (19. 10.) moved it to 20. 11. 2026 10:00. VZD 2 (19. 11.) moved it to 27. 11. 2026 10:00. | Yes. There were two extensions. VZD 2 went onto the profile on 20. 11. 2026 at 08:58 (zdlist.html), about 1 hour before the deadline then in force. A bidder who planned around 20. 11. would have rushed for nothing. |
| R02 | Deadline & submission | The offer must be **delivered** (not merely posted) to Sladovní 103/3, Pavlovičky, 779 00 Olomouc, "k rukám Patrika Prikrta", within the deadline. | ZD čl. 10 (p. 5) | — | Yes. What counts is receipt at the address, not the postmark date. |
| R03 | Deadline & submission | **Paper only**: one paper original plus an electronic copy on a data carrier (CD/DVD/USB). Electronic submission (e.g. NEN) is not allowed. | ZD čl. 4 (p. 3), čl. 10 | VZD 1 Ad 11 confirms "výhradně v listinné formě". | Yes. Most CZ tenders are e-submission, so habit leads bidders the wrong way. |
| R04 | Formal | Sealed envelope ("důsledně zalepená obálka") marked with the **tender name** and "**NEOTEVÍRAT**". | ZD čl. 4 (p. 4) | — | Yes. Bidders tend to remember "NEOTEVÍRAT" but forget the tender name. |
| R05 | Formal | Pages must be **numbered and bound** so that no sheet can be removed, or secured "jinou vhodnou formou". | ZD čl. 4 (p. 3) | — | — |
| R06 | Formal | Language: Czech or Slovak. | ZD čl. 4 (p. 4) | — | — |
| R07 | Formal | Variants are not permitted. | ZD čl. 8 (p. 5) | — | — |
| R08 | Deadline & submission | Opening: originally 2. 11. 2026 from 10:00. Now "neprodleně po konci lhůty" at Sladovní 103/3. Only bidders who submitted on time may attend. | ZD čl. 11 (p. 5) | VZD 1 and VZD 2: opening starts immediately after the (extended) deadline. | — |
| R09 | Deadline & submission | Offer validity ("zadávací lhůta"): **3 months from the end of the submission deadline**. Computed: until 27. 2. 2027. | ZD čl. 10 (p. 5) | Shifts with the deadline (computed, not stated). | — |
| R10 | Deadline & submission | Clarification requests must be in writing and must reach the authority **≥ 4 working days before the deadline**. The authority publishes answers on the profile within 2 working days. If it is late, it must extend the deadline by at least the number of working days of delay. | ZD čl. 9 (p. 5) | — | Yes (computed). With the 27. 11. deadline, the last day for a request was about 23. 11. 2026, so the window is closed as of 25. 11. |
| R11 | Formal (mandatory doc) | **FN**, filled in and **signed** (Příloha 1). | ZD čl. 4 a. | — | — |
| R12 | Formal (mandatory doc) | **Professional CVs of all team members** and a **project-management certificate for the PM**. | ZD čl. 4 b.; FN "odborná způsobilost realizačního týmu" | — | — |
| R13 | Formal (mandatory doc) | Copies of **ISO 9001 and ISO 27001** certificates. | ZD čl. 4 c.; FN "shoda s technickou normou" | — | — |
| R14 | Formal (mandatory doc) | Completed **OU** (Příloha 4). It is "povinnou součástí nabídky". | ZD čl. 3.2 d), čl. 4 d. | Use OU-upd (19. 10.). | Yes. Using the original OU form loses the slot for equivalent technologies (see R31). |
| R15 | Formal (mandatory doc) | **Binding draft contract** (SoD), filled in and signed by an authorised person, **including both annexes** (annex 2 = priced item budget plus MD rates), in **3 copies, 2 of them freely removable** from the offer. | ZD čl. 4 e. | Use SoD-upd (19. 10.). | Yes. "3 copies, 2 loose" conflicts with "bind all pages" (R05) unless planned for. The SoD must be the updated version. Annex 2 must be priced. |
| R16 | Formal (mandatory doc) | Scan of the paper offer (ideally PDF) on CD/DVD/USB. | ZD čl. 4 f. | — | — |
| R17 | Contract & commercial | The SoD may be completed **only where and how the authority indicates**. The bidder must accept the commercial and payment terms. | ZD čl. 4 (p. 4); FN "Prohlášení účastníka" | — | Yes. Edits to clauses (e.g. adding an acceptance deadline) would breach the conditions. |
| R18 | Qualification | **Základní způsobilost** per § 74 odst. 1–3 ZZVZ, proven by an honour declaration in the FN. | ZD čl. 6 (p. 4); FN | — | — |
| R19 | Qualification | **Profesní způsobilost** per § 77 odst. 1 ZZVZ, plus authorisation to do business in the CZ in the relevant scope. Honour declaration. | ZD čl. 6; FN | — | — |
| R20 | Qualification | **≥ 3 reference contracts**. Each must be: (i) "návrh a implementace nebo technická modernizace webové aplikace v oblasti **e-commerce**"; (ii) performed within the **last 5 years before the procedure started**; (iii) worth **≥ 4 000 000 Kč bez DPH each**. For each, give the subject, completion date, value and contact, and declare it "poskytnuta řádně a včas". | FN "Technická kvalifikace – referenční zakázky" | VZD 1 Ad 5: ZD čl. 6 ("alespoň 1") **is wrong**; 3 references are required. | Yes. The ZD text says 1. A careless reader of the main document submits 1 reference and is excluded. |
| R21 | Qualification | Ongoing contracts count as references **only if** a complete functional part ("ucelená funkční část") was officially handed over or put into live operation within the 5-year window **and the amount paid for it** at that moment met the 4 M threshold. The date of handover or go-live is used as the completion date. | VZD 1 Ad 1 | New via VZD 1. | Yes. "Long-term cooperation" does not qualify on its own. |
| R22 | Qualification | **Team of ≥ 5 different persons**, one per role: (a) Projektový manažer; (b) Senior Frontend Developer / Frontend Architekt; (c) UX/UI specialista; (d) Specialista na analytiku; (e) DevOps / Infrastructure specialista. One person may not hold two roles. Members must take part "přímo a aktivně". | FN "odborná způsobilost realizačního týmu"; ZD čl. 3.2 b) | — | Yes. Small agencies often combine PM with UX, or FE with DevOps. |
| R23 | Qualification | Each role needs **≥ 5 years of active practice** in that role. The PM must also hold an **international PM certification (e.g. PRINCE2 or Scrum)**, and a copy goes in the offer. | FN (role rows) | — | Yes. The PM certificate is required twice (ZD čl. 4 b and FN), and a missing copy is a qualification gap. |
| R24 | Qualification | **ISO 9001** valid **on the submission date**, with scope covering software development and project activities/management. | FN "shoda s technickou normou" | — | Yes. Scope wording: a certificate scoped only to "trading" or "IT services" may not fit. |
| R25 | Qualification | **ISO 27001** valid on the submission date, with the same scope requirement. | FN | — | Yes. Many agencies do not hold ISO 27001, so this is a hard knock-out. |
| R26 | Qualification | The authority may ask for documents proving qualification if it has doubts. | ZD čl. 6 | — | — |
| R27 | Evaluation | Criteria: **Nabídková cena bez DPH, 70 %** (minimising), and **Odbornost a zkušenosti realizačního týmu, 30 %** (maximising). Scale 1–100 points. **Tie-break: lowest price**. | ZD čl. 3, 3.3 (pp. 1–3); FN "Údaje pro hodnocení" | — | — |
| R28 | Evaluation | Price score = **100 × (lowest price / evaluated price) × 0.7**. Price = sum of all items in the item budget. | ZD čl. 3.1 (p. 2) | — | — |
| R29 | Evaluation | Team score = **(raw points / 97.5) × 100 × 0.3**. Raw points: **1 pt** per qualifying reference (max 5 per role); **+1 pt** if that reference is demonstrably **e-commerce**; **+0.25 pt** per checked evaluated technology used by that person on that reference. Max raw total is **97.5**. | ZD čl. 3.2 e)–f) (pp. 2–3) | — | Yes. 97.5 is the raw sub-criterion maximum, not the total score (that is 100). ZD čl. 3.2 e) also wrongly refers to "bodu 3.3.e" (it should be 3.2.e). |
| R30 | Evaluation | Role thresholds for a reference to score. PM: role equivalent to PM/team lead; web app design and implementation or modernisation; value **≥ 6 000 000 Kč bez DPH**. SFD/UXS/SNA/DevOps: equivalent role; value **≥ 3 000 000 Kč bez DPH**. All roles: completed within the **last 8 years** before the procedure started. Non-compliant references score 0. Per-role maxima (computed from the OU checklists: PM no tech list, SFD 10 tech, UXS 4, SNA 12, DevOps 12): PM 10, SFD 22.5, UXS 15, SNA 25, DevOps 25, total 97.5. | OU-upd, header of each role section | VZD 1 Ad 1: value = **value of the whole contract**, not the person's share; ongoing contracts accepted under the R21 logic. | Yes. There are two different windows (5 years for company references vs 8 years for persons) and two thresholds (6 M for PM vs 3 M for others), and the e-commerce point is a bonus here but mandatory for qualification. |
| R31 | Evaluation | A technology counts **only if that person used it directly**, not another team member or a subcontractor. **Equivalent technologies** may be named in the bracket "( )" next to the item. The evaluation committee decides whether they are equivalent. | OU-upd (each reference) | VZD 1 Ad 10 plus OU-upd: brackets for equivalents added (the original OU had none). | Yes. Equivalence is judged by the committee, so naming Kubernetes instead of Nomad does not guarantee the 0.25 pt. |
| R32 | Evaluation | The persons in the OU must be **identical** to those named in the FN. Only one person per role is evaluated. All evaluated persons must actually be on the delivery team. | ZD čl. 3.2 b) | — | Yes. Using a "star" person in the OU who differs from the FN person is not allowed. |
| R33 | Evaluation | The authority may request proof: confirmations of reference completion and original CVs. The bidder must cooperate. | ZD čl. 3.3 (p. 3); OU intro declaration | — | — |
| R34 | Price | Price is a **maximum price** in **CZK excl. VAT**. It covers all costs (team, other staff, licences, all fees). | ZD čl. 5 (p. 4) | — | — |
| R35 | Price | The price must be stated **in both the FN and the SoD**. If they differ, the **lower** price counts. | ZD čl. 5 (p. 4) | — | Yes. A typo costs money: you are held to the lower figure. |
| R36 | Price | Item budget (SoD-P2): 7 items (GA; Redesign; Projekt 1; Projekt 2; Košík; Logování; Přístupnost). **Their sum must equal the Cena Díla.** | SoD-P2 | — | Yes. Item prices later drive invoicing and partial handover (SoD 4.4, 5.2), so front-loading or back-loading has cash-flow effects. |
| R37 | Price | **Binding MD rates** for 5 roles (PM, SFD, UXS, SNA, DevOps) for extra/reduced work and ad-hoc post-handover service. They are **not evaluated**. | SoD-P2 | — | Yes. They are not scored but they bind you for change requests and post-delivery work. |
| R38 | Contract & commercial | Cena Díla is "**konečná a nepřekročitelná**" and includes integration, deployment and user training. It **excludes** external cloud/DB/hosting services, but only if they were consulted beforehand and approved in writing. | SoD 4.1–4.2 | — | Yes. This is a fixed price with no source-code access (VZD 1 Ad 4), which is the main pricing risk. |
| R39 | Contract & commercial | Delivery: the work must be completed "**nejpozději do 30. 6. 2027**". The authority alone may extend to **31. 12. 2027**, only if (i) the grant provider approves extending the project's realisation phase **and** (ii) the extension is needed for the authority's operational reasons. | SoD 3.1–3.2; ZD čl. 7 ("předpokládaná doba plnění do 30. 6. 2027") | Questioned in VZD 2 Q5, not answered yet. | Yes. ZD says "expected" while SoD says "at the latest". The extension is not a contractor right, even when the delay is caused by the authority's own backend team. |
| R40 | Contract & commercial | Place of performance and handover: Sladovní 103/3, Olomouc (the authority's seat), unless agreed otherwise. | ZD čl. 7; SoD 5.6 | — | — |
| R41 | Contract & commercial | Schedule: the contractor submits a draft **within 7 days of the SoD taking effect**, split at least by sub-project and phase. The authority comments within 7 days. The authority approves and may change the order. | SoD 3.3.1–3.3.4 | VZD 1 Ad 6: the contractor proposes the order of projects, and the final say is the authority's. | — |
| R42 | Contract & commercial | Reporting: status at least every 14 days; **written monthly report by the 10th** of the following month; a personal meeting at least 1× per month on request. | SoD 2.6.1–2.6.4 | — | — |
| R43 | Contract & commercial | Delivery only through the team named in the offer. Replacing a member needs **prior written consent**, and the replacement must meet the FN qualification **and have at least equal OU-level experience**. | SoD 2.5.1–2.5.3; FN team section | — | Yes. Inflating the OU with seniors makes later substitution almost impossible. |
| R44 | Contract & commercial | **Liability insurance ≥ 8 000 000 Kč** for the whole performance, with the same minimum for every subcontractor. Proof is due promptly after the SoD takes effect. Failure is a material breach. | SoD 2.7.1–2.7.3 | — | Yes. The subcontractor insurance requirement is easy to overlook. |
| R45 | Contract & commercial | Payment: invoice after the handover protocol for the Dílo or a part is signed. **30 days due** from delivery of the invoice. Only the part of the price for the handed-over part per annex 2, **minus retention**. | SoD 4.3–4.4 | VZD 1 Ad 7: no separate invoicing of analytic phases by default; smaller parts only by agreement (SoD 5.2). | Yes. P1/P2 analytic phases have separate acceptance but **not** separate invoicing, so pre-financing is long. |
| R46 | Contract & commercial | Invoices must show project name "**Komplexní modernizace IT infrastruktury ve společnosti T.S.BOHEMIA**" and reg. no. "**CZ.01.01.02/01/24_054/0007184**". Otherwise the invoice is returned and the due date restarts. | SoD 4.7–4.8 | — | Yes. A missing grant ID delays payment. |
| R47 | Contract & commercial | **Retention ("Zádržné") 10 %** of every invoiced part, held until the **last defect in the final handover protocol for the whole Dílo** is removed (or the SoD ends). The authority may set off its claims against it. | SoD 4.9.1–4.9.2 | — | Yes. Retention on early parts (e.g. GA, July 2027) is released only after the final project's defects are fixed. |
| R48 | Contract & commercial | Penalty for missing the **final deadline** (3.1/3.2): **0.1 % of Cena Díla bez DPH per started day**. | SoD 7.2 | — | Yes. This is calculated on the **whole** price, not the late part. |
| R49 | Contract & commercial | Penalty for missing a **Harmonogram milestone**: **2 000 Kč per day**. | SoD 7.3 | — | — |
| R50 | Contract & commercial | Penalty for a team role not staffed per 2.5.3, vacant, or inactive after a warning: **10 000 Kč per role per uninterrupted 30 days**. | SoD 7.4 | — | — |
| R51 | Contract & commercial | Penalties fall due the day after the entitlement arises and may be set off. Damages are claimable on top. The contractor acknowledges that damage may **exceed the price** (grant withdrawal). | SoD 7.5–7.6 | — | Yes. Grant clawback risk is pushed onto the contractor, but capped by R52. |
| R52 | Contract & commercial | **Aggregate liability cap 8 000 000 Kč** for all damage, penalties and other sanctions. It does not apply to intent or gross negligence. | SoD-upd 7.7 | **New** in SoD-upd (VZD 1 Ad 12 a). | Yes. It is absent from SoD-orig, so signing the old version means no cap. |
| R53 | Contract & commercial | Authority's late-payment interest: 0.1 % of the overdue amount excl. VAT per started day. | SoD 7.1 | — | — |
| R54 | Contract & commercial | **Licence** (from signing of the handover protocol): all known uses, irrevocable, unlimited, for the duration of the property rights, transferable and sublicensable. **Exclusive** for parts made solely for the authority. **Non-exclusive** for standard modules, libraries, frameworks and pre-existing works, but broad enough to use, modify, develop and transfer without further fees. A **list of non-exclusive components** (rights holder, licence terms) is due at handover. No components that prevent maintenance or migration without the contractor (no lock-in). | SoD-upd 6.2–6.6 | Changed by VZD 1 Ad 12 b + SoD-upd. SoD-orig required an exclusive licence to everything. | Yes. The component/licence inventory is a new deliverable. Proprietary accelerators or paid libraries are effectively excluded. |
| R55 | Contract & commercial | Handover: announce the demonstration **≥ 3 days** ahead. The authority may postpone it by up to 15 days, with no contractor delay during that time. Only complete parts per annex 2. A protocol lists defects and states whether the authority accepts. **No deadline for the authority to accept.** | SoD 5.1–5.3 | VZD 1 Ad 12 c: "Žádná lhůta pro převzetí díla stanovena není". Questioned again in VZD 2 Q4, not answered yet. | Yes. Acceptance, invoicing and retention release all depend on the authority's discretion. |
| R56 | Technical scope | Delivery of **source code** (machine-readable, editable) plus **user documentation** and **user training**. A trial operation precedes handover. **≥ 2 weeks of monitoring** after each go-live, with immediate defect fixing. | SoD 5.4–5.5, 5.7–5.8 | — | — |
| R57 | Contract & commercial | No separate **warranty period ("záruka")** is stated anywhere in the SoD or ZD. | SoD (whole text; no "záruk…" term) | — | Yes (absence). Statutory regime applies; the bidder should not assume or price a stated warranty or SLA. |
| R58 | Contract & commercial | Confidentiality survives termination. Partial withdrawal is possible for parts not yet started. Documentation must be archived **10 years**, with a duty to cooperate in financial control (§ 2 e) 320/2001 Sb.), passed down to subcontractors. Amendments only per Pravidla čl. 7.2. | SoD 8, 9.3, 10.2, 10.5; ZD čl. 12 | — | Yes. Partial withdrawal (9.3) means later projects may never be ordered. |
| R59 | Technical scope | Scope = **7 sub-projects**: (1) GA4/GTM new containers; (2) mobile redesign (Figma plus FE); (3) Technical modernisation P1 (Pages Router to App Router, read-heavy, BFF for product detail, shared cache); (4) P2 (Provider Hell, state management, cart/profile/HP/categories/search, React 19; estimate **80–130 MD**); (5) cart optimisation (FoxEntry, cross-sell, B2B/B2C, Mapy.com); (6) FE logging (e.g. Winston, Promtail, Loki, Grafana); (7) accessibility to **WCAG 2.1 AA / EN 301 549**. Not divided into lots, so the full scope must be bid. | ZD čl. 2; TS 1–7; SoD 1.1; SoD-P1 | — | — |
| R60 | Technical scope | **Backend (.NET REST API) and infrastructure changes are done by the authority's team.** The supplier delivers the FE and writes the backend change specification. | VZD 1 Ad 2 | New via VZD 1. | Yes. A dependency on the authority's team, with no SLA for its cooperation in the SoD (VZD 2 Q2 unanswered). The .NET 7 upgrade question was not explicitly answered. |
| R61 | Technical scope | **Core Web Vitals targets are an acceptance condition**: LCP p75 < 1 400 ms; INP > 80 % < 200 ms **or** 75 % < 150 ms; CLS p75 ≤ 0.05. Measured on **CrUX real-user data for the whole origin**. **Third-party scripts count.** | TS 3.7, 4.7; VZD 1 Ad 3 | VZD 1 Ad 3 turns "metrics" into acceptance conditions. TS 3.12.2/4.12.2 only require documenting before/after. | Yes. This is the biggest one. Reading only the TS acceptance criteria suggests documenting a before/after measurement is enough. Methodology questions (VZD 2 Q1) are still unanswered. |
| R62 | Technical scope | Project 1, Phase 7: **closed list** of third-party services: CookieHub; PPC (Google Ads, Microsoft Ads, Sklik); Meta / Facebook Pixel; Criteo; RTB House; Boldem; Heureka; Vendor Pixel Kingston; Commerce-Connector (Wayvia); GetHatch (Wayvia); SmartForm, SmartSupp. | VZD 1 Ad 9; SoD-upd P1 (GA, Fáze 7) | Changed by VZD 1 + SoD-upd. The open items "Ostatní měřící platformy" and "Partneři a Afilliate" were removed, and RTB House, Kingston, Commerce-Connector and GetHatch were added. | Yes. **TS (Příloha 3) was not re-issued** and still shows the old open list, so it is inconsistent with SoD-upd annex 1. |
| R63 | Technical scope | "Administrační část webu" (TS project 2 = mobile Redesign, Figma screen list) = the customer-account area: Objednávky, Faktury, Reklamace a vrácení, Zakoupené zboží a záruky, Hodnocení, Licence, Hlídací psi, Oblíbené, Můj účet, Dodací adresy, Disponentní účty. | VZD 1 Ad 8; TS 2 | Clarified by VZD 1. | Yes. That is 11 extra screen groups in Figma plus FE. |
| R64 | Technical scope | Current state given: Next.js 14.2.30, React 18.2.0, 25 pages, 35 API routes (60 routes in total), 16 global Context Providers, i18next 23.10.1 (JSON locales), 16 UI tests, 0 e2e, 0 component tests, 11 unit tests. **No source-code access before bidding.** | VZD 1 Ad 4; TS "Současný technický stack" | New via VZD 1. | Yes. Fixed price on code nobody can inspect, with almost no test coverage. |
| R65 | Technical scope | P1 and P2 each have an **analytic phase with separate acceptance** (architecture, cache, BFF, refined estimate, Azure DevOps breakdown, risks). Work is managed in **Azure DevOps**, Scrum or Kanban. | TS 3.9, 3.11, 3.12.1, 4.9, 4.11, 4.12.1 | — | — |
| R66 | Technical scope | No production downtime. The new App Router runs alongside the Pages Router. Infrastructure demands may not increase without approval. Cart must not be slower than today. | TS 3 intro, 3.7, 4.7, 5.5 | — | — |
| R67 | Formal | Grant-related: the authority may cancel the procedure. Results and exclusions are published on the profile and deemed delivered on publication (Pravidla 7.4.2). No reimbursement of bid costs. | ZD čl. 12 (p. 5) | — | Yes. You must monitor the profile, because there are no individual notices. |
| R68 | Technical scope | VZD 3: the e-shop is "plně integrován se stávajícím EPR [sic] systémem". | VZD 3 (20. 11. 2026) | New. | Low relevance. It was a vendor sales e-mail answered as a clarification. |

---

## 2. Changes over time

### 2.1 Timeline (dates as stated in the documents; publication times from zdlist.html)

| Date | Event |
|---|---|
| (TS file dated 3. 7. 2026; FN/SoD/OU files dated 22. 9. 2026) | Annex drafts |
| 1. 10. 2026 | ZD signed (Pešák) |
| 2. 10. 2026 20:30 | ZD and annexes published on the profile |
| 5. 10. 2026 | Clarification request 1 received (12 questions) |
| 19. 10. 2026 (published 18:15) | **VZD 1**: answers, SoD-upd and OU-upd. Deadline moved from 2. 11. to **20. 11. 2026 10:00**. |
| 12. 11. 2026 | Clarification request 2 received (6 topic blocks) |
| 19. 11. 2026 (signed 17:25, published 20. 11. 08:58) | **VZD 2**: no answers, deadline moved to **27. 11. 2026 10:00**. Answers are promised later. Signed by P. Prikrt (technical director), not by the chairman. |
| 19. 11. 2026 | Request 3 received (vendor sales e-mail) |
| 20. 11. 2026 (signed 17:31, published 18:15) | **VZD 3**: one-line answer about the ERP |

### 2.2 SoD: original (22. 9.) vs aktualizovaná (19. 10.). Paragraph-level diff; only 4 hunks differ.

1. **čl. 6.2.1 Licence: "výhradní" deleted.** Original: "výhradní licenci k veškerým známým způsobům užití Díla…". Updated: "licenci k veškerým známým způsobům užití Díla…".
2. **New čl. 6.3–6.6 (licence split).** 6.3 gives an exclusive licence for parts created solely for the authority. 6.4 gives a non-exclusive licence for standard modules, libraries, frameworks, tools and pre-existing works of the contractor or third parties, with a minimum scope (unlimited use, modification, development, integration, copies, third-party support, transfer to successors) and no further licence, service or similar fees. 6.5 requires a list of non-exclusive components (rights holder, licence terms, scope) at handover at the latest. 6.6 bans components or licence terms that would prevent maintenance, modification, development or migration without the contractor. (This implements VZD 1 Ad 12 b.)
3. **New čl. 7.7 liability cap:** total liability for all damage, penalties and other sanctions is capped at **8 000 000 Kč**, except intent or gross negligence. (Implements VZD 1 Ad 12 a.)
4. **Annex 1, GA project, Fáze 7 "Služby třetích stran":** "Facebook" became "Meta / Facebook Pixel"; **added** RTB House, Vendor Pixel Kingston, Commerce-Connector (Wayvia), GetHatch (Wayvia); **removed** "Ostatní měřící platformy" and "Partneři a Afilliate". (Implements VZD 1 Ad 9.)

**Unchanged:** price and payment terms, retention 10 %, penalties (0.1 %/day, 2 000 Kč/day, 10 000 Kč/30 days), deadline 30. 6. 2027 / 31. 12. 2027, insurance 8 M, handover (still no acceptance deadline), annex 2 structure.
Side note (not a VZD change): SoD annex 1 vs TS PDF differ only in typography, plus "open-source projekty" before "Zustand, Redux" (TS 4.5). After 19. 10. the **TS PDF still carries the old third-party list** and was not re-issued.

### 2.3 OU: original (22. 9.) vs aktualizovaná (19. 10.)

- The **only substantive change**: in every technology checklist (SFD × 5, UXS × 5, SNA × 5, DevOps × 5 references) the instruction adds "pokud [role] namísto zde uvedené technologie použil jinou rovnocennou technologii, uveďte do závorky v odpovídajícím řádku název takové rovnocenné technologie", and each technology line gets an empty "( )". This implements VZD 1 Ad 10.
- Not changed: role thresholds (PM ≥ 6 M, others ≥ 3 M), 8-year window, the technology lists themselves, the 5 references per role, the PM section (no technology list).
- Minor inconsistency in both versions: OU calls the procedure "Otevřené řízení podle Pravidel…", while ZD calls it "otevřená výzva".

### 2.4 Changes made by clarification text alone (no annex change)

- ZD čl. 6: "alespoň 1 referenční zakázka" is **corrected to 3** (VZD 1 Ad 5).
- ZD čl. 10/11: deadline and opening moved twice (VZD 1, VZD 2).
- Reference value = whole contract value; ongoing references accepted under conditions (VZD 1 Ad 1).
- Backend and infrastructure are out of the supplier's scope (VZD 1 Ad 2).
- CWV targets are acceptance conditions on CrUX origin-level data, including third-party scripts (VZD 1 Ad 3).
- "Administrační část webu" defined (VZD 1 Ad 8).
- Paper-only submission confirmed (VZD 1 Ad 11).

---

## 3. Q&A from clarifications

### VZD 1 (dated 19. 10. 2026; request received 5. 10. 2026)

| # | Question (summary) | Authority's answer (summary) |
|---|---|---|
| 1 | Can ongoing long-term cooperation count as a reference? Is go-live the completion date? Does the same apply to OU (8 years)? Is the value the whole contract or the person's share? | Completed references within 5 years are accepted. Ongoing ones are accepted if the app (or a complete functional part) was officially handed over or put live within the window and its **paid** value met the minimum at that time. Use the handover or go-live date. The same logic applies to OU, which must still meet the OU conditions. References with no complete functional part delivered are not accepted. **Value = whole contract, not the person's share.** |
| 2 | Are backend (.NET REST API) and infrastructure changes for projects 5 and 6 in scope? Is the .NET 7 upgrade in scope? | Backend and infrastructure changes **are done by the authority's team**. The supplier does the FE and writes the backend change specification. (The .NET upgrade is not explicitly addressed.) |
| 3 | Are the LCP/INP/CLS targets an acceptance condition, or only before/after measurement? Which tool and data? Impact of third-party code? | **Targets are an acceptance condition.** Measured on public **CrUX** real-user data for the **whole origin**. Project 1 should move the metrics significantly. **Third-party code counts.** |
| 4 | Basic app data or read-only code access under NDA? | Data given (Next.js 14.2.30, React 18.2.0, 25 pages, 35 API routes, 60 routes, 16 context providers, i18next 23.10.1, UI tests 16, e2e 0, component 0, unit 11). **No source-code access.** |
| 5 | ZD čl. 6 says 1 reference, FN says 3 × 4 M. Which is binding? | ZD čl. 6 is **wrong**. **3 references** per FN. |
| 6 | Who sets the project order? | The contractor proposes the schedule and order (SoD 3.3.1). The authority approves or comments and has the final say. |
| 7 | Can accepted analytic phases (P1/P2) or sub-phases be invoiced separately? | Invoicing per SoD 4.4, by parts per annex 2 minus retention. Smaller parts are possible only by agreement (SoD 5.2). |
| 8 | What is "Administrační část webu" in the redesign? | Customer account and purchases: Objednávky, Faktury, Reklamace a vrácení, Zakoupené zboží a záruky, Hodnocení, Licence, Hlídací psi, Oblíbené, Můj účet, Dodací adresy, Disponentní účty. |
| 9 | Can the third-party list (project 1, phase 7) be closed? | Yes. The closed list is given (see R62). |
| 10 | OU scores specific products without "or equivalent". Will equivalents count? | The scoring of specific products is lawful (PpVD 5.2.5 concerns technical conditions, not evaluation). **Equivalents are nonetheless allowed**: check the item, note the equivalent, and the committee judges equivalence. |
| 11 | Can bids be submitted via NEN? | **No. Paper only** (ZD čl. 4, 10). |
| 12a | Liability and penalty cap? | **8 000 000 Kč** cap on liability (except intent or gross negligence), which also caps total penalties. Implemented as SoD-upd 7.7. |
| 12b | Does the exclusive licence cover pre-existing tools and third-party software? | A non-exclusive licence for those parts is acceptable if it does not limit use or modification, needs no future payments and does not affect ownership. Implemented as SoD-upd 6.3–6.6. |
| 12c | Maximum acceptance period? Do minor defects block acceptance? | See SoD 5.3. The authority decides case by case and will probably accept minor defects that do not block use. **No acceptance deadline is set.** |
| — | (Own initiative) | Deadline moved to **20. 11. 2026 10:00**. Opening immediately after. Attachments: OU-upd, SoD-upd. |

### VZD 2 (dated 19. 11. 2026; request received 12. 11. 2026; published 20. 11. 2026 08:58)

The questions cover 6 blocks:
1. CWV acceptance methodology: baseline values, CrUX source and URL (tsbohemia.cz vs www), mobile/desktop, all metrics at once, INP alternative, 28-day window timing, P1 vs P2, changes by the authority or third parties, third-party responsibility, RUM/lab evidence, request to soften the criterion.
2. The authority's cooperation: deadlines, schedule dependencies, blocking, automatic extension, no penalties, extra costs.
3. Unforeseeable technical state (no code access, fixed price): a change mechanism per Pravidla 7.2.4 / 7.2.7.
4. Acceptance deadlines: e.g. 10 working days, acceptance with minor defects, inaction by the authority.
5. The extension to 31. 12. 2027: contractor's right? Grant provider pre-agreed? Delays caused by the authority without grant extension?
6. Request for amendments and a further extension per Pravidla 5.3.5.

**Answer:** the authority is working on the answers but cannot give them now. The **deadline is extended to 27. 11. 2026 10:00**, answers will be published once prepared, and opening follows immediately after the deadline. **No substantive answers are in the provided documents.**

### VZD 3 (dated 20. 11. 2026; request received 19. 11. 2026)

- Question: an e-mail from a vendor's sales contact asking whether follow-up work covers linking the e-shop to stock availability and orders, and who leads it.
- Answer: the e-shop is "plně integrován se stávajícím EPR systémem zadavatele".

---

## 4. Open questions a bidder should still ask (opinion)

*Labelled as opinion. As of 25. 11. 2026, the request deadline under ZD čl. 9 (≥ 4 working days before 27. 11.) has passed, so these are risk items to price or to raise via the authority, not guaranteed answers.*

1. **All of VZD 2 is unanswered.** Will answers be published before 27. 11. 10:00? If they materially change conditions, will there be another extension? The most important: CWV acceptance methodology (VZD 2 Q1) and acceptance deadlines (Q4).
2. **CWV acceptance at origin level** with third-party scripts and backend outside the supplier's control. In my view this is the single largest unpriceable risk: it ties acceptance, and with it invoicing and retention, to factors the supplier does not control.
3. **.NET 7 upgrade:** VZD 1 Ad 2 does not explicitly say whether it is in or out of scope.
4. **Cooperation SLA:** no deadlines for the authority's backend team (SoD 2.2 is generic), while milestone penalties (7.3) run.
5. **Warranty:** the SoD has no warranty clause or post-acceptance defect-fixing period. It is unclear whether statutory rules apply only, and how this relates to ad-hoc MD-rate service work (annex 2).
6. **TS vs SoD-upd inconsistency** on the third-party list (TS 1.3 Fáze 7 was not re-issued). Presumably SoD-upd and VZD 1 Ad 9 prevail, but this is not stated.
7. **Reference start date:** the "zahájení výběrového řízení" date for the 5-year and 8-year windows is not stated. Presumably publication on 2. 10. 2026 (zdlist.html).
8. **Retention release** only after the last defect of the whole Dílo is fixed. Could it be released per project?
9. **P2 estimate 80–130 MD:** is it indicative only, or a cap relevant to change requests? There is no estimate for P1 or the other projects.
10. **Partial withdrawal (SoD 9.3):** how does it interact with a fixed-price bid if the authority drops later projects?

---

## 5. Claim checks

| Claim | Verdict | Source and nuance |
|---|---|---|
| (a) 3 e-commerce references of ≥ 4 M CZK each in the last 5 years | **TRUE** (with precision) | FN "Technická kvalifikace – referenční zakázky": ≥ 3 references, web app "v oblasti e-commerce", ≥ 4 000 000 Kč **bez DPH** each, performed within 5 years **before the procedure started**. ZD čl. 6 says "alespoň 1", which VZD 1 Ad 5 says is wrong: 3 apply. Ongoing contracts are accepted only under VZD 1 Ad 1. |
| (b) Penalties 0.1 %/day | **PARTLY TRUE** | 0.1 % of **Cena Díla bez DPH** per started day applies **only** to missing the final deadline (SoD 7.2). Milestone delay is **2 000 Kč/day** (7.3); team breach is **10 000 Kč per role per 30 days** (7.4). The authority's late-payment interest is also 0.1 %/day (7.1). Everything is capped at 8 M Kč (7.7, SoD-upd only). |
| (c) 10 % retention | **TRUE** | SoD 4.9.1: 10 % from **each** invoiced part, held until the last defect in the final handover protocol for the **whole** Dílo is removed (or the SoD ends). |
| (d) Deadline extended to 27. 11. 2026 10:00 | **TRUE** | VZD 2 (dated 19. 11. 2026). Chain: 2. 11. 2026 10:00 (ZD čl. 10), then 20. 11. 2026 10:00 (VZD 1), then 27. 11. 2026 10:00 (VZD 2). |
| (e) Delivery by 30. 6. 2027 | **TRUE** (with nuance) | SoD 3.1 "nejpozději do 30. 6. 2027" (ZD čl. 7: "předpokládaná doba plnění do 30. 6. 2027"). The authority alone may extend to 31. 12. 2027 if the grant provider approves **and** the authority has operational reasons (SoD 3.2). |
| (f) Evaluation price 70 % / team expertise 30 %, max 97.5 points | **TRUE for 70/30; MISLEADING for 97.5** | ZD čl. 3; FN. 97.5 is the **raw point maximum of the team-expertise sub-criterion** before conversion: (pts / 97.5) × 100 × 0.3 (ZD čl. 3.2 f). The overall maximum is **100 points** (ZD čl. 3.3). |
| (g) Lower price prevails if form and contract differ | **TRUE** | ZD čl. 5: "V případě rozporu … bude za správnou považována ta nižší z nabídkových cen." |
| (h) Paper submission in envelope marked "NEOTEVÍRAT" | **TRUE** (incomplete) | ZD čl. 4: sealed envelope with the **tender name** and "NEOTEVÍRAT". Paper only, confirmed by VZD 1 Ad 11. An electronic copy on CD/DVD/USB must be inside, and the SoD goes in 3 copies (2 removable). |
