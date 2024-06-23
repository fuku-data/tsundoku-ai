from pathlib import Path

from extract_question_keywords import classify_question_and_extract_keywords
from parse_pdf import extract_text_from_pdf
from search_index import (add_documents_to_index, create_search_index,
                          search_index)

root_dir = Path(__file__).resolve().parents[3]

ix = create_search_index()
for path in root_dir.joinpath("book").glob("*.pdf"):
    pdf_title, pdf_text = extract_text_from_pdf(path)
    add_documents_to_index(ix, pdf_title, pdf_text)
search_index(["分割代入"])

# question = "エラーバジェットの運用について知りたい"
# classification = classify_question_and_extract_keywords(question)
# print(classification)
