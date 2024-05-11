from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="a4")
topics = pd.read_csv("topics.csv")

for index, row in topics.iterrows():
    for p in range(row["Pages"]):
        pdf.add_page()
        pdf.set_font(family="Arial", style="B", size=14)
        pdf.cell(w=0, h=12, txt=f"{row['Order']}. {row['Topic']}", align="L", ln=1)
        pdf.line(10, 20, 200, 20)
        pdf.set_font(family="Arial", size=12)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=0, txt="\n\nNotes:", align="L", ln=1)
pdf.output("output.pdf")
