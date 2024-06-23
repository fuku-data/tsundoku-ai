from pathlib import Path

import fitz


def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    title = pdf_path.stem
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        page_text = page.get_text()
        text += page_text.replace("\n", "")
        text += "\n\n"
    return title, text
