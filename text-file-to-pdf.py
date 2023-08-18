from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", size=10)

with open("tabulate-table.txt", "r") as fp:
  lineNum = 1
  for line in fp:
    pdf.cell(200,10,txt=line,ln=lineNum, align="C")
    lineNum += 1

pdf.output("tabulate-table.pdf")