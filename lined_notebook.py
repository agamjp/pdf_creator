from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="a4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=16)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=13, txt=f"{row['Order']}. {row['Topic']}", align="L", ln=1)
    pdf.set_font(family="Times", size=14)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=10, txt="Notes:", align="L", ln=1, )
    for i in range(21, 282, 10):
        pdf.line(10, i, 200, i)
    pdf.ln(249)
    pdf.set_font(family="Times", size=10)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=11, txt=f"{row['Topic']} | Page 1", align="C", ln=1)
    for p in range(row["Pages"]):
        pdf.add_page()
        pdf.set_font(family="Times", size=14)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=16, txt="Notes:", align="L", ln=1)
        for i in range(21, 281, 10):
            pdf.line(10, i, 200, i)
        pdf.ln(260)
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=11, txt=f"{row['Topic']} | Page {p + 2}", align="C", ln=1)
pdf.output("lined.pdf")

