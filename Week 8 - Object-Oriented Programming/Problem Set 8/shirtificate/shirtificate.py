from fpdf import FPDF

# Get name from user
name = input("Name: ")

pdf = FPDF(orientation="portrait", format="A4")
pdf.add_page()

# Add "CS50 Shirtificate" text
pdf.set_font("helvetica", "B", size=50)
pdf.cell(0, 30, "CS50 Shirtificate", align="C")

# Add image
pdf.image("shirtificate.png", x=0, y=60)

# Add "(name) took CS50"
pdf.set_font("helvetica", size=30)
pdf.set_text_color(255, 255, 255)
pdf.cell(-185, 250, f"{name} took CS50", align="C")

# Save pdf
pdf.output("shirtificate.pdf")
