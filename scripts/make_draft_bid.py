"""Builds sample-data/tender/draft/Quanti_nabidka_TSB_pracovni.docx: a draft bid with planted errors.

The planted errors are listed in solutions/draft-bid-key.md; keep both in sync.
Run: uv run --with python-docx python scripts/make_draft_bid.py
"""
from pathlib import Path

from docx import Document
from docx.shared import Pt, RGBColor

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "sample-data/tender/draft/Quanti_nabidka_TSB_pracovni.docx"

doc = Document()
style = doc.styles["Normal"]
style.font.name = "Montserrat"
style.font.size = Pt(10.5)

warning = doc.add_paragraph()
run = warning.add_run("CVIČNÝ DOKUMENT PRO WORKSHOP. Údaje o týmu, referencích a certifikátech jsou fiktivní.")
run.bold = True
run.font.color.rgb = RGBColor(0xDF, 0x26, 0x86)

doc.add_heading("Nabídka: Technická modernizace a optimalizace webové aplikace tsbohemia.cz", 1)
doc.add_paragraph("Pracovní verze 0.3 pro interní kontrolu, 24. 11. 2026. Zadavatel: T.S.BOHEMIA a.s. Účastník: Quanti s.r.o.")

doc.add_heading("1. Lhůta a způsob podání", 2)
for line in [
    "Lhůta pro podání nabídek: 2. 11. 2026 v 10:00.",
    "Nabídku podáme elektronicky přes NEN; pro jistotu pošleme kopii e-mailem kontaktní osobě zadavatele.",
    "Případnou listinnou verzi vložíme do obálky označené „NEOTEVÍRAT“.",
    "Nabídka bude svázaná a stránky očíslované.",
]:
    doc.add_paragraph(line, style="List Bullet")

doc.add_heading("2. Cena", 2)
doc.add_paragraph(
    "Nabídková cena dle Formuláře nabídky (Příloha 1): 4 850 000 Kč bez DPH, 5 868 500 Kč vč. DPH."
)
doc.add_paragraph(
    "Položkový rozpočet (Příloha 2 smlouvy) je přiložen v samostatném souboru; jeho součet: 4 580 000 Kč bez DPH."
)
doc.add_paragraph(
    "Cena je orientační; při vyšší skutečné pracnosti ji navýšíme po dohodě se zadavatelem podle sazeb v rozpočtu."
)

doc.add_heading("3. Kvalifikace: referenční zakázky", 2)
doc.add_paragraph("Podle čl. 6 ZD postačuje alespoň 1 referenční zakázka; pro jistotu uvádíme dvě.")
table = doc.add_table(rows=1, cols=4)
table.style = "Light Grid Accent 1"
for cell, value in zip(table.rows[0].cells, ["Klient", "Předmět", "Hodnota bez DPH", "Dokončeno"]):
    cell.text = value
for row in [
    ("Klient A (fiktivní)", "B2B/B2C e-shop na Adobe Commerce, napojení na ERP", "6 500 000 Kč", "03/2025"),
    ("Klient B (fiktivní)", "Redesign e-shopu a optimalizace výkonu", "3 200 000 Kč", "09/2024"),
]:
    cells = table.add_row().cells
    for cell, value in zip(cells, row):
        cell.text = value

doc.add_heading("4. Realizační tým (Odborná úroveň, Příloha 4)", 2)
team = doc.add_table(rows=1, cols=3)
team.style = "Light Grid Accent 1"
for cell, value in zip(team.rows[0].cells, ["Role", "Osoba", "Poznámka"]):
    cell.text = value
for row in [
    ("Projektový manažer", "Jana K.", "Certifikát PRINCE2 doložíme po podpisu smlouvy."),
    ("Senior Frontend developer", "Petr N.", "React, Next.js, 9 let praxe"),
    ("UX/UI designer", "Lucie M.", "8 let praxe"),
    ("Analytik (webová analytika)", "Tomáš R.", "GA4, GTM, 6 let praxe"),
    ("DevOps specialista", "Petr N.", "Docker, CI/CD"),
]:
    cells = team.add_row().cells
    for cell, value in zip(cells, row):
        cell.text = value
doc.add_paragraph("Použijeme formulář Odborná úroveň ve verzi z 22. 9. 2026 (260922_Priloha4ZD-Odborna_uroven.docx).")

doc.add_heading("5. Certifikáty", 2)
for line in [
    "ISO 9001: platný do 05/2028, rozsah vývoj software a řízení projektů.",
    "ISO 27001: certifikace probíhá, certifikát očekáváme v 01/2027; přiložíme čestné prohlášení.",
]:
    doc.add_paragraph(line, style="List Bullet")

doc.add_heading("6. Smlouva o dílo", 2)
for line in [
    "Přikládáme podepsaný závazný návrh smlouvy ve verzi z 22. 9. 2026 (260922_Priloha2ZD-Smlouva_o_dilo.docx).",
    "Smlouva bude svázaná spolu s ostatními částmi nabídky v jednom vyhotovení.",
    "Termín dokončení díla: nejpozději 30. 6. 2027.",
]:
    doc.add_paragraph(line, style="List Bullet")

doc.add_heading("7. Technický přístup", 2)
for line in [
    "Úpravy backendového REST API (.NET) pro košík a logování (projekty 5 a 6) provedeme sami, odhad 80 MD je v ceně.",
    "Cílové hodnoty Core Web Vitals ověříme laboratorním měřením (Lighthouse) bez skriptů třetích stran.",
    "Měření před a po zdokumentujeme v závěrečné zprávě.",
]:
    doc.add_paragraph(line, style="List Bullet")

OUT.parent.mkdir(parents=True, exist_ok=True)
doc.save(OUT)
print(f"wrote {OUT.relative_to(ROOT)}")
