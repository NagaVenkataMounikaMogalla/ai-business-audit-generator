from fpdf import FPDF
import os


def generate_pdf(company_name, insights):

    current_dir = os.getcwd()

    folder_path = os.path.join(current_dir, "generated_reports")

    if not os.path.isdir(folder_path):

        if os.path.exists(folder_path):
            os.remove(folder_path)

        os.mkdir(folder_path)

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", "B", 20)

    pdf.cell(200, 10, f"{company_name} AI Business Audit", ln=True)

    pdf.ln(10)

    pdf.set_font("Arial", size=12)

    clean_text = insights.encode("latin-1", "replace").decode("latin-1")

    pdf.multi_cell(0, 10, clean_text)

    file_path = os.path.join(
        folder_path,
        f"{company_name}_report.pdf"
    )

    pdf.output(file_path)

    return file_path