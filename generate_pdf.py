import os
import re
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image, HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        if self._pageNumber == 1:
            # Cover page - no headers/footers
            return

        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#003399"))

        # Running Header
        self.drawString(40, 755, "INSTITUTO TECNOLÓGICO DE EXCELENCIA EDUCATIVA (ITEE)")
        self.setFont("Helvetica-Oblique", 8)
        self.setFillColor(colors.HexColor("#555555"))
        self.drawRightString(572, 755, "Informe Técnico: CYBER NEXUS 3D")

        # Header Line
        self.setStrokeColor(colors.HexColor("#003399"))
        self.setLineWidth(1)
        self.line(40, 748, 572, 748)
        self.setStrokeColor(colors.HexColor("#FFCC00"))
        self.setLineWidth(2)
        self.line(40, 746, 572, 746)

        # Footer Line
        self.setStrokeColor(colors.HexColor("#CCCCCC"))
        self.setLineWidth(0.5)
        self.line(40, 45, 572, 45)

        # Footer Text
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#555555"))
        self.drawString(40, 32, "Desarrollado por: José Ortiz (12vo PRG) | ¡Dios los bendiga!")
        
        page_str = f"Página {self._pageNumber} de {page_count}"
        self.drawRightString(572, 32, page_str)

        self.restoreState()


def create_professional_pdf(md_filename, pdf_filename, logo_filename):
    if not os.path.exists(md_filename):
        print(f"Error: {md_filename} no existe.")
        return

    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=letter,
        rightMargin=40, leftMargin=40,
        topMargin=50, bottomMargin=50
    )

    styles = getSampleStyleSheet()

    # Color Palette
    PRIMARY_BLUE = colors.HexColor("#003399")
    GOLD_YELLOW = colors.HexColor("#FFCC00")
    DARK_TEXT = colors.HexColor("#1A1A2E")
    LIGHT_BG = colors.HexColor("#F4F7FB")
    BORDER_COLOR = colors.HexColor("#D0DDF0")

    # Custom Typography Styles
    title_cover_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=PRIMARY_BLUE,
        alignment=1, # Center
        spaceAfter=8
    )

    slogan_style = ParagraphStyle(
        'CoverSlogan',
        parent=styles['Normal'],
        fontName='Helvetica-BoldOblique',
        fontSize=12,
        leading=15,
        textColor=colors.HexColor("#0055CC"),
        alignment=1,
        spaceAfter=15
    )

    subtitle_cover_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor("#333333"),
        alignment=1,
        spaceAfter=15
    )

    project_banner_style = ParagraphStyle(
        'ProjectBanner',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=colors.white,
        alignment=1,
        spaceBefore=6,
        spaceAfter=6
    )

    meta_label_style = ParagraphStyle(
        'MetaLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=PRIMARY_BLUE
    )

    meta_value_style = ParagraphStyle(
        'MetaValue',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=DARK_TEXT
    )

    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=PRIMARY_BLUE,
        spaceBefore=16,
        spaceAfter=8,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor("#0055AA"),
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        textColor=DARK_TEXT,
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'BulletCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        textColor=DARK_TEXT,
        leftIndent=15,
        spaceAfter=4
    )

    formula_style = ParagraphStyle(
        'FormulaCustom',
        parent=styles['Normal'],
        fontName='Courier-Oblique',
        fontSize=9.5,
        leading=13,
        textColor=PRIMARY_BLUE,
        alignment=1,
        spaceBefore=4, spaceAfter=4
    )

    story = []

    # ==================== PORTADA FORMAL ====================
    # Top Gold & Blue Lines
    story.append(HRFlowable(width="100%", thickness=4, color=PRIMARY_BLUE, spaceAfter=2))
    story.append(HRFlowable(width="100%", thickness=2, color=GOLD_YELLOW, spaceAfter=15))

    # School Logo
    if os.path.exists(logo_filename):
        img = Image(logo_filename, width=170, height=170)
        img.hAlign = 'CENTER'
        story.append(img)
        story.append(Spacer(1, 10))

    story.append(Paragraph("INSTITUTO TECNOLÓGICO DE EXCELENCIA EDUCATIVA", title_cover_style))
    story.append(Paragraph("¡Evolucionando la Educación!", slogan_style))
    story.append(HRFlowable(width="60%", thickness=1, color=BORDER_COLOR, spaceAfter=12))

    story.append(Paragraph("INFORME TÉCNICO DE PROYECTO DE SOFTWARE", subtitle_cover_style))

    # Project Title Box (Styled Table)
    proj_title_p = Paragraph("CYBER NEXUS 3D: OMEGA ASCENT", project_banner_style)
    proj_sub_p = Paragraph("Arcade 2D/3D Shooter con HTML5 Canvas & Web Audio API", ParagraphStyle('SubBanner', parent=project_banner_style, fontSize=11, fontName='Helvetica-Oblique'))
    
    banner_table = Table([[proj_title_p], [proj_sub_p]], colWidths=[520])
    banner_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), PRIMARY_BLUE),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LINEBELOW', (0,0), (-1,0), 1, GOLD_YELLOW),
        ('BOX', (0,0), (-1,-1), 2, PRIMARY_BLUE),
    ]))
    story.append(banner_table)
    story.append(Spacer(1, 20))

    # Metadata Card Box
    meta_data = [
        [Paragraph("INSTITUCIÓN:", meta_label_style), Paragraph("Instituto Tecnológico de Excelencia Educativa (ITEE)", meta_value_style)],
        [Paragraph("CARRERA:", meta_label_style), Paragraph("Informática Orientada en la Programación", meta_value_style)],
        [Paragraph("ASIGNATURA:", meta_label_style), Paragraph("Programación de IA", meta_value_style)],
        [Paragraph("DESARROLLADOR:", meta_label_style), Paragraph("<b>José Ortiz</b> (12vo PRG)", meta_value_style)],
        [Paragraph("DOCENTE:", meta_label_style), Paragraph("Ing. Miklos Szabo", meta_value_style)],
        [Paragraph("FECHA DE ENTREGA:", meta_label_style), Paragraph("16 de Septiembre de 2026", meta_value_style)],
        [Paragraph("UBICACIÓN:", meta_label_style), Paragraph("San Pedro Sula, Cortés, Honduras", meta_value_style)],
    ]
    meta_table = Table(meta_data, colWidths=[140, 360])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('PADDING', (0,0), (-1,-1), 6),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('LINELEFT', (0,0), (0,-1), 4, PRIMARY_BLUE),
    ]))
    story.append(meta_table)

    story.append(Spacer(1, 25))
    story.append(HRFlowable(width="100%", thickness=2, color=GOLD_YELLOW, spaceAfter=2))
    story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY_BLUE, spaceAfter=0))

    # End of Cover Page
    story.append(PageBreak())

    # ==================== CONTENIDO DEL INFORME ====================
    with open(md_filename, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    in_table = False
    table_raw_data = []

    # Skip Cover Markdown text in body parsing
    skip_until_content = False

    for line in lines:
        line_str = line.strip()

        if "PORTADA FORMATO UNIVERSITARIO" in line_str:
            skip_until_content = True
            continue

        if skip_until_content:
            if "TABLA DE ENLACES DE ENTREGA" in line_str or line_str.startswith("## 1."):
                skip_until_content = False
            else:
                continue

        if not line_str:
            if in_table and table_raw_data:
                # Render formatted table
                t = Table(table_raw_data, colWidths=[150, 80, 270])
                t.setStyle(TableStyle([
                    ('BACKGROUND', (0,0), (-1,0), PRIMARY_BLUE),
                    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
                    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
                    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0,0), (-1,-1), 9),
                    ('PADDING', (0,0), (-1,-1), 6),
                    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG]),
                    ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
                ]))
                story.append(Spacer(1, 4))
                story.append(t)
                story.append(Spacer(1, 10))
                in_table = False
                table_raw_data = []
            continue

        if line_str.startswith('|') and line_str.endswith('|'):
            if '---' in line_str:
                continue
            cells = [c.strip() for c in line_str.split('|')[1:-1]]
            p_cells = [Paragraph(re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', c), body_style) for c in cells]
            table_raw_data.append(p_cells)
            in_table = True
            continue

        if line_str.startswith('## '):
            text = line_str[3:].replace('**', '')
            story.append(Paragraph(text, h1_style))
            story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY_BLUE, spaceAfter=6))
        elif line_str.startswith('### '):
            text = line_str[4:].replace('**', '')
            story.append(Paragraph(text, h2_style))
        elif line_str.startswith('$$') or line_str.startswith('X\' ='):
            text = line_str.replace('$$', '')
            formula_p = Paragraph(f"<b>Fórmula:</b> {text}", formula_style)
            f_table = Table([[formula_p]], colWidths=[500])
            f_table.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
                ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
                ('PADDING', (0,0), (-1,-1), 6),
                ('LINELEFT', (0,0), (0,-1), 3, GOLD_YELLOW),
            ]))
            story.append(f_table)
            story.append(Spacer(1, 6))
        elif line_str.startswith('* ') or line_str.startswith('- ') or (len(line_str) > 2 and line_str[0].isdigit() and line_str[1] == '.'):
            text = line_str
            if line_str.startswith('* ') or line_str.startswith('- '):
                text = line_str[2:]
            text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
            text = re.sub(r'`(.*?)`', r'<font face="Courier" color="#003399"><b>\1</b></font>', text)
            story.append(Paragraph(f"• {text}", bullet_style))
        else:
            if line_str == '---':
                story.append(Spacer(1, 6))
                continue
            text = line_str
            text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
            text = re.sub(r'`(.*?)`', r'<font face="Courier" color="#003399"><b>\1</b></font>', text)
            story.append(Paragraph(text, body_style))

    if in_table and table_raw_data:
        t = Table(table_raw_data, colWidths=[150, 80, 270])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), PRIMARY_BLUE),
            ('TEXTCOLOR', (0,0), (-1,0), colors.white),
            ('ALIGN', (0,0), (-1,-1), 'LEFT'),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('FONTSIZE', (0,0), (-1,-1), 9),
            ('PADDING', (0,0), (-1,-1), 6),
            ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG]),
            ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ]))
        story.append(t)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Éxito: PDF profesional generado en {pdf_filename}")

if __name__ == '__main__':
    create_professional_pdf('informe_tecnico.md', 'informe_tecnico.pdf', 'logo_itee.png')
