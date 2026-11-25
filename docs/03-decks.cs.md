> 🌍 Read this in: [English](03-decks.md) | **Česky**

# 03 · Prezentace

K prezentaci vedou dvě cesty. Vyberte podle toho, kam půjde dál:

| Cesta | Výstup | Kdy |
|---|---|---|
| **Cowork + skill pptx** | Soubor `.pptx` ve vaší složce | Prezentace, které budete upravovat v PowerPointu, posílat jako soubor nebo používat jako šablonu |
| **Claude Slides** | Slidový artefakt; export do PPTX nebo PDF | Rychlé vizuální návrhy, úpravy živě s Claude, prezentace z publikovaného design systému |

Obě drží brand: Cowork přes skill `quanti-brand`, Slides přes publikovaný design systém.

## Prezentace z poptávky

Dobrý prompt říká: pro koho, cíl schůzky, počet slidů, strukturu, zdrojové soubory a název
souboru. Claude pak prezentaci postaví na **oficiální šabloně PowerPointu**
(`brand/templates/Quanti_PPT_Template_CZ.potx`, anglická verze vedle): 26 rozvržení a 46
ukázkových slidů s grafy, Gantty, časovými osami, organigramy a tabulkami v barvách brandu.
Zduplikuje rozvržení a ukázkové slidy, které potřebuje, nahradí jejich text a data a firemní
slidy („Kdo jsme“, reference, „Kontakt“) zkopíruje z **intro prezentace**
`decks/Quanti_intro_2026_CZ.pptx`, místo aby je psal znovu. Pak soubor zvaliduje proti šabloně
a vyrenderuje každý slide.

Dva soubory, které je dobré znát:

| Soubor | Co to je | Pravidlo |
|---|---|---|
| `brand/templates/Quanti_PPT_Template_CZ.potx` (+ `_ENG`) | Oficiální šablona: rozvržení, grafy, diagramy, tabulky, ikony | Každá prezentace začíná tady; ukázkové slidy se duplikují, ne kreslí znovu |
| `decks/Quanti_intro_2026_CZ.pptx` | Schválená firemní prezentace: fakta, služby, certifikace, 30 referencí, pobočky | Slidy se kopírují; čísla jen odsud nebo z `approved-claims.md` |

Obchodní struktura, která funguje na první schůzku:
1. Titulní: klient, téma, datum.
2. Vaše situace: jejich problém jejich slovy (citace z poptávky).
3. Co navrhujeme: tři výsledky, ne technologie.
4. Jak bychom postupovali: fáze a jedno datum, na kterém jim záleží.
5. Proč Quanti: dvě tři relevantní reference ze schválených tvrzení.
6. Další krok: jedna konkrétní akce s datem.

## Kontrola prezentace

`deck-review` čte samotný soubor, ne jeho obrázek: u každého tvaru vypíše použité barvy
a písma, takže chytí nadpis v Calibri nebo výplň `#1F4E9C`, která vypadá „skoro správně“. Pak
zkontroluje obchodní strukturu. O opravu požádejte, až si přečtete zprávu; oprava zachová obsah
a uloží nový soubor `_opraveno`.

## Typické chyby, které zkontrolujte sami

- Text přetékající z rámečku (Claude kontroluje render, ale podívejte se i vy).
- Montserrat není nainstalovaný na počítači, kde se soubor otevře: PowerPoint použije jiné
  písmo. Nainstalujte ho ze `sample-data/brand/fonts/` nebo při exportu vložte písma.
- Tvrzení, které zní správně, ale není v `approved-claims.md`.
