from openai_service import openai_chat_completion
import streamlit as st

hide_streamlit_style = """
<style>
    header {visibility: hidden;}
    footer {visibility: hidden;}
</style>
"""


def main():
    st.set_page_config(
        page_title="openai DEMO"
    )

    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.header("openai DEMO")

    system_prompt = st.text_area("system_prompt", value='I want to you to act as a mediator for our quiz game, so you need to provided 10 random general-knowledge question based on the subject we select', height=225)
    user_prompt = st.text_area("user_prompt", value='Geography', height=225)

    translate_button = st.button("Generate")

    if translate_button:
        with st.spinner("Generating..."):
            response = openai_chat_completion(system_prompt, user_prompt)
            st.write(response)


if __name__ == "__main__":
    main()
