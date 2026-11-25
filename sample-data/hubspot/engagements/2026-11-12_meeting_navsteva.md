---
type: MEETING
date: 2026-11-12 10:00–12:00
place: sklad Praha-Hostivař
attendees: Petr Dvořák (IT manažer), Jana Horáková (část), za Quanti: obchodník
---

## Zápis

- ERP **Money S5**, verze 2025, modul Money S5 API je aktivní (REST), používá ho dnes jen
  pokladní systém. Sklady 3 (Hostivař, Brno, Plzeň), 9 000 aktivních SKU, ceníky B2C + 3× B2B.
- Synchronizace: stav skladu a ceny chtějí každých 15 minut, objednávky z e-shopu do ERP ihned,
  faktury vznikají v ERP.
- Špička: 600 objednávek/den v listopadu a prosinci, mimo sezónu 150–200.
- Shoptet: data o zákaznících a objednávkách za 6 let chtějí převést (export CSV/API).
- Věrnostní karty: čísla karet jsou v pokladním systému, ne v ERP; propojení přes Money S5 API
  nebo přímo s pokladnou (dodavatel pokladny zatím neodpověděl).
- GDPR: souhlasy k věrnostnímu programu jsou papírové; Petr chce, aby nový program měl souhlas
  řešený digitálně.
- Hosting: preferují data v ČR nebo EU; dnes Shoptet cloud.
- Petr má obavu z kapacity svého týmu (2 lidé) při migraci; čeká, že integrace bude naše.

Otevřené: dodavatel pokladny, rozsah migrace dat ze Shoptetu, kdo spravuje obsah po spuštění.
