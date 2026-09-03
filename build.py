"""
Builds two SEPARATE PDFs from content.py:
  LCA_Life_Science_Ch1_Practice_Test.pdf   (student copy, no answers)
  LCA_Life_Science_Ch1_Answer_Key.pdf      (answers only)
Styled to Lexington Christian Academy: royal blue #253A7E, condensed caps headings.
"""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether)

import content as C

OUT = os.path.dirname(os.path.abspath(__file__))
TEST_PDF = os.path.join(OUT, "LCA_Life_Science_Ch1_Practice_Test.pdf")
KEY_PDF = os.path.join(OUT, "LCA_Life_Science_Ch1_Answer_Key.pdf")

PAGE_W, PAGE_H = letter
MARGIN = 0.75 * inch
TOP_MARGIN = 0.95 * inch
BODY_W = PAGE_W - 2 * MARGIN

LCA_BLUE = colors.HexColor("#253A7E")
LCA_DEEP = colors.HexColor("#172550")
EDGE = colors.HexColor("#0E0C0B")
GRAY = colors.HexColor("#55575E")
RULE = colors.HexColor("#CFCCCB")
TINT = colors.HexColor("#E7EAF4")
BAND = colors.HexColor("#F2F3F8")

BASE, BOLD, ITAL = "Helvetica", "Helvetica-Bold", "Helvetica-Oblique"

st_title = ParagraphStyle("t", fontName=BOLD, fontSize=19, leading=22, alignment=TA_CENTER, textColor=LCA_BLUE)
st_sub = ParagraphStyle("s", fontName=BASE, fontSize=12, leading=15, alignment=TA_CENTER, textColor=colors.black)
st_eyebrow = ParagraphStyle("e", fontName=BOLD, fontSize=8, leading=11, alignment=TA_CENTER, textColor=GRAY)
st_badge = ParagraphStyle("b", fontName=BOLD, fontSize=12, leading=15, alignment=TA_CENTER, textColor=colors.white)
st_part = ParagraphStyle("p", fontName=BOLD, fontSize=11, leading=14, textColor=colors.white)
st_partpts = ParagraphStyle("pp", fontName=BASE, fontSize=8.5, leading=14, textColor=colors.HexColor("#C3CBE4"),
                            alignment=2)
st_instr = ParagraphStyle("i", fontName=ITAL, fontSize=9.5, leading=12.5, textColor=GRAY, spaceAfter=5)
st_body = ParagraphStyle("bd", fontName=BASE, fontSize=10.5, leading=13.8)
st_q = ParagraphStyle("q", parent=st_body, leftIndent=24, firstLineIndent=-24, spaceBefore=5)
st_opt = ParagraphStyle("o", parent=st_body, leftIndent=40, firstLineIndent=-14, leading=13.2)
st_cell = ParagraphStyle("c", parent=st_body, fontSize=10, leading=12.4)
st_cellb = ParagraphStyle("cb", parent=st_cell, fontName=BOLD)
st_small = ParagraphStyle("sm", parent=st_body, fontSize=9, leading=12, textColor=GRAY)
st_ans = ParagraphStyle("a", parent=st_body, leftIndent=30, firstLineIndent=-30, spaceBefore=2)
st_note = ParagraphStyle("n", parent=st_body, leftIndent=14, firstLineIndent=-14, spaceBefore=3, fontSize=10, leading=13)
st_model = ParagraphStyle("m", parent=st_body, leftIndent=30, spaceBefore=1, spaceAfter=4)

BLANK = "_" * 22
SHORT_BLANK = "_" * 8
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
TERM_LETTER = {t: LETTERS[i] for i, t in enumerate(C.MATCHING_TERMS)}


def part_heading(key, title, pts):
    """Blue bar heading, LCA style."""
    t = Table([[Paragraph(f"PART {key}.  {title.upper()}", st_part),
                Paragraph(f"{pts} POINTS", st_partpts)]],
              colWidths=[BODY_W * 0.72, BODY_W * 0.28])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), LCA_BLUE),
                           ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                           ("LEFTPADDING", (0, 0), (0, -1), 8), ("RIGHTPADDING", (1, 0), (1, -1), 8),
                           ("VALIGN", (0, 0), (-1, -1), "MIDDLE")]))
    return [Spacer(1, 10), t, Spacer(1, 4)]


def word_bank(words, cols=4, lettered=False, title="WORD BANK"):
    rows = -(-len(words) // cols)
    grid = [["" for _ in range(cols)] for _ in range(rows)]
    for i, w in enumerate(words):
        r, c = i % rows, i // rows
        label = f"<b><font color='#253A7E'>{LETTERS[i]}.</font></b>  " if lettered else ""
        grid[r][c] = Paragraph(label + w, st_cell)
    head = [[Paragraph(f"<b><font color='#253A7E'>{title}</font></b>", st_small)] + [""] * (cols - 1)]
    t = Table(head + grid, colWidths=[BODY_W / cols] * cols)
    t.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.8, RULE),
                           ("LINEABOVE", (0, 0), (-1, 0), 2, LCA_BLUE),
                           ("SPAN", (0, 0), (-1, 0)),
                           ("BACKGROUND", (0, 0), (-1, -1), BAND),
                           ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                           ("LEFTPADDING", (0, 0), (-1, -1), 9)]))
    return t


# --------------------------------------------------------------- numbering ---
n = 1
NUM = {}
NUM["matching"] = [n + i for i in range(len(C.MATCHING_ITEMS))];  n += len(C.MATCHING_ITEMS)
NUM["mc"] = [n + i for i in range(len(C.MULTIPLE_CHOICE))];       n += len(C.MULTIPLE_CHOICE)
NUM["fill"] = [n + i for i in range(len(C.FILL_IN))];             n += len(C.FILL_IN)
NUM["tf"] = [n + i for i in range(len(C.TRUE_FALSE))];            n += len(C.TRUE_FALSE)
NUM["chart"] = [n + i for i in range(2 * len(C.CHART_ROWS))];     n += 2 * len(C.CHART_ROWS)
NUM["cls"] = n;                                                    n += 1
NUM["short"] = [n + i for i in range(len(C.SHORT_ANSWER))];       n += len(C.SHORT_ANSWER)
TOTAL_ITEMS = n - 1

PTS = {"matching": len(C.MATCHING_ITEMS), "mc": len(C.MULTIPLE_CHOICE),
       "fill": sum(len(a) for _, a in C.FILL_IN), "tf": len(C.TRUE_FALSE),
       "chart": 2 * len(C.CHART_ROWS), "cls": len(C.CLASSIFICATION_LEVELS),
       "short": 3 * len(C.SHORT_ANSWER)}
PTS["total"] = sum(PTS.values())

PART_TITLES = [("A", "Vocabulary Matching", PTS["matching"]), ("B", "Multiple Choice", PTS["mc"]),
               ("C", "Fill in the Blank", PTS["fill"]), ("D", "True or False", PTS["tf"]),
               ("E", "Worldview Chart", PTS["chart"]), ("F", "Levels of Classification", PTS["cls"]),
               ("G", "Select and Order", PTS["short"])]


def make_header_footer(right_label):
    def draw(canv, doc):
        canv.saveState()
        # top rule with the course label, like the school's own worksheets
        canv.setFillColor(LCA_BLUE)
        canv.setFont(BOLD, 8)
        canv.drawString(MARGIN, PAGE_H - 0.55 * inch, C.COURSE_LABEL.upper())
        canv.setFont(BASE, 8)
        canv.setFillColor(GRAY)
        canv.drawRightString(PAGE_W - MARGIN, PAGE_H - 0.55 * inch, right_label.upper())
        canv.setStrokeColor(LCA_BLUE); canv.setLineWidth(1.6)
        canv.line(MARGIN, PAGE_H - 0.63 * inch, PAGE_W - MARGIN, PAGE_H - 0.63 * inch)
        canv.setStrokeColor(EDGE); canv.setLineWidth(1.1)
        canv.line(MARGIN, PAGE_H - 0.655 * inch, PAGE_W - MARGIN, PAGE_H - 0.655 * inch)
        canv.setFont(BASE, 8)
        canv.setFillColor(GRAY)
        canv.drawString(MARGIN, 0.5 * inch, "Lexington Christian Academy  |  Chapter 1: God's Living World")
        canv.drawRightString(PAGE_W - MARGIN, 0.5 * inch, f"Page {doc.page}")
        canv.restoreState()
    return draw


def make_doc(path, title):
    return SimpleDocTemplate(path, pagesize=letter, leftMargin=MARGIN, rightMargin=MARGIN,
                             topMargin=TOP_MARGIN, bottomMargin=MARGIN, title=title, author="Practice test")


# ================================================================== TEST ======
def build_test():
    s = []
    s.append(Paragraph(C.SUBTITLE.upper(), st_title))
    s.append(Paragraph("Practice Test", st_sub))
    s.append(Spacer(1, 3))
    s.append(Paragraph("Everything is multiple choice, true or false, or answered from a word bank.", st_eyebrow))
    s.append(Spacer(1, 10))
    hdr = Table([[Paragraph("Name: " + "_" * 32, st_body),
                  Paragraph("Date: " + "_" * 14, st_body),
                  Paragraph(f"Score: ______ / {PTS['total']}", st_body)]],
                colWidths=[3.4 * inch, 1.9 * inch, 1.7 * inch])
    hdr.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]))
    s.append(hdr)
    s.append(Spacer(1, 6))

    # Part A
    s += part_heading("A", "Vocabulary Matching", PTS["matching"])
    s.append(Paragraph("Write the letter of the correct term on the blank next to its definition. "
                       "Each term is used at most once, and four terms in the bank are never used.", st_instr))
    s.append(word_bank(C.MATCHING_TERMS, cols=4, lettered=True, title="TERM BANK"))
    s.append(Spacer(1, 6))
    rows = [[Paragraph(SHORT_BLANK, st_body), Paragraph(f"{num}.", st_body), Paragraph(d, st_body)]
            for num, (d, _) in zip(NUM["matching"], C.MATCHING_ITEMS)]
    t = Table(rows, colWidths=[0.8 * inch, 0.4 * inch, BODY_W - 1.2 * inch])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("TOPPADDING", (0, 0), (-1, -1), 3),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 3), ("LEFTPADDING", (0, 0), (-1, -1), 0),
                           ("RIGHTPADDING", (0, 0), (0, -1), 0)]))
    s.append(t)

    # Part B
    s += part_heading("B", "Multiple Choice", PTS["mc"])
    s.append(Paragraph("Circle the letter of the best answer. Read all four choices before you pick one.", st_instr))
    for num, (stem, opts, _) in zip(NUM["mc"], C.MULTIPLE_CHOICE):
        blk = [Paragraph(f"{num}.  {stem}", st_q)]
        blk += [Paragraph(f"{'abcd'[i]}.  {o}", st_opt) for i, o in enumerate(opts)]
        s.append(KeepTogether(blk))

    # Part C
    s += part_heading("C", "Fill in the Blank", PTS["fill"])
    s.append(Paragraph("Use the word bank to complete each sentence. One point per blank. "
                       "Eight words in the bank are never used.", st_instr))
    s.append(word_bank(C.FILL_WORD_BANK, cols=4))
    s.append(Spacer(1, 4))
    for num, (text, _) in zip(NUM["fill"], C.FILL_IN):
        s.append(Paragraph(f"{num}.  " + text.replace("{}", BLANK), st_q))

    # Part D
    s += part_heading("D", "True or False", PTS["tf"])
    s.append(Paragraph("Write T if the statement is true or F if it is false. "
                       "Read carefully. Some of these turn on a single word.", st_instr))
    rows = [[Paragraph(SHORT_BLANK, st_body), Paragraph(f"{num}.", st_body), Paragraph(text, st_body)]
            for num, (text, _, _) in zip(NUM["tf"], C.TRUE_FALSE)]
    t = Table(rows, colWidths=[0.8 * inch, 0.4 * inch, BODY_W - 1.2 * inch])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("TOPPADDING", (0, 0), (-1, -1), 4),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 4), ("LEFTPADDING", (0, 0), (-1, -1), 0),
                           ("RIGHTPADDING", (0, 0), (0, -1), 0)]))
    s.append(t)

    # Part E
    blk = part_heading("E", "Worldview Chart", PTS["chart"])
    blk.append(Paragraph("Use the word bank to complete the chart comparing how Christians and naturalists "
                         "view life. Each answer is used once. The first row is done for you.", st_instr))
    blk.append(word_bank(C.CHART_WORD_BANK, cols=4))
    blk.append(Spacer(1, 6))
    hc = ParagraphStyle("hc", parent=st_cellb, alignment=TA_CENTER, textColor=colors.white)
    data = [[Paragraph("", hc), Paragraph("CHRISTIANS", hc), Paragraph("NATURALISTS", hc)]]
    ex = C.CHART_EXAMPLE
    data.append([Paragraph(ex[0], st_cellb), Paragraph(ex[1], st_cell), Paragraph(ex[2], st_cell)])
    it = iter(NUM["chart"])
    for label, _, _ in C.CHART_ROWS:
        a, b = next(it), next(it)
        data.append([Paragraph(label, st_cellb),
                     Paragraph(f"({a})  " + "_" * 20, st_cell),
                     Paragraph(f"({b})  " + "_" * 20, st_cell)])
    ct = Table(data, colWidths=[1.75 * inch, 2.625 * inch, 2.625 * inch],
               rowHeights=[0.3 * inch] + [0.4 * inch] * (len(data) - 1))
    ct.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.8, RULE),
                            ("BACKGROUND", (0, 0), (-1, 0), LCA_BLUE),
                            ("BACKGROUND", (0, 1), (-1, 1), TINT),
                            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("LEFTPADDING", (0, 0), (-1, -1), 6)]))
    blk.append(ct)
    s.append(KeepTogether(blk))

    # Part F
    blk = part_heading("F", "Levels of Classification", PTS["cls"])
    blk.append(Paragraph(f"{NUM['cls']}.  Use the word bank to write the eight levels of classification in order "
                         "from the largest group to the smallest group.", st_q))
    blk.append(Spacer(1, 4))
    blk.append(word_bank(C.LEVEL_WORD_BANK, cols=4))
    blk.append(Spacer(1, 6))
    half = len(C.CLASSIFICATION_LEVELS) // 2
    rows = [[Paragraph(f"{i + 1}.  " + "_" * 24, st_body), Paragraph(f"{i + 1 + half}.  " + "_" * 24, st_body)]
            for i in range(half)]
    t = Table(rows, colWidths=[BODY_W / 2] * 2, rowHeights=[0.33 * inch] * half)
    t.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 24), ("VALIGN", (0, 0), (-1, -1), "MIDDLE")]))
    blk.append(t)
    s.append(KeepTogether(blk))

    # Part G
    s += part_heading("G", "Select and Order", PTS["short"])
    s.append(Paragraph("Three points each. Follow the directions in each question: circle every correct choice, "
                       "or number the steps in order.", st_instr))
    for num, q in zip(NUM["short"], C.SHORT_ANSWER):
        blk = [Paragraph(f"{num}.  {q['q']}", st_q)]
        if q["type"] == "multi":
            letters = "abcdefghij"
            opts = [Paragraph(f"{letters[i]}.  {txt}", st_opt) for i, (txt, _) in enumerate(q["options"])]
            h = -(-len(opts) // 2)
            t = Table([[opts[i], opts[i + h] if i + h < len(opts) else ""] for i in range(h)],
                      colWidths=[BODY_W / 2] * 2)
            t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0),
                                   ("TOPPADDING", (0, 0), (-1, -1), 1), ("BOTTOMPADDING", (0, 0), (-1, -1), 1)]))
            blk.append(t)
        elif q["type"] == "order":
            t = Table([[Paragraph(SHORT_BLANK, st_body), Paragraph(step, st_body)] for step in q["shown"]],
                      colWidths=[0.8 * inch, BODY_W - 0.8 * inch - 24])
            t.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (0, -1), 0),
                                   ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
            w = Table([[t]], colWidths=[BODY_W])
            w.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 24), ("TOPPADDING", (0, 0), (-1, -1), 2),
                                   ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]))
            blk.append(w)
        else:
            blk += [Paragraph(f"{'abcd'[i]}.  {o}", st_opt) for i, o in enumerate(q["options"])]
        blk.append(Spacer(1, 4))
        s.append(KeepTogether(blk))

    s.append(Spacer(1, 12))
    s.append(Paragraph("End of practice test. Go back and check that every question has an answer.", st_instr))

    doc = make_doc(TEST_PDF, "LCA Life Science Chapter 1 Practice Test")
    doc.build(s, onFirstPage=make_header_footer("Practice Test"), onLaterPages=make_header_footer("Practice Test"))


# =================================================================== KEY ======
def build_key():
    s = []
    s.append(Paragraph(C.SUBTITLE.upper(), st_title))
    s.append(Paragraph("Practice Test", st_sub))
    s.append(Spacer(1, 8))
    badge = Table([[Paragraph("ANSWER KEY", st_badge)]], colWidths=[1.6 * inch])
    badge.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), LCA_DEEP),
                               ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
    badge.hAlign = "CENTER"
    s.append(badge)
    s.append(Spacer(1, 6))
    s.append(Paragraph(f"Total {PTS['total']} points across {TOTAL_ITEMS} questions. "
                       "Keep this key separate from the student copy.",
                       ParagraphStyle("c", parent=st_instr, alignment=TA_CENTER)))

    s += part_heading("A", "Vocabulary Matching", PTS["matching"])
    items = list(zip(NUM["matching"], C.MATCHING_ITEMS))
    h = -(-len(items) // 2)
    rows = []
    for i in range(h):
        cells = []
        for j in (i, i + h):
            if j < len(items):
                num, (_, term) = items[j]
                cells.append(Paragraph(f"<b>{num}.</b>  {TERM_LETTER[term]}   ({term})", st_body))
            else:
                cells.append(Paragraph("", st_body))
        rows.append(cells)
    t = Table(rows, colWidths=[BODY_W / 2] * 2)
    t.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 6), ("TOPPADDING", (0, 0), (-1, -1), 2),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]))
    s.append(t)
    unused = [t_ for t_ in C.MATCHING_TERMS if t_ not in [x[1] for x in C.MATCHING_ITEMS]]
    s.append(Paragraph("Never used: " + ", ".join(unused) + ".", st_small))

    s += part_heading("B", "Multiple Choice", PTS["mc"])
    for num, (_, opts, correct) in zip(NUM["mc"], C.MULTIPLE_CHOICE):
        s.append(Paragraph(f"<b>{num}.</b>  <b>{'abcd'[correct]}</b>  {opts[correct]}", st_ans))

    s += part_heading("C", "Fill in the Blank", PTS["fill"])
    for num, (_, ans) in zip(NUM["fill"], C.FILL_IN):
        s.append(Paragraph(f"<b>{num}.</b>  " + ";  ".join(ans), st_ans))

    s += part_heading("D", "True or False", PTS["tf"])
    for num, (_, is_true, why) in zip(NUM["tf"], C.TRUE_FALSE):
        s.append(Paragraph(f"<b>{num}.</b>  <b>{'T' if is_true else 'F'}</b>  "
                           f"<font color='#55575E'>{why}</font>", st_ans))

    blk = part_heading("E", "Worldview Chart", PTS["chart"])
    hc = ParagraphStyle("hc2", parent=st_cellb, alignment=TA_CENTER, textColor=colors.white)
    data = [[Paragraph("", hc), Paragraph("CHRISTIANS", hc), Paragraph("NATURALISTS", hc)]]
    ex = C.CHART_EXAMPLE
    data.append([Paragraph(ex[0], st_cellb), Paragraph(ex[1] + "  (given)", st_cell),
                 Paragraph(ex[2] + "  (given)", st_cell)])
    it = iter(NUM["chart"])
    for label, ac, an in C.CHART_ROWS:
        a, b = next(it), next(it)
        data.append([Paragraph(label, st_cellb), Paragraph(f"({a})  <b>{ac}</b>", st_cell),
                     Paragraph(f"({b})  <b>{an}</b>", st_cell)])
    ct = Table(data, colWidths=[1.75 * inch, 2.625 * inch, 2.625 * inch])
    ct.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.8, RULE),
                            ("BACKGROUND", (0, 0), (-1, 0), LCA_BLUE),
                            ("BACKGROUND", (0, 1), (-1, 1), TINT),
                            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                            ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                            ("LEFTPADDING", (0, 0), (-1, -1), 6)]))
    blk.append(ct)
    s.append(KeepTogether(blk))

    blk = part_heading("F", "Levels of Classification", PTS["cls"])
    order = ", ".join(f"{i + 1}) {l}" for i, l in enumerate(C.CLASSIFICATION_LEVELS))
    blk.append(Paragraph(f"<b>{NUM['cls']}.</b>  {order}", st_ans))
    blk.append(Paragraph(f"Memory trick: <i>{C.CLASSIFICATION_MNEMONIC}</i>. One point per level in the "
                         "correct position.", st_small))
    s.append(KeepTogether(blk))

    s += part_heading("G", "Select and Order", PTS["short"])
    s.append(Paragraph("Circle-all questions: 3 points if every correct choice is circled and nothing extra, then "
                       "take off 1 point for each miss or extra circle, never below 0. Number-the-steps: 3 points "
                       "for all four in order, 2 for three, 1 for one or two.", st_instr))
    for num, q in zip(NUM["short"], C.SHORT_ANSWER):
        blk = [Paragraph(f"<b>{num}.</b>  <i>{q['q']}</i>", st_ans)]
        if q["type"] == "multi":
            letters = "abcdefghij"
            right = [(letters[i], txt) for i, (txt, ok) in enumerate(q["options"]) if ok]
            blk.append(Paragraph("<b>" + ", ".join(l for l, _ in right) + "</b>:  " +
                                 "; ".join(f"{l}) {t}" for l, t in right), st_model))
        elif q["type"] == "order":
            numbered = ", ".join(f"{q['steps'].index(st) + 1} {st}" for st in q["shown"])
            blk.append(Paragraph(f"As printed on the test: <b>{numbered}</b>. "
                                 f"Correct order: {', '.join(q['steps'])}.", st_model))
        else:
            blk.append(Paragraph(f"<b>{'abcd'[q['a']]}</b>  {q['options'][q['a']]}", st_model))
        s.append(KeepTogether(blk))

    s.append(Spacer(1, 10))
    notes = [Table([[""]], colWidths=[BODY_W], rowHeights=[2])]
    notes[0].setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, -1), 1.6, LCA_BLUE)]))
    notes.append(Spacer(1, 6))
    notes.append(Paragraph("<b><font color='#253A7E'>NOTES FOR RYAN</font></b>", st_body))
    for line in C.NOTES_FOR_PARENT:
        notes.append(Paragraph("-  " + line, st_note))
    s.append(KeepTogether(notes))

    doc = make_doc(KEY_PDF, "LCA Life Science Chapter 1 Practice Test - Answer Key")
    doc.build(s, onFirstPage=make_header_footer("Answer Key"), onLaterPages=make_header_footer("Answer Key"))


if __name__ == "__main__":
    build_test()
    build_key()
    print("items", TOTAL_ITEMS, "points", PTS)
    print("wrote", TEST_PDF)
    print("wrote", KEY_PDF)
