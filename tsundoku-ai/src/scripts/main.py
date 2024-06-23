from pathlib import Path

from parse_pdf import extract_text_from_pdf
from search_index import create_search_index, search_index

root_dir = Path(__file__).resolve().parents[3]

pdf_text = extract_text_from_pdf(root_dir / "book" / "oreilly-978-4-8144-0034-8e.pdf")
create_search_index(pdf_text)
search_index("エラーバジェット")
