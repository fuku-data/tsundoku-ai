from pathlib import Path

from whoosh.fields import ID, NUMERIC, TEXT, Schema
from whoosh.index import create_in, open_dir
from whoosh.qparser import MultifieldParser
from whoosh.query import And

root_dir = Path(__file__).resolve().parents[1]
index_dir = root_dir.joinpath("index")


def create_search_index():
    schema = Schema(
        book_name=ID(stored=True),
        page_number=NUMERIC(stored=True),
        content=TEXT(stored=True),
    )
    if index_dir.exists():
        ix = open_dir(str(index_dir))
        return ix
    index_dir.mkdir(exist_ok=True)
    ix = create_in(str(index_dir), schema)
    return ix


def add_documents_to_index(ix, title, text):
    writer = ix.writer()
    for page, section in enumerate(text.split("\n\n")):
        writer.add_document(book_name=title, page_number=page + 1, content=section)
    writer.commit()


def search_index(keywords):
    ix = open_dir(str(index_dir))
    with ix.searcher() as searcher:
        parser = MultifieldParser(["content"], schema=ix.schema)
        query = And([parser.parse(keyword) for keyword in keywords])
        results = searcher.search(query)
        for result in results:
            print(result["book_name"])
            print(result["page_number"])
            print(result["content"])