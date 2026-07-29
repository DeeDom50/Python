# ReadPDF.py
import pdfplumber

pdfToString = ""
pdf_path = "/Users/devante/Library/CloudStorage/OneDrive-ECPIUniversity/Desktop/dDominicci_cis_123/SimplePDF.pdf"
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        string = page.extract_text()
        pdfToString += string

with open("/Users/devante/Library/CloudStorage/OneDrive-ECPIUniversity/Desktop/dDominicci_cis_123/Small.txt", "w") as f:
    f.write(pdfToString)
