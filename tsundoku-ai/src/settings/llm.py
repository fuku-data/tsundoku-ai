import openai
import streamlit as st


def session_init_render() -> None:
    if "llm_set_or_clear_button_disabled" not in st.session_state:
        st.session_state.llm_set_or_clear_button_disabled = False
    if "llm_openai_api_key" not in st.session_state:
        st.session_state.llm_openai_api_key = ''
    if "llm_set_or_clear_button_label" not in st.session_state:
        st.session_state.llm_set_or_clear_button_label = st.session_state.lg_Set_API_key
    if "llm_set_or_clear_button_type" not in st.session_state:
        st.session_state.llm_set_or_clear_button_type = 'primary'
    if "llm_connection_flag" not in st.session_state:
        st.session_state.llm_connection_flag = False
    if "llm_set_or_clear_button" not in st.session_state:
        st.session_state.llm_set_or_clear_button = False
    if "llm_click_set_or_clear_button_result" not in st.session_state:
        st.session_state.llm_click_set_or_clear_button_result = ''


def session_re_render() -> None:
    if st.session_state.llm_connection_flag:
        st.session_state.llm_set_or_clear_button_label = st.session_state.lg_Clear_API_key
        st.session_state.llm_set_or_clear_button_type = 'secondary'
        st.session_state.llm_set_or_clear_button_disabled = True
    else:
        st.session_state.llm_set_or_clear_button_label = st.session_state.lg_Set_API_key
        st.session_state.llm_set_or_clear_button_type = 'primary'
        st.session_state.llm_set_or_clear_button_disabled = False


def click_set_or_clear_button() -> None:
    st.session_state.llm_set_or_clear_button = not st.session_state.llm_set_or_clear_button


def set_or_clear_openai_api_key_button_event() -> None:
    set_or_clear_openai_api_key()
    session_re_render()


def set_or_clear_openai_api_key() -> None:
    if st.session_state.llm_connection_flag:
        openai.api_key = None
        st.session_state.llm_openai_api_key = ''
        st.session_state.llm_connection_flag = False
    else:
        with st.spinner(f'{st.session_state.lg_Processing}'):
            # NOTE:langchainモジュールを使うには`os.environ['OPENAI_API_KEY']`を設定する必要があり、Streamlit in Snowflake上で使うには危険。
            openai.api_key = st.session_state.llm_openai_api_key
            # try:
            #     # NOTE:openai.api_keyとして有効かどうかを確認👇。enginとpromptは任意で良い。
            #     # NOTE:確認用エンジンは安価の`babbage`を使う。
            #     test_response = openai.Completion.create(
            #         engine='babbage',
            #         prompt='This is a test request to check API key validity.',
            #         max_tokens=5
            #     )
            #     test_response.choices[0].text

            #     st.session_state.llm_connection_flag = True
            #     st.session_state.llm_click_set_or_clear_button_result = 'success'
            # except AuthenticationError:
            #     st.session_state.llm_click_set_or_clear_button_result = 'authentication_error'

            # FUTURE FIXME: 入力されたAPIが間違っているかどうかテストする
            # test_response = openai.chat.completions.create(
            #     engine='babbage',
            #     prompt='This is a test request to check API key validity.',
            #     max_tokens=5
            # )
            # test_response.choices[0].text

            st.session_state.llm_connection_flag = True
            st.session_state.llm_click_set_or_clear_button_result = 'success'
