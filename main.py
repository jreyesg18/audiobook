import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import os
import PyPDF2


def translate_text(text, dest_lang='es'):
    try:
        translator = GoogleTranslator(target=dest_lang)
        translation = translator.translate(text)
        return translation
    except Exception as e:
        return f"Error en la traducción: {e}"


def speak_text(text, lang='es'):
    try:
        tts = gTTS(text, lang=lang)
        audio_file = "translated.mp3"
        tts.save(audio_file)
        os.system(f"afplay {audio_file}")  # Usa afplay en lugar de mpg321
    except Exception as e:
        print(f"Error al reproducir el texto: {e}")


def read_pdf(file):
    texts = []
    try:
        reader = PyPDF2.PdfReader(file)
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                texts.append(f"Página {i + 1}:\n{text}")
            else:
                texts.append(f"Página {i + 1}: (No se pudo extraer texto)")
    except Exception as e:
        print(f"Error al leer el PDF: {e}")
    return texts


def main():
    st.title("Traductor de PDF y Conversor de Voz")

    pdf_file = st.file_uploader("Sube el archivo PDF que deseas traducir", type="pdf")

    if pdf_file is not None:
        pages_text = read_pdf(pdf_file)

        if not pages_text:
            st.error("No se pudo extraer texto del PDF.")
            return

        st.write(f"El PDF tiene {len(pages_text)} páginas.")
        start_page = st.number_input(
            f"Introduce el número de la página desde la cual deseas empezar a traducir (1 a {len(pages_text)})",
            min_value=1, max_value=len(pages_text), value=1)
        dest_lang = st.selectbox("Selecciona el idioma al que deseas traducir", ['es', 'en', 'fr', 'de', 'it'])

        if st.button("Traducir y Reproducir"):
            for page_number, text in enumerate(pages_text[start_page - 1:], start=start_page):
                st.write(f"Traduciendo página {page_number}...")
                translated_text = translate_text(text, dest_lang)
                st.text_area(f"Texto traducido de la página {page_number}", translated_text, height=200)

                # Reproducción de la traducción en voz
                speak_text(translated_text, lang=dest_lang)
                st.audio("translated.mp3", format="audio/mp3")


if __name__ == "__main__":
    main()