"""Builds plugins/quanti-sales/skills/quanti-brand/assets/quanti-template.pptx: one of each slide type.

Run: uv run --with python-pptx python scripts/make_template.py
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "plugins/quanti-sales/skills/quanti-brand/assets"
sys.path.insert(0, str(ASSETS))

from quanti_slides import cards, chapter_slide, closing_slide, content_slide, new_deck, title_slide  # noqa: E402

deck = new_deck()
title_slide(deck, "Název prezentace", "Podnadpis prezentace")
chapter_slide(deck, "Název kapitoly")
content_slide(deck, "Nadpis obsahového slidu", ["Jedna myšlenka na slide", "Krátké věty, vykáme", "Logo vždy vpravo dole"],
              lead="Úvodní věta, která říká, co si má klient odnést.")
slide = content_slide(deck, "Tři karty vedle sebe", lead="Nejvýše tři karty v řadě, jedna smí být růžová.")
cards(slide, [("Analýza", "Projdeme procesy a data."), ("Vývoj", "Postavíme a napojíme."), ("Spuštění", "Ohlídáme ostrý provoz.")],
      accent_index=2)
closing_slide(deck, "Jméno Příjmení", "Pozice", "jmeno.prijmeni@quanti.cz", "+420 000 000 000")
out = ASSETS / "quanti-template.pptx"
deck.save(out)
print(f"wrote {out.relative_to(ROOT)}")
