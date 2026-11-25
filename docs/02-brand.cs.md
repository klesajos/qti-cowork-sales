> 🌍 Read this in: [English](02-brand.md) | **Česky**

# 02 · Brand: tón a vizuální identita

Brand v Claude žije na třech místech. Vězte, co dělá které:

| Kde | Co obsahuje | Kdo ho nastavuje | Kdo ho používá |
|---|---|---|---|
| Skill `quanti-brand` (plugin) | Barvy, písmo, pravidla loga, tón, pravidla pro tvrzení, závěrečná kontrola | Vedoucí obchodu, jednou; je součástí pluginu | Každý soubor, který Claude v Coworku vytvoří: PPTX, DOCX, XLSX, PDF |
| **Design systém** (Settings → Capabilities → Design systems) | Vizuální styly vytažené z podkladů | Kdo vlastní brand; *Published* z něj udělá výchozí pro organizaci | Claude Slides, Claude Design a HTML artefakty |
| Soubory v projektu nebo konverzaci | Brand brief, loga, korpus textů | Kdokoli | Jen ten projekt nebo konverzace |

Skill je jediná sada pravidel, která jde s každým úkolem. Design systém zajistí, že vizuální
nástroje (Slides, artefakty) začínají v brandu. Obojí udržujte z jednoho zdroje,
`sample-data/brand/tokens.json`.

## Tón ze skutečných textů

`sample-data/tone-corpus/` obsahuje 58 veřejných textů z quanti.cz (blog, reference, služby).
To stačí, aby Claude popsal, jak Quanti píše, s citacemi jako důkazem, místo aby tón vymýšlel.
Plugin `brand-voice` z katalogu Anthropicu (skilly `discover-brand`, `guideline-generation`,
`brand-voice-enforcement`) to umí automaticky nad Notionem, Drive nebo Confluence; nad
obyčejnými soubory stačí prompt.

Na co se ve výsledku dívat: konkrétní dvojice „ano / ne“, citace z korpusu a slova, kterým se
vyhnout. Pak to porovnejte s tónem ve skillu `quanti-brand` a skill vylepšete.

## Design systém z podkladů

Nahrajte brand manuál v PDF, `brand-brief.md`, `tokens.json`, obě loga a písma Montserrat.
Claude vytáhne barvy, písmo a komponenty a ukáže náhled. Před publikováním náhled porovnejte
s manuálem: nadpisy verzálkami, zaoblené karty místo panelu se seříznutými rohy, logo jinde než
vpravo dole a výchozí písmo jsou typické chyby prvního běhu.

> Samostatný Claude Design (claude.ai/design) končí **14. 12. 2026**. Design systémy zůstávají
> v Settings → Capabilities → Design systems; na plánu Enterprise je musí admin nejdřív zapnout
> (Organization settings → Artifacts).

## Pravidlo pro tvrzení

Největší brandové riziko v obchodě není špatná barva, ale číslo, které nikdo nedoloží. Skill
povoluje čísla, klienty a certifikáty jen ze vstupů úkolu nebo z `approved-claims.md`, jinak
napíše `[DOPLNIT: …]`. Počítejte s těmito značkami; jsou to záměr, ne chyba.
