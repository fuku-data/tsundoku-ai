import settings.language
import settings.llm

import openai
import streamlit as st


def main():
    settings.language.session_init_render()
    settings.llm.session_init_render()
    llm_assistant_ui()
    model_name, temperature = select_model()
    init_messages()
    converse_with_ai(model_name, temperature)


def llm_assistant_ui():
    st.set_page_config(
        page_title='FUKU DATA CATALOG',
        page_icon='📘',
        layout='wide',
        initial_sidebar_state='expanded'
    )
    st.header('📘 FUKU DATA CATALOG')
    st.header(f'🤖 {st.session_state.lg_AI_Assistant}')
    with st.empty():
        if not st.session_state.llm_connection_flag:
            st.warning(
                f"""
                ##### **🔔 {st.session_state.lg_No_OpenAI_API_key_is_provided}**
                """
            )


def select_model():
    model = st.sidebar.radio(f'{st.session_state.lg_Choose_Model} :', ["GPT-3.5 Turbo", "GPT-4"])
    if model == "GPT-3.5 Turbo":
        model_name = "gpt-3.5-turbo"
    else:
        model_name = "gpt-4"

    temperature = st.sidebar.slider(f'{st.session_state.lg_Temperature} :',
                                    min_value=0.0,
                                    max_value=2.0,
                                    value=0.0,
                                    step=0.1
                                    )

    return model_name, temperature


def init_messages():
    clear_button = st.sidebar.button("Clear Chats", key="clear")
    if clear_button or "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]
        st.session_state.costs = []


def converse_with_ai(model_name, temperature):
    container = st.container()
    with container:
        with st.form(key='your_form', clear_on_submit=True):
            user_input = st.text_area(
                label=st.session_state.lg_Can_I_ask_a_question,
                key='input',
                height=100,
                disabled=not st.session_state.llm_connection_flag
            )

            # leave nothing against line breaks
            content = user_input.replace('\n', '')
            submit_button = st.form_submit_button(
                label=st.session_state.lg_Send,
                type='primary',
                disabled=not st.session_state.llm_connection_flag
            )

    if submit_button and user_input:
        # try:
        #     st.session_state.messages.append({'role': 'user', 'content': content})
        #     with st.spinner(f'{st.session_state.lg_Processing}'):
        #         messages = st.session_state.messages
        #         response = openai.ChatCompletion.create(
        #             model=model_name,
        #             messages=messages,  # 文字列に変換したmessagesを渡す
        #             temperature=temperature
        #         )
        #     st.session_state.messages.append({'role': 'assistant', 'content': response.choices[0]['message']['content']})
        # except AuthenticationError:
        #     st.error(
        #         f"""
        #         #### **🚨 {st.session_state.lg_The_API_key_you_typed_is_not_valid}**
        #         """
        #     )
        st.session_state.messages.append({'role': 'user', 'content': content})
        with st.spinner(f'{st.session_state.lg_Processing}'):
            messages = st.session_state.messages
            response = openai.ChatCompletion.create(
                model=model_name,
                messages=messages,  # 文字列に変換したmessagesを渡す
                temperature=temperature
            )
        st.session_state.messages.append({'role': 'assistant', 'content': response.choices[0]['message']['content']})

    # present chat history
    messages = st.session_state.messages
    for message in messages:
        if message['role'] == "assistant":
            # NOTE:Streamlit 1_22_0では、st.chat_messageは使えない
            with st.chat_message('assistant'):
                st.markdown(message['content'])
            # st.info(f"""🤖 Assistant: {message['content']}""")
        elif message['role'] == "user":
            with st.chat_message('user'):
                st.markdown(message['content'])
            # st.success(f"""😀 You: {message['content']}""")
        else:
            st.markdown(f"""System message: {message['content']}""")


if __name__ == '__main__':
    main()