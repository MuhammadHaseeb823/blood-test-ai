from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
import io


def generate_pdf(data, results):

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    title_style = styles["Title"]

    cell_style = ParagraphStyle(
        name="cell",
        fontSize=9,
        leading=11,
        alignment=TA_LEFT
    )

    section_title = ParagraphStyle(
        name="section",
        fontSize=12,
        leading=14,
        spaceAfter=6,
        textColor=colors.HexColor("#2E5AAC"),
        bold=True
    )

    disclaimer = (
        "⚠️ Disclaimer: This report is strictly for educational purposes only and "
        "should not be used as a substitute for professional medical advice, diagnosis, or treatment."
    )

    content = []

    # =========================
    # HEADER
    # =========================
    content.append(Paragraph("🏥 Clinical Diagnostic Report", title_style))
    content.append(Spacer(1, 10))

    content.append(Paragraph(f"Gender: {data.get('gender','N/A')}", styles["Normal"]))
    content.append(Paragraph(f"Timestamp: {data.get('timestamp','N/A')}", styles["Normal"]))

    content.append(Spacer(1, 10))
    content.append(Paragraph(disclaimer, styles["Normal"]))
    content.append(Spacer(1, 15))

    # =========================
    # RBC SECTION
    # =========================
    content.append(Paragraph("🩸 Red Blood Cell (RBC) Profile", section_title))

    rbc_table = [
        ["RBC", data.get("rbc", "N/A"),
         "Hb", data.get("hb", "N/A")],
        ["MCV", data.get("mcv", "N/A"),
         "Hematocrit", data.get("hct", "N/A")]
    ]

    content.append(Table(rbc_table, colWidths=[100, 100, 100, 100]))
    content.append(Spacer(1, 10))

    # =========================
    # WBC SECTION
    # =========================
    content.append(Paragraph("🧬 White Blood Cell (WBC) Profile", section_title))

    wbc_table = [
        ["WBC", data.get("wbc", "N/A"),
         "Neutrophils", data.get("neutrophils", "N/A")],
        ["Lymphocytes", data.get("lymphocyte_count", "N/A"),
         "Monocytes", data.get("monocyte_number", "N/A")],
        ["CRP", data.get("crp", "N/A"),
         "ESR", data.get("esr", "N/A")]
    ]

    content.append(Table(wbc_table, colWidths=[100, 100, 100, 100]))
    content.append(Spacer(1, 10))

    # =========================
    # LIVER SECTION
    # =========================
    content.append(Paragraph("🫀 Liver Function Tests", section_title))

    liver_table = [
        ["Bilirubin", data.get("total_bilirubin", "N/A"),
         "Albumin", data.get("albumin", "N/A")],
        ["LDH", data.get("ldh", "N/A"), "", ""]
    ]

    content.append(Table(liver_table, colWidths=[100, 100, 100, 100]))
    content.append(Spacer(1, 10))

    # =========================
    # KIDNEY SECTION
    # =========================
    content.append(Paragraph("🧪 Kidney Function Tests", section_title))

    kidney_table = [
        ["Urea", data.get("urea", "N/A"),
         "Creatinine", data.get("creatinine", "N/A")],
        ["Calcium", data.get("calcium", "N/A"),
         "Osmolality", data.get("osmolality", "N/A")]
    ]

    content.append(Table(kidney_table, colWidths=[100, 100, 100, 100]))
    content.append(Spacer(1, 15))

    # =========================
    # RESULTS TABLE
    # =========================
    content.append(Paragraph("📊 Diagnostic Findings", section_title))

    table_data = [["Condition", "Suggestion 1", "Suggestion 2"]]

    for r in results:
        table_data.append([
            Paragraph(r["condition"], cell_style),
            Paragraph(r.get("suggestion_1", "N/A"), cell_style),
            Paragraph(r.get("suggestion_2", "N/A"), cell_style)
        ])

    table = Table(table_data, colWidths=[160, 200, 200])

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2E5AAC")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1),
         [colors.whitesmoke, colors.lightgrey]),
    ]))

    content.append(table)

    # =========================
    # FOOTER DISCLAIMER
    # =========================
    content.append(Spacer(1, 20))
    content.append(Paragraph(disclaimer, styles["Normal"]))

    doc.build(content)

    buffer.seek(0)
    return buffer