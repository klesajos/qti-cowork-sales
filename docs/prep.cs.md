> 🌍 Read this in: [English](prep.md) | **Česky**

# Příprava na workshop

## Účastníci: den předem (10 min)

1. Nainstalujte **desktopovou aplikaci Claude** a přihlaste se účtem Quanti.
2. Nainstalujte písmo **Montserrat**: dvojklik na každý `sample-data/brand/fonts/Montserrat-*.ttf`
   (4 soubory) → Instalovat. Bez něj PowerPoint a Word zobrazí prezentace v náhradním písmu.
3. Rozbalte balíček workshopu, který jste dostali (`qti-cowork-sales.zip`), do
   `~/Documents/qti-cowork-sales`.
4. V Claude otevřete **Settings → Plugins** a zkontrolujte, že tam je `quanti-sales`. Pokud
   ne, řekněte lektorovi; nahrajete ho ve cvičení 0.
5. Mějte po ruce PowerPoint, Word a Excel (nebo Keynote, Pages, Numbers) na otevření výstupů.
6. Připojte HubSpot: v Claude **Plugins → HubSpot → Connect** a přihlaste se svým účtem do
   HubSpotu. Vyberte si jeden svůj otevřený deal s aspoň jedním zalogovaným e-mailem nebo
   hovorem na cvičení 9.

## Lektor: před workshopem

- [ ] **Vlastník organizace:** Organization settings → zapnout Cowork a Skills (pluginy
      potřebují obojí).
- [ ] **Vlastník organizace:** Organization settings → Plugins & skills → Add → Upload a plugin →
      `dist/quanti-sales.zip`; pro skupinu účastníků nastavit *Installed by default*.
- [ ] **Jen Enterprise:** design systémy jsou vypnuté, dokud je nezapnete v Organization
      settings → Artifacts. Rozhodněte, kdo smí design systém *publikovat*; na workshopu ho
      účastníci vytvoří, ale nepublikují.
- [ ] Volitelně: nainstalujte z katalogu plugin `brand-voice` od Anthropicu pro cvičení 1.
- [ ] **HubSpot:** HubSpot konektor je pro organizaci povolený; účastníci smí upravovat své
      dealy (zápis ve cvičení 9). Ukázka lektora běží na `sample-data/hubspot/` a práva
      v HubSpotu nepotřebuje.
- [ ] Repozitář je privátní. Pošlete účastníkům zip: `git archive -o qti-cowork-sales.zip
      --prefix=qti-cowork-sales/ HEAD`, nebo je přidejte jako spolupracovníky.
- [ ] Projděte si zkušební běh sami (aspoň cvičení 0, 3, 6). Poslední zaznamenaný běh je ve
      [screenshots/](screenshots/README.md).
- [ ] Zkontrolujte zakázku na [NEN](https://nen.nipez.cz/verejne-zakazky/detail-zakazky/N006-26-V00032057):
      nová vysvětlení mění klíč v `solutions/tender-answer-key.md`. Po lhůtě zůstává zakázka
      platným cvičením; řekněte to místnosti.
- [ ] `solutions/` sdílejte až po cvičeních.

## Známé pasti

| Příznak | Příčina | Oprava |
|---|---|---|
| Odpovědi o brandu jsou obecné | Plugin není nainstalovaný nebo je vypnutý | Settings → Plugins; nebo skill jmenujte: „Použij skill quanti-brand“ |
| Prezentace se otevře v Arialu/Calibri | Montserrat není na tomto počítači | Nainstalujte písmo (krok 2) |
| Claude se pokaždé ptá na přístup ke složce | Nová konverzace, složka není povolená | Na začátku každé konverzace povolte `sample-data` |
| Celková cena nabídky se mezi běhy liší | Odhad (MD) je úsudek, výpočet ne | Porovnávejte tabulku MD, ne jen součet; přepočítejte jeden řádek |
| Matice zakázky nemá prodlouženou lhůtu | Nepřečtená vysvětlení nebo staré přílohy | Dejte Claude celou složku `tender/` a chtějte nejdřív soupis dokumentů |
| Slidy se zastaví na „Allow Claude to copy files into this artifact?“ | Režim oprávnění *Manual*: zkopírování tokenů design systému do prezentace chce kliknutí | Stiskněte **Allow once**, nebo přepněte konverzaci na *Auto* |
