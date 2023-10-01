from fpdf import FPDF

# Create the PDF instance, as Portraid, all dimension in mm and format A4
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Add a page, at least one page is needed
pdf.add_page()

# Set font of the cell below until a new set_font is set
pdf.set_font(family="Times", style="B", size=12)

# Adding text through cells
pdf.cell(w=0, h=12, txt="Hello There", align="L", ln=1)

pdf.set_font(family="Times", size=12)
pdf.cell(w=0, h=12, txt="Hi There", align="L", ln=1)

# Generate the PDF when NAME.pdf is the name of the file
pdf.output("output.pdf")
