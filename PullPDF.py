import pdfplumber

print("devdom5222")  

def pullpdf(pdf):
    pull = pdfplumber.open(pdf)
    return pull

def writepdf(pdf):
    with open("Complex_Output.txt", "w", encoding='utf-8') as f:
        for page in pdf.pages:
            f.write(page.extract_text() + '\n')

# Open and extract text from all pages of ComplexPDF.pdf and write to a file
pdf = pullpdf("ComplexPDF.pdf")
writepdf(pdf)

# Close the PDF after processing
pdf.close()