"""Builds sample-data/decks/Bylinkarna_uvodni_prezentace.pptx: a deck with planted brand errors.

The planted errors are listed in solutions/deck-review-key.md; keep both in sync.
Run: uv run --with python-pptx python scripts/make_offbrand_deck.py
"""
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt

ROOT = Path(__file__).resolve().parent.parent
LOGO = ROOT / "sample-data/brand/quanti-logo.png"
OUT = ROOT / "sample-data/decks/Bylinkarna_uvodni_prezentace.pptx"

BLUE = RGBColor(0x1F, 0x4E, 0x9C)
GREEN = RGBColor(0x2E, 0xA0, 0x4F)
ORANGE = RGBColor(0xF2, 0x8C, 0x28)
PURPLE = RGBColor(0x4D, 0x12, 0x54)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
BLACK = RGBColor(0x00, 0x00, 0x00)


def fill(slide, color: RGBColor) -> None:
    background = slide.background.fill
    background.solid()
    background.fore_color.rgb = color


def text(slide, left, top, width, height, value: str, size: int, font: str, color: RGBColor, bold=False):
    box = slide.shapes.add_textbox(left, top, width, height)
    frame = box.text_frame
    frame.word_wrap = True
    for index, line in enumerate(value.split("\n")):
        paragraph = frame.paragraphs[0] if index == 0 else frame.add_paragraph()
        run = paragraph.add_run()
        run.text = line
        run.font.size = Pt(size)
        run.font.name = font
        run.font.bold = bold
        run.font.color.rgb = color
    return box


def card(slide, left, top, width, height, label: str, color: RGBColor):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.shadow.inherit = True
    frame = shape.text_frame
    frame.word_wrap = True
    run = frame.paragraphs[0].add_run()
    run.text = label
    run.font.size = Pt(14)
    run.font.name = "Calibri"
    run.font.color.rgb = WHITE


deck = Presentation()
deck.slide_width = Inches(13.333)
deck.slide_height = Inches(7.5)
blank = deck.slide_layouts[6]

# 1: blue title slide, Calibri, sentence-case title, stretched colour logo
slide = deck.slides.add_slide(blank)
fill(slide, BLUE)
slide.shapes.add_picture(str(LOGO), Inches(0.6), Inches(0.5), width=Inches(5), height=Inches(0.6))
text(slide, Inches(0.6), Inches(2.6), Inches(12), Inches(1.5), "Quanti x Bylinkárna Vltava", 48, "Calibri", WHITE, True)
text(slide, Inches(0.6), Inches(4.0), Inches(12), Inches(1), "Úvodní prezentace našich služeb", 24, "Calibri", WHITE)

# 2: wall of text, unapproved claims, buzzwords
slide = deck.slides.add_slide(blank)
fill(slide, WHITE)
text(slide, Inches(0.6), Inches(0.4), Inches(12), Inches(1), "O nás", 36, "Calibri", BLUE, True)
text(
    slide, Inches(0.6), Inches(1.4), Inches(12), Inches(5.5),
    "Quanti je world-class technologická společnost, která přináší inovativní komplexní řešení na klíč "
    "pro e-commerce, mobilní aplikace, hardware i IT infrastrukturu. Díky synergii našich týmů dokážeme "
    "našim klientům dodat maximální přidanou hodnotu v každé fázi projektu, od analýzy přes návrh, vývoj "
    "a testování až po dlouhodobou správu a rozvoj. Náš roční obrat přesahuje 200 mil. Kč a jsme držiteli "
    "certifikace ISO 27001. Máme více než 150 odborníků a stovky spokojených klientů po celé Evropě. "
    "Naše řešení jsou vždy postavena na nejmodernějších technologiích a nejlepších postupech v oboru, "
    "což nám umožňuje garantovat výsledky, které předčí vaše očekávání. Spolupracujeme s předními "
    "světovými značkami a neustále rozšiřujeme své portfolio služeb.",
    20, "Calibri", BLACK,
)

# 3: off-palette accents and Times New Roman
slide = deck.slides.add_slide(blank)
fill(slide, WHITE)
text(slide, Inches(0.6), Inches(0.4), Inches(12), Inches(1), "Co pro vás uděláme", 36, "Times New Roman", GREEN, True)
for index, (label, color) in enumerate([("Nový e-shop B2C + B2B", GREEN), ("Napojení na Money S5", ORANGE), ("Věrnostní program", BLUE)]):
    card(slide, Inches(0.6 + index * 4.2), Inches(2.0), Inches(3.8), Inches(2.5), label, color)

# 4: colour logo on purple, five sharp shadowed boxes in a row
slide = deck.slides.add_slide(blank)
fill(slide, PURPLE)
slide.shapes.add_picture(str(LOGO), Inches(10.4), Inches(0.4), width=Inches(2.4))
text(slide, Inches(0.6), Inches(0.4), Inches(9), Inches(1), "Postup", 36, "Calibri", WHITE, True)
for index, label in enumerate(["Analýza", "Design", "Vývoj", "Testování", "Spuštění"]):
    card(slide, Inches(0.6 + index * 2.5), Inches(2.5), Inches(2.3), Inches(1.6), label, BLUE)

# 5: unsourced guarantee, exclamation marks
slide = deck.slides.add_slide(blank)
fill(slide, WHITE)
text(slide, Inches(0.6), Inches(0.4), Inches(12), Inches(1), "Proč my!", 36, "Calibri", BLUE, True)
text(
    slide, Inches(0.6), Inches(1.6), Inches(12), Inches(4),
    "Garantujeme 99,99 % dostupnost e-shopu!\nNaše řešení používají Dr.Max, BAT nebo ProEx.\nSpuštění do 3 měsíců!",
    28, "Calibri", BLACK,
)

# 6: no next step, ends with a thank-you
slide = deck.slides.add_slide(blank)
fill(slide, BLUE)
text(slide, Inches(0.6), Inches(3.0), Inches(12), Inches(1.5), "Děkujeme za pozornost!", 48, "Calibri", WHITE, True)

OUT.parent.mkdir(parents=True, exist_ok=True)
deck.save(OUT)
print(f"wrote {OUT.relative_to(ROOT)} ({len(deck.slides)} slides)")
