from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="a4")
pdf.set_auto_page_break(auto=False, margin=0)

topics = pd.read_csv("topics.csv")

for index, row in topics.iterrows():
    pdf.add_page()
    pdf.set_font(family="Arial", style="B", size=14)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=14, txt=f"{row['Order']}. {row['Topic']}", align="L", ln=1)
    pdf.line(10, 20, 200, 20)

    pdf.set_font(family="Arial", size=12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt="Notes:", align="L", ln=1)

    pdf.ln(240)
    pdf.set_font(family="Arial", size=10, style="I")
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=f"{row['Topic']} | Page 1", align="R", ln=1)

    for p in range(row["Pages"]-1):
        pdf.add_page()
        pdf.set_font(family="Arial", size=12)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=0, txt="Notes:", align="L", ln=1)

        pdf.ln(266)
        pdf.set_font(family="Arial", size=10, style="I")
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=f"{row['Topic']} | Page {p + 2}",
                 align="R", ln=1)
pdf.output("output.pdf")
