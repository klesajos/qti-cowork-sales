# HubSpot export: Bylinkárna Vltava (fiktivní deal pro workshop)

Tato složka napodobuje, co vrátí HubSpot konektor v Claude pro jeden deal: záznamy firmy,
kontaktů a dealu (JSON tak, jak je vrací `search_crm_objects`) a aktivity (e-maily, hovor,
schůzka, poznámky, úkol) v `engagements/`, jedna aktivita = jeden soubor, název začíná datem.

Facilitátor na ní ukazuje cvičení 9 (nemá v HubSpotu právo zapisovat). Účastníci dělají totéž
nad **svým** dealem přes konektor: stejné prompty, jen místo „ve složce hubspot/“ řeknou
„v HubSpotu“. Všechna jména, čísla a firmy jsou smyšlené; shodují se s `offer/client-brief.md`.

Záměrné pasti (klíč: `solutions/deal-brief-key.md`): dva termíny (starší e-mail vs. novější),
„pátek 5. 12.“ v e-mailu je ve skutečnosti sobota, mobilní aplikace (e-mail „zatím ne“ vs. hovor
„majitelka ji chce“), rozpočet klienta vs. náš odhad v dealu, konkurenční nabídka, kontakt,
který je jen v hovoru.
