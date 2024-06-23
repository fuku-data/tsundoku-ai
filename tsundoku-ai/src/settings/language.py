import streamlit as st
import settings.llm


def session_init_render() -> None:
    if "lg_radio_options" not in st.session_state:
        st.session_state.lg_radio_options = ['English', 'Japanese']
    if "lg_radio_index" not in st.session_state:
        st.session_state.lg_radio_index = 0
    if "lg_select_radio_button_result" not in st.session_state:
        st.session_state.lg_select_radio_button_result = ''
    if "lg_Settings" not in st.session_state:
        st.session_state.lg_Settings = 'Settings'
    if "lg_Language_Settings" not in st.session_state:
        st.session_state.lg_Language_Settings = 'Language Settings'
    if "lg_AI_Settings" not in st.session_state:
        st.session_state.lg_AI_Settings = 'AI Settings'
    if "lg_OpenAI_API_Key_Setting" not in st.session_state:
        st.session_state.lg_OpenAI_API_Key_Setting = 'OpenAI API Key Setting'
    if "lg_API_Key" not in st.session_state:
        st.session_state.lg_API_Key = 'API Key'
    if "lg_Set_API_key" not in st.session_state:
        st.session_state.lg_Set_API_key = 'Set API Key'
    if "lg_Clear_API_key" not in st.session_state:
        st.session_state.lg_Clear_API_key = 'Clear API Key'
    if "lg_Choose_Model" not in st.session_state:
        st.session_state.lg_Choose_Model = 'Choose Model'
    if "lg_Temperature" not in st.session_state:
        st.session_state.lg_Temperature = 'Temperature'
    if "lg_Processing" not in st.session_state:
        st.session_state.lg_Processing = 'Processing...'
    if "lg_Successful_Connection" not in st.session_state:
        st.session_state.lg_Successful_Connection = 'Successful Connection!'
    if "lg_The_API_key_you_typed_is_not_valid" not in st.session_state:
        st.session_state.lg_The_API_key_you_typed_is_not_valid = 'ERROR: The API key you typed is not valid'
    if "lg_AI_Assistant" not in st.session_state:
        st.session_state.lg_AI_Assistant = 'AI Assistant'
    if "lg_COVID19_Number_of_cases_by_country" not in st.session_state:
        st.session_state.lg_COVID19_Number_of_cases_by_country = 'COVID-19 Number of cases by country'
    if "lg_No_OpenAI_API_key_is_provided" not in st.session_state:
        st.session_state.lg_No_OpenAI_API_key_is_provided = 'No OpenAI API key is provided.'
    if "lg_Can_I_ask_a_question" not in st.session_state:
        st.session_state.lg_Can_I_ask_a_question = 'Can I ask a question?'
    if "lg_Send" not in st.session_state:
        st.session_state.lg_Send = 'Send'
    if "lg_Datasource" not in st.session_state:
        st.session_state.lg_Datasource = 'Datasource'


def session_re_render() -> None:
    if st.session_state.language == st.session_state.lg_radio_options[0]:
        st.session_state.lg_radio_options = ['English', 'Japanese']
        st.session_state.lg_radio_index = 0
        lg_transaction('English')
        settings.llm.session_re_render()

        st.session_state.lg_select_radio_button_result = 'select_English'

    elif st.session_state.language == st.session_state.lg_radio_options[1]:
        st.session_state.lg_radio_options = ['英語', '日本語']
        st.session_state.lg_radio_index = 1
        lg_transaction('Japanese')
        settings.llm.session_re_render()

        st.session_state.lg_select_radio_button_result = 'select_Japanese'


dict = {
    'lg_Settings': {
        'English': 'Settings',
        'Japanese': '設定'
    },
    'lg_Language_Settings': {
        'English': 'Language Settings',
        'Japanese': '言語設定'
    },
    'lg_Snowflake_Settings': {
        'English': 'Snowflake Settings',
        'Japanese': 'Snowflakeの設定'
    },
    'lg_AI_Settings': {
        'English': 'AI Settings',
        'Japanese': 'AIの設定'
    },
    'lg_OpenAI_API_Key_Setting': {
        'English': 'OpenAI API Key Setting',
        'Japanese': 'OpenAI APIキーの設定'
    },
    'lg_API_Key': {
        'English': 'API Key',
        'Japanese': 'APIキー'
    },
    'lg_Set_API_key': {
        'English': 'Set API Key',
        'Japanese': 'APIキーを設定'
    },
    'lg_Clear_API_key': {
        'English': 'Clear API Key',
        'Japanese': 'APIキーをクリア'
    },
    'lg_Choose_Model': {
        'English': 'Choose Model',
        'Japanese': 'モデルを選択'
    },
    'lg_Temperature': {
        'English': 'Temperature',
        'Japanese': 'Temperature'
    },
    'lg_Processing': {
        'English': 'Processing...',
        'Japanese': '処理中...'
    },
    'lg_Successful_Connection': {
        'English': 'Successful Connection!',
        'Japanese': '接続に成功しました！'
    },
    'lg_The_API_key_you_typed_is_not_valid': {
        'English': 'ERROR: The API key you typed is not valid',
        'Japanese': 'エラー: 入力されたAPIキーは有効ではありません。'
    },
    'lg_AI_Assistant': {
        'English': 'AI Assistant',
        'Japanese': 'AI アシスタント'
    },
    'lg_COVID19_Number_of_cases_by_country': {
        'English': 'COVID-19 Number of cases by country',
        'Japanese': 'COVID-19国別感染者数'
    },
    'lg_No_OpenAI_API_key_is_provided': {
        'English': 'No OpenAI API key is provided.',
        'Japanese': 'OpenAIのAPIキーが設定されていません。'
    },
    'lg_Can_I_ask_a_question': {
        'English': 'Can I ask a question?',
        'Japanese': 'ご質問はありませんか？'
    },
    'lg_Send': {
        'English': 'Send',
        'Japanese': '送信'
    },
    'lg_Datasource': {
        'English': 'Datasource',
        'Japanese': 'データソース'
    }
}


def lg_transaction(language: str) -> None:
    st.session_state.lg_Settings = dict['lg_Settings'][language]
    st.session_state.lg_Language_Settings = dict['lg_Language_Settings'][language]
    st.session_state.lg_Snowflake_Settings = dict['lg_Snowflake_Settings'][language]
    st.session_state.lg_AI_Settings = dict['lg_AI_Settings'][language]
    st.session_state.lg_OpenAI_API_Key_Setting = dict['lg_OpenAI_API_Key_Setting'][language]
    st.session_state.lg_API_Key = dict['lg_API_Key'][language]
    st.session_state.lg_Set_API_key = dict['lg_Set_API_key'][language]
    st.session_state.lg_Clear_API_key = dict['lg_Clear_API_key'][language]
    st.session_state.lg_Choose_Model = dict['lg_Choose_Model'][language]
    st.session_state.lg_Temperature = dict['lg_Temperature'][language]
    st.session_state.lg_Processing = dict['lg_Processing'][language]
    st.session_state.lg_Successful_Connection = dict['lg_Successful_Connection'][language]
    st.session_state.lg_The_API_key_you_typed_is_not_valid = dict['lg_The_API_key_you_typed_is_not_valid'][language]
    st.session_state.lg_AI_Assistant = dict['lg_AI_Assistant'][language]
    st.session_state.lg_COVID19_Number_of_cases_by_country = dict['lg_COVID19_Number_of_cases_by_country'][language]
    st.session_state.lg_No_OpenAI_API_key_is_provided = dict['lg_No_OpenAI_API_key_is_provided'][language]
    st.session_state.lg_Can_I_ask_a_question = dict['lg_Can_I_ask_a_question'][language]
    st.session_state.lg_Send = dict['lg_Send'][language]
    st.session_state.lg_Datasource = dict['lg_Datasource'][language]