import pdfplumber

print("devdom5222")  

def pullpdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text() + '\n'
    return text

def write_to_textfile(text, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(text)

if __name__ == "__main__":
    pdf_path = "USCensus.pdf"
    output_path = "USCensus_Output.txt"
    text = pullpdf(pdf_path)
    write_to_textfile(text, output_path)
