import settings.language
import settings.llm

import streamlit as st
import time


def main():
    settings.language.session_init_render()
    settings.llm.session_init_render()
    setting_ui()


def setting_ui():
    st.set_page_config(
        page_title='FUKU DATA CATALOG',
        page_icon='📘',
        layout='wide',
        initial_sidebar_state='expanded'
    )
    st.header('📘 FUKU DATA CATALOG')
    st.header(f'🔧 {st.session_state.lg_Settings}')

    language_tab, llm_tab = st.tabs(
        [f'🌏 {st.session_state.lg_Language_Settings}', f'🤖 {st.session_state.lg_AI_Settings}']
    )

    with language_tab:
        st.markdown(f"""### 🌏 {st.session_state.lg_Language_Settings}""")
        st.radio(
            label='',
            options=st.session_state.lg_radio_options,
            index=st.session_state.lg_radio_index,
            key="language",
            on_change=settings.language.session_re_render,
            horizontal=False
        )
        with st.empty():
            if st.session_state.lg_select_radio_button_result == 'select_English':
                st.success(
                    """
                    #### **✅ Language set to English!**
                    """
                )
                time.sleep(1)
                st.write("")
                st.session_state.lg_select_radio_button_result = ''
            elif st.session_state.lg_select_radio_button_result == 'select_Japanese':
                st.success(
                    """
                    #### **✅ 言語を日本語に設定しました！**
                    """
                )
                time.sleep(1)
                st.write("")
                st.session_state.lg_select_radio_button_result = ''

    with llm_tab:
        st.markdown(f"""### 🤗 {st.session_state.lg_OpenAI_API_Key_Setting}""")

        # CHECK:再レンダリングポイント
        if st.session_state.llm_set_or_clear_button:
            settings.llm.set_or_clear_openai_api_key_button_event()
            settings.llm.click_set_or_clear_button()

        # TODO:以下、`st.session_state.llm_openai_api_key`の位置が気持ち悪い。keyパラメータを活用するには2つのst.session_stateのパラメータが必要と考えるが冗長的。
        st.session_state.llm_openai_api_key = st.text_input(
            label=f'🟡 {st.session_state.lg_API_Key} :',
            value=st.session_state.llm_openai_api_key,
            placeholder='sk-ABCDEFG...',
            type='password',
            on_change=settings.llm.session_re_render,
            disabled=st.session_state.llm_set_or_clear_button_disabled
        )

        with st.empty():
            if st.session_state.llm_click_set_or_clear_button_result == 'success':
                st.success(
                    f"""
                    #### **✅ {st.session_state.lg_Successful_Connection}**
                    """
                )
                time.sleep(1)
                st.write("")
                st.session_state.llm_click_set_or_clear_button_result = ''
            elif st.session_state.llm_click_set_or_clear_button_result == 'authentication_error':
                st.error(
                    f"""
                    #### **🚨 {st.session_state.lg_The_API_key_you_typed_is_not_valid}**
                    """
                )
                st.session_state.llm_click_set_or_clear_button_result = ''

        st.button(
            label=st.session_state.llm_set_or_clear_button_label,
            type=st.session_state.llm_set_or_clear_button_type,
            on_click=settings.llm.click_set_or_clear_button,
            use_container_width=True,
            disabled=False
        )


if __name__ == '__main__':
    main()

# if init_snowflake_setup:
    #     # TODO:SYSTEMADMINを持っている人しかできないようにする
    #     # FIXME:aaaどのロールで、どのようなオブジェクトを作成、編集するか説明文を書く
    #     # NOTE:MySQLやポスグレ上に置けるようにする。ホスト名、ユーザー名、パスワード
    #     init_agreement = st.checkbox('I agree!')
    #     set_sf_obj_button = st.button(
    #         'Create Objects',
    #         type='primary',
    #         key='set_sf_obj',
    #         disabled=False
    #     )
    #     st.warning(""" # ポスグレ、MySQLも選ばせる""")