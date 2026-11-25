> 🌍 Read this in: [English](README.md) | **Česky**

# Podklady k workshopu

| # | Průvodce | Stručně |
|---|---|---|
| 01 | [Nastavení](01-setup.cs.md) | Cowork, plugin, pracovní složka |
| 02 | [Brand](02-brand.cs.md) | Tón z textů, design systém z podkladů, skill `quanti-brand` |
| 03 | [Prezentace](03-decks.cs.md) | Prezentace z poptávky; kontrola a oprava prezentace mimo brand |
| 04 | [Nabídky](04-offers.cs.md) | Poptávka + ceník → naceněné DOCX, bez vymyšlených čísel |
| 05 | [Výběrová řízení](05-tenders.cs.md) | Matice požadavků, vysvětlení, go/no-go, kontrola rozpracované nabídky |
| 06 | [Vlastní skill](06-own-skill.cs.md) | Z opakované práce skill; nasazení pro celý tým |
| 07 | [HubSpot](07-hubspot.cs.md) | Obchodní brief z dealu přes HubSpot konektor; nabídka zapsaná zpět |

- [Cvičení](exercises.cs.md): prompty a „Hotovo, když“ ke každému cvičení.
- [Příprava](prep.cs.md): účastníci den předem, lektor před workshopem.
- [Tahák](cheatsheet.cs.md): jedna stránka, kterou máte otevřenou.
- [Snímky](screenshots/README.md): poslední zkušební běh.

## Jak to do sebe zapadá

```
Vy ── prompt ──▶ Claude (Cowork, pracovní složka na vašem Macu)
                   │
                   ├─ skill quanti-brand   ← načte se, když výstup uvidí klient
                   ├─ skill quanti-offer   ← „nabídka“, „kalkulace“
                   ├─ skill deck-review    ← „zkontroluj prezentaci“
                   ├─ skill tender-check   ← „zadávací dokumentace“, „go/no-go“
                    ├─ skill deal-brief     ← „podklady k dealu“, „zapiš do HubSpotu“ (HubSpot konektor)
                   └─ vestavěné souborové skilly (pptx, docx, xlsx, pdf) zapisují soubory
```

**Skill** je složka se souborem `SKILL.md`: popis (kdy ho použít) a instrukce (jak). Claude
předem čte jen popisy a celé instrukce načte, až když požadavek odpovídá. **Plugin** balí skilly
dohromady, aby celý tým měl stejné.
