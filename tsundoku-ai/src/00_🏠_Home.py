import ast
import os

import openai
import settings.language
import settings.llm
import streamlit as st
from scripts.search_index import search_index


def main():
    settings.language.session_init_render()
    settings.llm.session_init_render()
    # NOTE: 開発しやすいようにAPIキーをGUIから設定する手間を省く
    key: str = os.getenv("OPENAI_API_KEY")
    if len(key) > 0:
        st.session_state.llm_openai_api_key = key
        st.session_state.llm_connection_flag = True
        st.session_state.llm_click_set_or_clear_button_result = "success"
        # st.session_state.llm_set_or_clear_button_disabled = not st.session_state.llm_set_or_clear_button_disabled
    llm_assistant_ui()
    model_name, temperature = select_model()
    init_messages()
    converse_with_ai(model_name, temperature)


def llm_assistant_ui():
    st.set_page_config(
        page_title="積読PDF救済アプリ",
        page_icon="📘",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.header("📘 積読PDF救済アプリ")
    st.header(f"🤖 {st.session_state.lg_AI_Assistant}")
    with st.empty():
        if not st.session_state.llm_connection_flag:
            st.warning(
                f"""
                ##### **🔔 {st.session_state.lg_No_OpenAI_API_key_is_provided}**
                """
            )


def select_model():
    model = st.sidebar.radio(
        f"{st.session_state.lg_Choose_Model} :", ["GPT-3.5 Turbo", "GPT-4"]
    )
    if model == "GPT-3.5 Turbo":
        model_name = "gpt-3.5-turbo"
    else:
        model_name = "gpt-4"

    temperature = st.sidebar.slider(
        f"{st.session_state.lg_Temperature} :",
        min_value=0.0,
        max_value=2.0,
        value=0.0,
        step=0.1,
    )

    return model_name, temperature


def init_messages():
    clear_button = st.sidebar.button("Clear Chats", key="clear")
    if clear_button or "messages" not in st.session_state:
        system_prompt = """
            ## 回答ルール
            - ユーザーの質問文のキーワードを分析し、list型で返却してください。
            - キーワードが単一の場合は、1要素のlist、複数の場合はその個数分の要素を持ったlistで返却してください。

            ## 質問文とそれに対する返却値の例
            ###例1
            - 質問：`データガバナンスについて教えて下さい。`
            - 返却値：`['データガバナンス']`
            ###例2
            - 質問：`SnowflakeとRedshiftのメリットを教えて下さい。`
            - 返却値：`['Snowflake', 'Redshift']`
            ###例3
            - 質問：`Reactのstateとrefの違いを教えてください`
            - 返却値：`['React','state','ref']`
            ###例4
            - 質問：`Pythonのバージョン管理でおすすめなものは？`
            - 返却値：`['Python','バージョン管理']`
            ###例5
            - 質問：`キットカットとガリガリ君だったらどっちを買うのがいいですか？`
            - 返却値：`['キットカット','ガリガリ君']`
        """
        st.session_state.messages = [
            # {"role": "system", "content": "You are a helpful assistant."}
            {"role": "system", "content": system_prompt}
        ]
        # st.session_state.messages = []
        st.session_state.costs = []


def converse_with_ai(model_name, temperature):
    container = st.container()
    with container:
        with st.form(key="your_form", clear_on_submit=True):
            user_input = st.text_area(
                label=st.session_state.lg_Can_I_ask_a_question,
                key="input",
                height=100,
                disabled=not st.session_state.llm_connection_flag,
            )

            # leave nothing against line breaks
            content = user_input.replace("\n", "")
            submit_button = st.form_submit_button(
                label=st.session_state.lg_Send,
                type="primary",
                disabled=not st.session_state.llm_connection_flag,
            )

    if submit_button and user_input:
        st.session_state.messages.append({"role": "user", "content": content})
        with st.spinner(f"{st.session_state.lg_Processing}"):
            messages = st.session_state.messages
            response = openai.chat.completions.create(
                model=model_name,
                messages=messages,  # 文字列に変換したmessagesを渡す
                temperature=temperature,
            )

        keyword_list = ast.literal_eval(response.choices[0].message.content)
        results = search_index(keyword_list)
        reference_list = []
        for result in results:
            name_and_page_list = [result["book_name"], f"{result['page_number']}ページ"]
            reference_list.append(name_and_page_list)
        reference_contents = "以下の書籍のページが参考になります\n\n"
        for reference in reference_list:
            reference_contents += f"- 書籍名：{reference[0]}\n- ページ：{reference[1]}\n---\n"
        st.session_state.messages.append(
            {"role": "assistant", "content": reference_contents}
        )

    # present chat history
    messages = st.session_state.messages
    for message in messages:
        if message["role"] == "assistant":
            # NOTE:Streamlit 1_22_0では、st.chat_messageは使えない
            with st.chat_message("assistant"):
                st.markdown(message["content"])
            # st.info(f"""🤖 Assistant: {message['content']}""")
        elif message["role"] == "user":
            with st.chat_message("user"):
                st.markdown(message["content"])
            # st.success(f"""😀 You: {message['content']}""")


if __name__ == "__main__":
    main()
