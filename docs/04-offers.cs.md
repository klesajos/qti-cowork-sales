> 🌍 Read this in: [English](04-offers.md) | **Česky**

# 04 · Nabídky

V nabídce stojí špatné číslo skutečné peníze. Skill `quanti-offer` je postavený kolem toho:

1. **Nejdřív vstupy.** Claude vypíše, co má (poptávku, ceník, vaše poznámky), a bez ceníku se
   zastaví. Sazby nikdy neodhaduje.
2. **Odhad před cenou.** Člověkodny (MD) po rolích a fázích s předpoklady, pak cena.
3. **Výpočty kódem.** MD × sazba, pravidla z ceníku (procenta PM a QA, rezerva na rizika),
   DPH: počítá Python, ne model „z hlavy“.
4. **Tvrzení jen ze zdrojů.** Reference a čísla z poptávky nebo `approved-claims.md`; vše
   ostatní je `[DOPLNIT: …]`.
5. **Brand.** `quanti-brand` určuje vzhled DOCX i formulace.
6. **Předávací zpráva.** Celková cena a jak vznikla, otevřené `[DOPLNIT]`, předpoklady, které
   mění cenu, části poptávky bez odpovědi.

## Vaše role

Claude píše návrh; za nabídku odpovídáte vy. Než cokoli odejde klientovi:

- Přepočítejte sami jeden řádek cenové tabulky.
- Projděte každé `[DOPLNIT]` a doplňte ho, nebo větu smažte.
- Zkontrolujte hranici rozsahu („co není součástí“): tady začínají spory.
- Porovnejte termíny s termínem klienta.

## Ceník

`sample-data/offer/rate-card.xlsx` je **fiktivní**. Ve skutečnosti mějte platný ceník na jednom
místě, které čte celý tým (soubor na Drive nebo SharePointu přes konektor, nebo přímo
v pluginu), aby nikdo nevložil do konverzace starou verzi.
