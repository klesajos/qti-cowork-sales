"""Quanti slide helpers (python-pptx), following the Quanti brand manual 2024.

The signature element is the "základní tvar": a panel with two opposite corners cut on the
diagonal, echoing the hexagon in the logo. The logo always sits in the bottom-right corner.
Margins follow the manual's construction: A = the shorter side, outer margin A/25, text inset A/15.

Usage:
    import sys; sys.path.insert(0, "<path to this assets folder>")
    from quanti_slides import new_deck, title_slide, chapter_slide, content_slide, cards, closing_slide
    deck = new_deck()
    title_slide(deck, "Nový e-shop a věrnostní program", "Úvodní schůzka, Bylinkárna Vltava")
    slide = content_slide(deck, "Jak rozumíme vaší situaci", ["14 prodejen", "Money S5"])
    deck.save("out.pptx")
"""
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import MSO_ANCHOR
from pptx.util import Emu, Pt

ASSETS = Path(__file__).resolve().parent
LOGO = ASSETS / "quanti-logo.png"
LOGO_WHITE = ASSETS / "quanti-logo-white.png"

PINK = RGBColor(0xDF, 0x26, 0x86)
PURPLE = RGBColor(0x4D, 0x12, 0x54)
BLACK = RGBColor(0x04, 0x05, 0x05)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
PURPLE_20 = RGBColor(0xDB, 0xD0, 0xDD)
PINK_20 = RGBColor(0xF9, 0xD4, 0xE7)
FONT = "Montserrat"

WIDTH = Emu(12192000)   # 13.333 in, 16:9
HEIGHT = Emu(6858000)   # 7.5 in
MARGIN = Emu(HEIGHT // 25)
INSET = Emu(HEIGHT // 15)


def new_deck() -> Presentation:
    """A blank 16:9 deck whose theme fonts are Montserrat."""
    deck = Presentation()
    deck.slide_width, deck.slide_height = WIDTH, HEIGHT
    theme_part = deck.slide_master.part.part_related_by(
        "http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme")
    xml = theme_part.blob.decode("utf-8")
    for tag in ("majorFont", "minorFont"):
        start = xml.index(f"<a:{tag}>")
        latin_start = xml.index("<a:latin ", start)
        latin_end = xml.index("/>", latin_start) + 2
        xml = xml[:latin_start] + f'<a:latin typeface="{FONT}"/>' + xml[latin_end:]
    theme_part._blob = xml.encode("utf-8")
    return deck


def _blank(deck: Presentation, background: RGBColor):
    slide = deck.slides.add_slide(deck.slide_layouts[6])
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = background
    return slide


def hexagon_panel(slide, left, top, width, height, color: RGBColor, cut_top=0.34, cut_bottom=0.52):
    """The manual's basic shape: top-right and bottom-left corners cut on the diagonal.

    cut_top / cut_bottom are the cut sizes as a fraction of the panel width.
    """
    top_cut = int(width * cut_top)
    bottom_cut = int(width * cut_bottom)
    slope = height / width * 1.6
    builder = slide.shapes.build_freeform(left, top, scale=1.0)
    builder.add_line_segments([
        (left + width - top_cut, top),
        (left + width, top + int(top_cut * slope)),
        (left + width, top + height),
        (left + bottom_cut, top + height),
        (left, top + height - int(bottom_cut * slope * 0.45)),
        (left, top),
    ])
    shape = builder.convert_to_shape()
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    shape.shadow.inherit = False
    return shape


def text(slide, left, top, width, height, value: str, size: int, color: RGBColor, bold=False,
         anchor=MSO_ANCHOR.TOP, line_spacing=1.15):
    """A text box in Montserrat; each \\n starts a paragraph."""
    box = slide.shapes.add_textbox(left, top, width, height)
    frame = box.text_frame
    frame.word_wrap = True
    frame.vertical_anchor = anchor
    frame.margin_left = frame.margin_right = frame.margin_top = frame.margin_bottom = 0
    for index, line in enumerate(value.split("\n")):
        paragraph = frame.paragraphs[0] if index == 0 else frame.add_paragraph()
        paragraph.line_spacing = line_spacing
        run = paragraph.add_run()
        run.text = line
        run.font.name = FONT
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.color.rgb = color
    return box


def logo(slide, on_dark: bool, width=Emu(1600000)):
    """The logo, always bottom-right inside the margins."""
    image = LOGO_WHITE if on_dark else LOGO
    height = int(width * 256 / 1176)
    return slide.shapes.add_picture(str(image), WIDTH - MARGIN - INSET - width, HEIGHT - MARGIN - INSET - height,
                                    width=width)


def title_slide(deck, title: str, subtitle: str, footer="Software\nHardware\nInfrastruktura",
                background=PURPLE, panel=PINK):
    """Title slide: pink panel on purple (primary combination), white bold title."""
    slide = _blank(deck, background)
    hexagon_panel(slide, MARGIN, MARGIN, WIDTH - 2 * MARGIN, HEIGHT - 2 * MARGIN, panel)
    text(slide, MARGIN + INSET, Emu(int(HEIGHT * 0.2)), Emu(int(WIDTH * 0.62)), Emu(int(HEIGHT * 0.3)),
         title, 44, WHITE, bold=True, anchor=MSO_ANCHOR.BOTTOM, line_spacing=1.0)
    text(slide, MARGIN + INSET, Emu(int(HEIGHT * 0.52)), Emu(int(WIDTH * 0.6)), Emu(int(HEIGHT * 0.1)),
         subtitle, 22, WHITE, bold=True)
    text(slide, MARGIN + INSET, Emu(int(HEIGHT * 0.74)), Emu(int(WIDTH * 0.3)), Emu(int(HEIGHT * 0.16)),
         footer, 14, WHITE, line_spacing=1.1)
    logo(slide, on_dark=True)
    return slide


def chapter_slide(deck, title: str, background=PURPLE, panel=PINK, title_color=PURPLE):
    """Chapter divider: pink panel, purple bold title."""
    slide = _blank(deck, background)
    hexagon_panel(slide, MARGIN, MARGIN, WIDTH - 2 * MARGIN, HEIGHT - 2 * MARGIN, panel, cut_top=0.12, cut_bottom=0.0001)
    text(slide, MARGIN + INSET, Emu(int(HEIGHT * 0.3)), Emu(int(WIDTH * 0.6)), Emu(int(HEIGHT * 0.3)),
         title, 48, title_color, bold=True, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
    logo(slide, on_dark=True)
    return slide


def content_slide(deck, title: str, bullets=None, lead: str | None = None):
    """Content slide: white background, purple bold title, black body, colour logo bottom-right."""
    slide = _blank(deck, WHITE)
    text(slide, MARGIN + INSET, MARGIN + INSET, WIDTH - 2 * (MARGIN + INSET), Emu(900000),
         title, 32, PURPLE, bold=True, line_spacing=1.0)
    top = MARGIN + INSET + Emu(1000000)
    if lead:
        text(slide, MARGIN + INSET, top, Emu(int(WIDTH * 0.7)), Emu(700000), lead, 20, BLACK)
        top += Emu(800000)
    if bullets:
        text(slide, MARGIN + INSET, top, Emu(int(WIDTH * 0.7)), Emu(int(HEIGHT * 0.5)),
             "\n".join(f"•  {line}" for line in bullets), 20, BLACK, line_spacing=1.3)
    logo(slide, on_dark=False, width=Emu(1300000))
    return slide


def cards(slide, items, top=None, height=Emu(2200000), fill=PURPLE_20, accent_index=None):
    """Up to 3 cards in a row: (heading, body) pairs. accent_index makes one card pink with white text."""
    items = items[:3]
    top = top if top is not None else Emu(int(HEIGHT * 0.38))
    gap = Emu(250000)
    usable = WIDTH - 2 * (MARGIN + INSET)
    width = Emu((usable - gap * (len(items) - 1)) // len(items))
    for index, (heading, body) in enumerate(items):
        left = MARGIN + INSET + index * (width + gap)
        is_accent = index == accent_index
        hexagon_panel(slide, left, top, width, height, PINK if is_accent else fill, cut_top=0.14, cut_bottom=0.0001)
        color = WHITE if is_accent else BLACK
        text(slide, left + Emu(220000), top + Emu(220000), width - Emu(600000), Emu(500000),
             heading, 18, WHITE if is_accent else PURPLE, bold=True, line_spacing=1.0)
        text(slide, left + Emu(220000), top + Emu(800000), width - Emu(440000), height - Emu(950000),
             body, 15, color, line_spacing=1.2)


def closing_slide(deck, name: str, role: str, email: str, phone: str, background=PURPLE, panel=PINK):
    """Closing slide: same colours as the title slide, salesperson's contact."""
    slide = _blank(deck, background)
    hexagon_panel(slide, MARGIN, MARGIN, WIDTH - 2 * MARGIN, HEIGHT - 2 * MARGIN, panel)
    text(slide, MARGIN + INSET, Emu(int(HEIGHT * 0.3)), Emu(int(WIDTH * 0.6)), Emu(600000), name, 32, WHITE, bold=True)
    text(slide, MARGIN + INSET, Emu(int(HEIGHT * 0.3)) + Emu(650000), Emu(int(WIDTH * 0.6)), Emu(400000),
         role, 16, WHITE, bold=True)
    text(slide, MARGIN + INSET, Emu(int(HEIGHT * 0.3)) + Emu(1250000), Emu(int(WIDTH * 0.6)), Emu(800000),
         f"{email}\n{phone}", 16, WHITE)
    logo(slide, on_dark=True)
    return slide
