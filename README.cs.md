> 🌍 Read this in: [English](README.md) | **Česky**

# Quanti sales × Claude Cowork

Půldenní (4 h) praktický workshop pro obchodní tým Quanti. Na konci každý umí:

1. **Držet brand**: Claude zná barvy, písmo, logo a tón Quanti a používá je ve všem, co vyrobí.
2. **Dělat prezentace**: klientskou prezentaci v PPTX z poptávky a kontrolu prezentace mimo brand.
3. **Psát nabídky**: naceněnou nabídku v DOCX z e-mailu klienta a ceníku, bez vymyšlených čísel.
4. **Kontrolovat požadavky výběrového řízení**: matici požadavků ze skutečné veřejné zakázky,
   go/no-go a kontrolu rozpracované nabídky.

Vše běží v Claude (Cowork) s jedním pluginem `quanti-sales`, který obsahuje brand a tři
pracovní postupy jako skilly.

## Co je v repozitáři

| Cesta | Co to je |
|---|---|
| [`docs/`](docs/README.cs.md) | Průvodci, cvičení, příprava, poznámky pro lektora (CS + EN) |
| [`plugins/quanti-sales/`](plugins/quanti-sales) | Plugin: skilly `quanti-brand`, `quanti-offer`, `deck-review`, `tender-check` |
| [`dist/quanti-sales.zip`](dist/quanti-sales.zip) | Plugin připravený k nahrání do Claude |
| [`sample-data/`](sample-data) | Brand podklady, korpus textů, fiktivní poptávka a ceník, prezentace mimo brand, skutečná zakázka z NEN |
| [`solutions/`](solutions) | Klíče řešení pro lektora |
| [`scripts/`](scripts) | `build-plugin.sh` (zabalí plugin), generátory ukázkových dat |

## Program (4 h)

| Čas | Blok | Cvičení |
|---|---|---|
| 0:00 | Úvod, nastavení | 0 |
| 0:20 | Brand: tón a design systém | 1, 2 |
| 1:00 | Prezentace | 3, 4 |
| 1:45 | *Přestávka* | |
| 2:00 | Nabídky | 5 |
| 2:40 | Výběrová řízení | 6, 7 |
| 3:35 | Vlastní postup jako skill, závěr | 8 |

Začněte v [docs/README.cs.md](docs/README.cs.md). Lektoři nejdřív [docs/prep.cs.md](docs/prep.cs.md).

## Data a zdroje

- Hodnoty brandu jsou z QUANTI Brand manuálu 2024 (`sample-data/brand/`); soubory loga jsou
  z quanti.cz. Montserrat je pod licencí SIL Open Font License (`sample-data/brand/fonts/OFL.txt`).
- Korpus textů jsou veřejné texty z quanti.cz (blog, reference, služby), bez kontaktů na kolegy.
- Klient „Bylinkárna Vltava“ a ceník jsou **fiktivní**.
- Zakázka je veřejná: T.S.BOHEMIA a.s., *Technická modernizace a optimalizace webové aplikace
  tsbohemia.cz*, [NEN N006/26/V00032057](https://nen.nipez.cz/verejne-zakazky/detail-zakazky/N006-26-V00032057).
