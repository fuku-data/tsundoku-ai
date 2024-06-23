from pathlib import Path

from whoosh.fields import TEXT, Schema
from whoosh.index import create_in, open_dir
from whoosh.qparser import QueryParser

root_dir = Path(__file__).resolve().parents[1]
index_dir = root_dir.joinpath("index")


def create_search_index(text):
    schema = Schema(content=TEXT(stored=True))
    index_dir.mkdir(exist_ok=True)
    ix = create_in(str(index_dir), schema)
    writer = ix.writer()
    for section in text.split("\n\n"):
        writer.add_document(content=section)
    writer.commit()


def search_index(query_str):
    ix = open_dir(str(index_dir))
    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema).parse(query_str)
        results = searcher.search(query)
        for result in results:
            print(result["content"])
