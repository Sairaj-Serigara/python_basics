from pypdf import PdfWriter

merger = PdfWriter()

for pdf in ["MODULE 3.pdf", "Module1_RM.pdf", "Module2_RM.pdf"]:
    merger.append(pdf)

merger.write("research-ia-1.pdf")
merger.close()