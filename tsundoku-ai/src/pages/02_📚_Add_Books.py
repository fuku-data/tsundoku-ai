import streamlit as st
from scripts.parse_pdf import extract_text_from_pdf
from scripts.search_index import add_documents_to_index, create_search_index

st.title("書籍 PDF アップロード")

uploaded_files = st.file_uploader(
    "追加したい書籍の PDF を選択してください", type="pdf", accept_multiple_files=True
)

if uploaded_files:
    create_search_index()
    for uploaded_file in uploaded_files:
        pdf_title, pdf_text = extract_text_from_pdf(uploaded_file)
        add_documents_to_index(pdf_title, pdf_text)
    st.write("書籍の PDF のアップロードが完了しました")