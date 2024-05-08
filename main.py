from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="a4")

pdf.add_page()
pdf.set_font(family="Arial", size=14)
pdf.cell(w=0, h=12, txt="Hello World!", align="L", ln=1, border=1)
pdf.set_font(family="Arial", size=12)
pdf.cell(w=0, h=12, txt="Hi there!", align="L", ln=1, border=1)
pdf.output("output.pdf")
