#!/usr/bin/env python3
"""Generate SAD Phase 2 PDF with a Phase-1-like simple theme."""

from __future__ import annotations

import re
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, StyleSheet1, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = PROJECT_ROOT / "docs"
INPUT_MD = DOCS_DIR / "SAD_Phase2.md"
OUTPUT_PDF = DOCS_DIR / "SAD_Phase2.pdf"
FONT_REGULAR = "SADSans"
FONT_BOLD = "SADSansBold"
FONT_ITALIC = "SADSansItalic"
FONT_BOLD_ITALIC = "SADSansBoldItalic"


def register_fonts() -> None:
    """Register Unicode-capable fonts for Turkish characters."""
    base = Path("C:/Windows/Fonts")
    pdfmetrics.registerFont(TTFont(FONT_REGULAR, str(base / "times.ttf")))
    pdfmetrics.registerFont(TTFont(FONT_BOLD, str(base / "timesbd.ttf")))
    pdfmetrics.registerFont(TTFont(FONT_ITALIC, str(base / "timesi.ttf")))
    pdfmetrics.registerFont(TTFont(FONT_BOLD_ITALIC, str(base / "timesbi.ttf")))


def inline_md_to_html(text: str) -> str:
    """Convert minimal inline markdown (**bold**, `code`) to reportlab XML."""
    escaped = escape(text)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", escaped)
    escaped = re.sub(r"`(.+?)`", r"<font face='Courier'>\1</font>", escaped)
    return escaped


def build_styles() -> StyleSheet1:
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="H1Formal",
            parent=styles["Heading1"],
            fontName=FONT_BOLD,
            fontSize=16,
            leading=20,
            spaceBefore=10,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="H2Formal",
            parent=styles["Heading2"],
            fontName=FONT_BOLD,
            fontSize=13,
            leading=17,
            spaceBefore=8,
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="H3Formal",
            parent=styles["Heading3"],
            fontName=FONT_BOLD,
            fontSize=11.5,
            leading=15,
            spaceBefore=6,
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BodyFormal",
            parent=styles["BodyText"],
            fontName=FONT_REGULAR,
            fontSize=11,
            leading=15,
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BulletFormal",
            parent=styles["BodyText"],
            fontName=FONT_REGULAR,
            fontSize=11,
            leading=15,
            leftIndent=14,
            bulletIndent=4,
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CodeFormal",
            parent=styles["Code"],
            fontName="Courier",
            fontSize=8.7,
            leading=11,
            backColor=None,
            borderColor=None,
            borderWidth=0.5,
            borderPadding=2,
            leftIndent=4,
            rightIndent=4,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SmallMuted",
            parent=styles["BodyText"],
            fontName=FONT_ITALIC,
            fontSize=9,
            alignment=0,
        )
    )
    return styles


def parse_table_block(table_lines: list[str], styles: StyleSheet1) -> Table:
    rows: list[list[str]] = []
    for line in table_lines:
        stripped = line.strip().strip("|")
        if set(stripped.replace("|", "").replace("-", "").replace(" ", "")) == set():
            continue
        cols = [inline_md_to_html(col.strip()) for col in stripped.split("|")]
        rows.append(cols)

    if not rows:
        return Table([[""]])

    col_count = max(len(row) for row in rows)
    normalized_rows: list[list[Paragraph]] = []
    for row in rows:
        row = row + [""] * (col_count - len(row))
        normalized_rows.append([Paragraph(cell, styles["BodyFormal"]) for cell in row])

    table = Table(normalized_rows, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), None),
                ("FONTNAME", (0, 0), (-1, 0), FONT_BOLD),
                ("FONTNAME", (0, 1), (-1, -1), FONT_REGULAR),
                ("GRID", (0, 0), (-1, -1), 0.5, "black"),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    return table


def add_page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont(FONT_REGULAR, 9)
    canvas.drawRightString(A4[0] - 1.8 * cm, 1.0 * cm, str(doc.page))
    canvas.restoreState()


def build_story(md_text: str, styles: StyleSheet1):
    lines = md_text.splitlines()
    story = []

    in_code = False
    code_lines: list[str] = []
    table_buffer: list[str] = []

    def flush_table():
        nonlocal table_buffer
        if table_buffer:
            story.append(parse_table_block(table_buffer, styles))
            story.append(Spacer(1, 0.2 * cm))
            table_buffer = []

    for raw in lines:
        line = raw.rstrip("\n")
        stripped = line.strip()

        if stripped.startswith("```"):
            flush_table()
            if in_code:
                code_text = "\n".join(code_lines).rstrip()
                if code_text:
                    story.append(Preformatted(code_text, styles["CodeFormal"]))
                code_lines = []
                in_code = False
            else:
                in_code = True
            continue

        if in_code:
            code_lines.append(line)
            continue

        if stripped.startswith("|") and stripped.endswith("|"):
            table_buffer.append(line)
            continue
        flush_table()

        if not stripped:
            story.append(Spacer(1, 0.12 * cm))
            continue

        if stripped == "---":
            story.append(Spacer(1, 0.08 * cm))
            continue

        if stripped.startswith("# "):
            story.append(Paragraph(inline_md_to_html(stripped[2:]), styles["H1Formal"]))
            continue
        if stripped.startswith("## "):
            story.append(Paragraph(inline_md_to_html(stripped[3:]), styles["H1Formal"]))
            continue
        if stripped.startswith("### "):
            story.append(Paragraph(inline_md_to_html(stripped[4:]), styles["H2Formal"]))
            continue
        if stripped.startswith("#### "):
            story.append(Paragraph(inline_md_to_html(stripped[5:]), styles["H3Formal"]))
            continue

        ordered = re.match(r"^(\d+)\.\s+(.*)$", stripped)
        if ordered:
            story.append(
                Paragraph(
                    f"{ordered.group(1)}. {inline_md_to_html(ordered.group(2))}",
                    styles["BodyFormal"],
                )
            )
            continue

        if stripped.startswith("- "):
            story.append(
                Paragraph(
                    f"• {inline_md_to_html(stripped[2:])}",
                    styles["BulletFormal"],
                )
            )
            continue

        story.append(Paragraph(inline_md_to_html(stripped), styles["BodyFormal"]))

    flush_table()
    if code_lines:
        story.append(Preformatted("\n".join(code_lines).rstrip(), styles["CodeFormal"]))

    return story


def main() -> None:
    if not INPUT_MD.exists():
        raise FileNotFoundError(f"Missing input file: {INPUT_MD}")

    register_fonts()
    styles = build_styles()
    story = build_story(INPUT_MD.read_text(encoding="utf-8"), styles)

    doc = SimpleDocTemplate(
        str(OUTPUT_PDF),
        pagesize=A4,
        leftMargin=1.8 * cm,
        rightMargin=1.8 * cm,
        topMargin=1.6 * cm,
        bottomMargin=1.6 * cm,
        title="Software Architecture Document V2",
        author="PromoCatch Team",
    )
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f"Wrote {OUTPUT_PDF} ({OUTPUT_PDF.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
