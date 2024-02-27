import string

import pdfplumber

pdf_path = "data/sample.pdf"


def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text(layout=False)
            page_text = "".join(filter(lambda x: x in string.printable, page_text))
            if page_text:
                yield page_text


text = extract_text_from_pdf(pdf_path)
