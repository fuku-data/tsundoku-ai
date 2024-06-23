from os.path import splitext

import fitz


def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    title = splitext(pdf_file.name)[0]
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        page_text = page.get_text()
        text += page_text.replace("\n", "")
        text += "\n\n"
    return title, text
