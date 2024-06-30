from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(file_name, contents):
    c = canvas.Canvas(file_name, pagesize=letter)
    width, height = letter
    for i, page in enumerate(contents):
        text = c.beginText(40, height - 40)
        for line in page.split('\n'):
            text.textLine(line)
        c.drawText(text)
        if i < len(contents) - 1:
            c.showPage()
    c.save()

simple_pdf_content = [
    """This is a simple PDF document.
It only contains a single page of text.
The purpose of this document is to test the basic functionality of PDF text extraction.
Thank you for reading."""
]

medium_pdf_content = [
    """This is the first page of a medium complexity PDF document.
It contains multiple pages and some structured text.""",
    """This is the second page of the medium PDF document.
The purpose is to test the extraction of text across multiple pages.""",
    """This is the third and final page of the medium PDF document.
Thank you for reading this medium complexity PDF."""
]

complex_pdf_content = [
    """This is a complex PDF document.
It contains multiple pages with more structured and detailed text.
The purpose is to test the extraction of text from a more complex document.""",
    """The second page of the complex PDF document contains additional information.
We include more text here to simulate a more detailed and lengthy document.""",
    """Continuing on the third page, we see more detailed descriptions and structured text.
This helps us test the robustness of our PDF text extraction process.""",
    """Finally, this is the fourth page of the complex PDF document.
The test should handle all pages and extract text correctly.
Thank you for reading through this complex PDF."""
]

create_pdf("SimplePDF.pdf", simple_pdf_content)
create_pdf("MediumPDF.pdf", medium_pdf_content)
create_pdf("ComplexPDF.pdf", complex_pdf_content)
