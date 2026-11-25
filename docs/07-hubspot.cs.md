> 🌍 Read this in: [English](07-hubspot.md) | **Česky**

# 07 · HubSpot: od dealu k nabídce a zpět

CRM Quanti je HubSpot. V Claude dává **HubSpot konektor** (Plugins → HubSpot → Connect, s vaším
vlastním přihlášením do HubSpotu) Claude přístup k firmám, kontaktům, dealům a všem zalogovaným
aktivitám, a po vašem potvrzení umí zapsat poznámku, úkol a posun fáze. Skill `deal-brief` z toho
dělá obchodní postup.

## Co skill dělá

1. **Sesbírá**: deal, jeho firmu a kontakty a všechny aktivity od nejstarší (e-maily, hovory,
   schůzky, poznámky, úkoly). Plné texty, ne shrnutí.
2. **Brief**: jedna strana česky: klient v kostce, lidé a role, časová osa, požadavky se zdroji,
   termíny (novější zdroj vítězí, oba se ukážou), rozpočet vs. náš odhad, konkurence, rozpory,
   rizika, další krok. Mezery jsou `[DOPLNIT]`, nikdy odhad.
3. **Předá** skillu `quanti-offer` (nabídka) nebo `quanti-brand` (prezentace).
4. **Zapíše zpět**: poznámku, úkol na follow-up a posun fáze, každé za potvrzovací tabulkou
   konektoru. Nikdy Closed Won/Lost, nikdy e-maily z HubSpotu.

## Dva způsoby, jak to pustit

| | Ukázka facilitátora | Účastníci |
|---|---|---|
| Data | `sample-data/hubspot/`: export fiktivního dealu Bylinkárna Vltava ve tvaru, jaký vrací konektor | Vlastní otevřený deal přes konektor |
| Prompt | „…ve složce hubspot/“ | „…v HubSpotu“ |
| Zápis zpět | Nejde (bez práva zápisu): Claude dá text poznámky k vložení | Skutečný, s potvrzením |
| Klíč | `solutions/deal-brief-key.md` | Žádný; porovnejte s tím, co o dealu víte |

## Na co si dát pozor

- **Zdroj u každého faktu.** Brief bez „(e-mail 18. 11.)“ za datem je odhad.
- **Novější vítězí.** V exportu jsou dva e-maily s termíny; brief musí ukázat oba a použít
  novější.
- **Slova klienta vs. naše poznámky.** Částka dealu v HubSpotu je obvykle první odhad
  obchodníka; brief to musí říct.
- **Potvrzení před zápisem.** Claude ukáže tabulku (objekt, vlastnost, stará hodnota, nová
  hodnota). Přečtěte ji; špatný posun fáze vidí celý tým.
- **Osobní údaje.** Jen jména, role a pracovní e-maily. Soukromé poznámky o lidech zůstávají v CRM.

## Co je potřeba

- HubSpot konektor připojený v Claude (účastníci den předem, viz [přípravu](prep.cs.md)).
- Právo upravovat dealy v HubSpotu pro část se zápisem. Bez něj funguje aspoň čtení.
- Vlastní deal s aspoň jedním zalogovaným e-mailem nebo hovorem. Kdo žádný nemá, vezme deal
  kolegy jen pro čtení a zápis vynechá.
