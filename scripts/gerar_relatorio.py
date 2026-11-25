"""Gera o PDF do relatório a partir do .md e do config.json (padrão Relatório Final Grupo 05)."""
import json, os, re, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import (CondPageBreak, Image as RLImage, KeepTogether, PageBreak, Paragraph,
                                Preformatted, SimpleDocTemplate, Spacer, Table, TableStyle)

HERE = os.path.dirname(os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else "config.json"))
CFG = json.load(open(sys.argv[1] if len(sys.argv) > 1 else "config.json", encoding="utf-8"))
SRC, OUT = os.path.join(HERE, CFG["md"]), os.path.join(HERE, CFG["pdf"])
W = 523  # largura útil em pontos (A4 com margens de 36)

# Fonte: Arial se existir; senão Liberation Sans (mesmas medidas da Arial)
def _font_dir():
    for d in ["/usr/share/fonts/truetype/msttcorefonts/", "/Library/Fonts/", "/System/Library/Fonts/Supplemental/"]:
        if os.path.exists(os.path.join(d, "Arial.ttf")):
            return d, ("Arial.ttf", "Arial Bold.ttf" if os.path.exists(os.path.join(d, "Arial Bold.ttf")) else "Arial_Bold.ttf",
                       "Arial Italic.ttf" if os.path.exists(os.path.join(d, "Arial Italic.ttf")) else "Arial_Italic.ttf",
                       "Arial Bold Italic.ttf" if os.path.exists(os.path.join(d, "Arial Bold Italic.ttf")) else "Arial_Bold_Italic.ttf")
    for d in ["/usr/share/fonts/truetype/liberation/", "/usr/share/fonts/truetype/liberation2/"]:
        if os.path.exists(os.path.join(d, "LiberationSans-Regular.ttf")):
            return d, ("LiberationSans-Regular.ttf", "LiberationSans-Bold.ttf", "LiberationSans-Italic.ttf", "LiberationSans-BoldItalic.ttf")
    raise SystemExit("Instale a fonte Arial ou Liberation Sans")
_d, _f = _font_dir()
for name, file in zip(("LSans", "LSans-Bold", "LSans-Italic", "LSans-BoldItalic"), _f):
    pdfmetrics.registerFont(TTFont(name, os.path.join(_d, file)))
pdfmetrics.registerFontFamily("LSans", normal="LSans", bold="LSans-Bold", italic="LSans-Italic", boldItalic="LSans-BoldItalic")


class NumberedCanvas(canvas.Canvas):
    def __init__(self, *a, **k):
        super().__init__(*a, **k); self._states = []
    def showPage(self):
        self._states.append(dict(self.__dict__)); self._startPage()
    def save(self):
        n = len(self._states)
        for st in self._states:
            self.__dict__.update(st); self.draw_page(n); super().showPage()
        super().save()
    def draw_page(self, total):
        if self._pageNumber == 1:  # capa sem cabeçalho e sem rodapé
            return
        self.saveState(); self.setFont("LSans", 8); self.setFillColor(colors.HexColor("#475569"))
        self.setStrokeColor(colors.HexColor("#CBD5E1")); self.setLineWidth(0.5)
        if self._pageNumber > 2:
            self.drawString(36, 810, CFG.get("cabecalho_esq", "")); self.drawRightString(559, 810, CFG.get("cabecalho_dir", ""))
            self.line(36, 804, 559, 804)
        self.line(36, 40, 559, 40)
        self.drawString(36, 28, CFG.get("rodape", "")); self.drawRightString(559, 28, f"Página {self._pageNumber} de {total}")
        self.restoreState()


S = getSampleStyleSheet()
def PS(name, **k):
    return ParagraphStyle(name, parent=S["Normal"], fontName=k.pop("fontName", "LSans"), **k)
inst_header = PS("Inst", fontName="LSans-Bold", fontSize=9.5, leading=13, alignment=TA_CENTER, textColor=colors.HexColor("#1E3A8A"))
doc_title = PS("DocTitle", fontName="LSans-Bold", fontSize=12, leading=15.5, alignment=TA_CENTER, textColor=colors.HexColor("#0F172A"), spaceAfter=10)
h2 = PS("H2", fontName="LSans-Bold", fontSize=10, leading=14, textColor=colors.HexColor("#1E3A8A"), spaceBefore=9, spaceAfter=3.5, keepWithNext=1)
h3 = PS("H3", fontName="LSans-Bold", fontSize=8.8, leading=12, textColor=colors.HexColor("#1E293B"), spaceBefore=5.5, spaceAfter=2.5, keepWithNext=1)
body = PS("Body", fontSize=8.3, leading=12.2, alignment=TA_JUSTIFY, textColor=colors.HexColor("#1E293B"), spaceAfter=3.8)
bullet = PS("Bullet", fontSize=8.3, leading=12.2, leftIndent=11, spaceAfter=2.8, textColor=colors.HexColor("#1E293B"))
meta_l = PS("MetaL", fontName="LSans-Bold", fontSize=7.8, leading=10.2, textColor=colors.HexColor("#1E293B"))
meta_v = PS("MetaV", fontSize=7.8, leading=10.2, textColor=colors.HexColor("#334155"))
cell = PS("Cell", fontSize=7.2, leading=9.2, textColor=colors.HexColor("#1E293B"))
cell_c = PS("CellC", fontSize=7.2, leading=9.2, alignment=TA_CENTER, textColor=colors.HexColor("#1E293B"))
cell_h = PS("CellH", fontName="LSans-Bold", fontSize=7.2, leading=9.2, alignment=TA_CENTER, textColor=colors.white)
ref = PS("Ref", fontSize=7.6, leading=10.5, alignment=TA_LEFT, textColor=colors.HexColor("#334155"), leftIndent=14, firstLineIndent=-14, spaceAfter=3.2)
cap = PS("Cap", fontName="LSans-Bold", fontSize=7.8, leading=10, alignment=TA_CENTER, spaceBefore=4, spaceAfter=3)
fonte = PS("Fonte", fontSize=7.0, leading=9, alignment=TA_LEFT, spaceBefore=1, spaceAfter=6)
foto_leg = PS("FotoLeg", fontSize=7.2, leading=9, alignment=TA_CENTER)
code_st = ParagraphStyle("Code", parent=S["Normal"], fontName="Courier", fontSize=6.8, leading=8.6)


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
def inline(s):
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", s)
    s = re.sub(r"(https?://[^\s<]+?)([.,;)]?)(?=\s|$)", r'<link href="\1" color="#1D4ED8">\1</link>\2', s)
    return s
def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]
def is_sep(line):
    return bool(re.match(r"^\|\s*:?-{2,}", line.strip()))


def col_widths(rows):
    n = len(rows[0])
    w = [min(max(max(len(r[c]) if c < len(r) else 0 for r in rows), 4), 70) for c in range(n)]
    fixed = {c: 36 for c in range(n) if max(len(r[c]) if c < len(r) else 0 for r in rows) <= 8}
    rest = sum(w[c] for c in range(n) if c not in fixed) or 1
    avail = W - sum(fixed.values())
    out = [fixed.get(c, avail * w[c] / rest) for c in range(n)]
    mins = []
    for c in range(n):
        m = 0
        for i, r in enumerate(rows):
            if c < len(r):
                f, sz = (("LSans-Bold", 7.2) if i == 0 else ("LSans", 7.2))
                m = max(m, max((stringWidth(x, f, sz) for x in re.sub(r"[*`]", "", r[c]).split()), default=0))
        mins.append(m * 1.08 + 12)
    out = [max(o, m) for o, m in zip(out, mins)]
    ex = sum(out) - W
    if ex > 0:
        slack = [max(o - m, 0) for o, m in zip(out, mins)]; ss = sum(slack)
        if ss >= ex:
            out = [o - ex * s / ss if s > 0 else o for o, s in zip(out, slack)]
        else:
            print("AVISO: tabela mais larga que a página; reduza o texto das células")
    return out


def build_table(rows):
    widths = col_widths(rows)
    if rows[0][0].strip() == "Atividade" and len(rows[0]) > 10:  # gráfico de Gantt
        widths = [165] + [(W - 165) / (len(rows[0]) - 1)] * (len(rows[0]) - 1)
    n = len(rows[0])
    short = [all(len(r[c] if c < len(r) else "") <= 8 for r in rows[1:]) for c in range(n)]
    data, gantt = [], []
    for i, row in enumerate(rows):
        line = []
        for c in range(n):
            t = row[c] if c < len(row) else ""
            if i > 0 and t.strip() == "X":
                gantt.append((c, i)); line.append(Paragraph("", cell_c))
            elif i == 0:
                line.append(Paragraph(inline(t), cell_h))
            else:
                line.append(Paragraph(inline(t), cell_c if short[c] and t else cell))
        data.append(line)
    tb = Table(data, colWidths=widths, repeatRows=1)
    st = [("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1E3A8A")), ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
          ("TOPPADDING", (0, 0), (-1, -1), 2.2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.2),
          ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4)]
    st += [("BACKGROUND", (0, r), (-1, r), colors.HexColor("#F8FAFC")) for r in range(2, len(rows), 2)]
    st += [("BACKGROUND", (c, r), (c, r), colors.HexColor("#2563EB")) for c, r in gantt]
    tb.setStyle(TableStyle(st))
    return tb


def build_meta(rows):
    tb = Table([[Paragraph(inline(r[0]), meta_l), Paragraph(inline(r[1] if len(r) > 1 else ""), meta_v)] for r in rows], colWidths=[150, 373])
    tb.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F8FAFC")), ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
                            ("TOPPADDING", (0, 0), (-1, -1), 2.2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.2),
                            ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5)]))
    return tb


def image(path, width):
    from PIL import Image as PI
    p = os.path.join(HERE, path)
    w0, h0 = PI.open(p).size
    h = width * h0 / w0
    if h > 600:  # imagem muito alta: limitar à página
        width, h = width * 600 / h, 600
    return RLImage(p, width=width, height=h)


def photo_grid(spec):
    """@FOTOS|arquivo.jpg::Nome;arquivo2.jpg::Nome 2 -> grade com 3 fotos por linha."""
    items = [x.split("::") for x in spec.split(";") if x.strip()]
    cells = []
    for it in items:
        path, name = it[0].strip(), (it[1].strip() if len(it) > 1 else "")
        img = image(path, 140)
        if img.drawHeight > 170:
            img = RLImage(os.path.join(HERE, path), width=140 * 170 / img.drawHeight, height=170)
        cells.append([img, Paragraph(esc(name), foto_leg)])
    rows = [cells[i:i + 3] for i in range(0, len(cells), 3)]
    rows = [r + [""] * (3 - len(r)) for r in rows]
    tb = Table(rows, colWidths=[W / 3] * 3)
    tb.setStyle(TableStyle([("ALIGN", (0, 0), (-1, -1), "CENTER"), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
    return tb


def build_cover(story):
    c = CFG["capa"]
    inst = PS("CI", fontName="LSans-Bold", fontSize=12, leading=14.5)
    c12 = PS("C12", fontName="LSans-Bold", fontSize=12, leading=15, alignment=TA_CENTER)
    c14 = PS("C14", fontName="LSans-Bold", fontSize=14, leading=19, alignment=TA_CENTER)
    top = Paragraph("<br/>".join(esc(x) for x in c["instituicao"]), inst)
    if c.get("logo") and os.path.exists(os.path.join(HERE, c["logo"])):
        logo = image(c["logo"], 60)
        head = Table([[top, logo]], colWidths=[440, 83])
    else:
        head = Table([[top]], colWidths=[W])
    head.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("ALIGN", (-1, 0), (-1, 0), "RIGHT"),
                              ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0)]))
    extra = max(len(c["integrantes"]) - 3, 0) * 15
    story += [head, Spacer(1, 170 - extra / 3), Paragraph(esc(c["titulo"]), c14), Paragraph(esc(c["tema"]), c14),
              Spacer(1, 150 - extra / 3)]
    if c.get("grupo"):
        story.append(Paragraph(esc(c["grupo"]), c12))
    story += [Paragraph(esc(x), c12) for x in c["integrantes"]]
    story += [Spacer(1, 150 - extra / 3), Paragraph(esc(c["cidade"]), c12), Paragraph(esc(c["data"]), c12), PageBreak()]


def main():
    lines = open(SRC, encoding="utf-8").read().split("\n")
    doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=36, rightMargin=36, topMargin=46, bottomMargin=50, title=CFG["capa"]["tema"])
    story, pending, in_refs, i, head_done = [], None, False, 0, False
    build_cover(story)

    def put(flow):
        nonlocal pending
        if pending is not None:
            story.append(KeepTogether([pending, flow])); pending = None
        else:
            story.append(flow)

    while i < len(lines):
        line = lines[i].rstrip()
        if not head_done and line.startswith("# ") and i + 1 < len(lines) and lines[i + 1].startswith("**"):
            story += [Paragraph(esc(line[2:]) + "<br/>" + esc(lines[i + 1].strip("* ")), inst_header), Spacer(1, 8)]
            head_done = True; i += 2; continue
        if line.strip() == "<!-- quebra -->":
            story.append(PageBreak()); i += 1; continue
        if line.startswith("```"):
            code = []; i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                code.append(lines[i]); i += 1
            i += 1
            box = Table([[Preformatted("\n".join(code), code_st)]], colWidths=[W])
            box.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F8FAFC")), ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1"))]))
            put(box); story.append(Spacer(1, 4)); continue
        if line.startswith("@CAP|"):
            pending = Paragraph(esc(line[5:].strip()), cap); i += 1; continue
        if line.startswith("@IMG|"):
            parts = line[5:].split("|")
            put(image(parts[0].strip(), float(parts[1]) if len(parts) > 1 and parts[1].strip() else W)); i += 1; continue
        if line.startswith("@FOTOS|"):
            put(photo_grid(line[7:])); i += 1; continue
        if line.startswith("@FONTE|"):
            story.append(Paragraph(esc(line[7:].strip()), fonte)); i += 1; continue
        if line.startswith("@TOC|"):
            _, lvl, ttl, pg = line.split("|", 3)
            f = "LSans-Bold" if lvl == "2" else "LSans"; ind = 0 if lvl == "2" else 18
            dots = max(int((W - ind - stringWidth(pg, f, 8.3) - 16 - stringWidth(ttl, f, 8.3)) / stringWidth(".", f, 8.3)), 3)
            story.append(Paragraph(esc(ttl) + " " + "." * dots + " " + pg, PS("T" + lvl, fontName=f, fontSize=8.3, leftIndent=ind, leading=10, spaceAfter=0.8)))
            i += 1; continue
        if line.startswith("|"):
            block = []
            while i < len(lines) and lines[i].startswith("|"):
                block.append(lines[i]); i += 1
            rows = [split_row(b) for b in block if not is_sep(b)]
            if rows[0][0] == "Campo":
                story.append(build_meta(rows[1:]))
            elif pending is not None and len(rows) > 12:  # tabela longa: pode continuar na página seguinte
                story += [CondPageBreak(90), pending, build_table(rows)]; pending = None
            else:
                put(build_table(rows))
            story.append(Spacer(1, 7)); continue
        if line.startswith("# "):
            story.append(Paragraph(inline(line[2:]), doc_title))
        elif line.startswith("## "):
            t = line[3:].strip(); in_refs = bool(re.match(r"^(\d+\s*)?(REFERÊNCIAS|BIBLIOGRAFIA)", t))
            story.append(Paragraph(inline(t), doc_title if t == "SUMÁRIO" else h2))
        elif line.startswith("### "):
            story.append(Paragraph(inline(line[4:]), h3))
        elif line.startswith("- "):
            story.append(Paragraph("• " + inline(line[2:]), bullet))
        elif line.strip() in ("", "---"):
            pass
        else:
            story.append(Paragraph(inline(line.strip()), ref if in_refs else body))
        i += 1
    doc.build(story, canvasmaker=NumberedCanvas)
    print("PDF gerado:", OUT)


if __name__ == "__main__":
    main()
