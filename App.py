import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 Language Translation Tool")
st.write("Translate text between multiple languages")

languages = {
    "Auto Detect": "auto",
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Tamil": "ta",
    "Japanese": "ja"
}

text = st.text_area(
    "Enter Text",
    height=150,
    placeholder="Type text here..."
)

col1, col2 = st.columns(2)

with col1:
    source = st.selectbox(
        "Source Language",
        list(languages.keys())
    )

with col2:
    target = st.selectbox(
        "Target Language",
        list(languages.keys())[1:]
    )

if st.button("Translate"):

    if text.strip() == "":
        st.warning("Please enter some text")
    else:
        try:
            translated = GoogleTranslator(
                source=languages[source],
                target=languages[target]
            ).translate(text)

            st.success("Translation Successful")

            st.text_area(
                "Translated Text",
                translated,
                height=150
            )

            st.code(translated)

        except Exception:
            st.error("Translation failed. Check internet connection.")