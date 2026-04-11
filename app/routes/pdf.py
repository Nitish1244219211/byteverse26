from flask import Blueprint, request, send_file
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from app.models import patients
from reportlab.platypus import Table, TableStyle

from app.services.hospital import get_hospitals_by_department

import io

pdf = Blueprint("pdf", __name__)

@pdf.route("/download_pdf", methods=["POST"])
def download_pdf():

    data = request.get_json()

    hospital = data["hospital"]
    department = data["department"]
    disease = data["disease"]
    token = data["token"]

    patient = patients.query.filter_by(access_token=token).first()

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    content = []
    # Hospital title
    content.append(Paragraph(f"<b>{hospital}</b>", styles["Title"]))
    content.append(Spacer(1, 1))

    table_data = [
        [
            f"Patient ID: {patient.sno}\n"
            f"Name: {patient.name}\n"
            f"Age: {patient.age}\n"
            f"Sex: {patient.sex or 'N/A'}\n"
            f"Mobile: {patient.mobile}",


            f"Disease: {disease}\n"
            f"Department: {department}\n"
            f"Symptoms: {patient.desc}"
        ]
    ]

    table = Table(table_data, colWidths=[250, 250])

    table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))

    content.append(table)
    doc.build(content)
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="receipt.pdf",
        mimetype="application/pdf"
    )