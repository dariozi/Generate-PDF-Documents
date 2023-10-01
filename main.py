from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="Left", ln=1)
    #Generate line every 10mm, starting at 20mm until 297mm per page, increasing 10mm
    for y in range(20, 297, 10):
        pdf.line(10, y, 200, y)


    #Footer - LN is different for the first page because of the header
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    #we add the -1 because the first page was created above
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        # Footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
        for y in range(20, 297, 10):
            pdf.line(10, y, 200, y)

pdf.output("output.pdf")