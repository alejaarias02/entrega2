import streamlit as st
from googletrans import Translator
from gtts import gTTS
import tempfile
import os

st.title("Aplicativo AMA")
# Resto del código...

# Dentro de la condición donde traduces el texto y creas el audio
if text and target_lang:
    # Resto del código...
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio_file:
        tts.save(temp_audio_file.name)
        audio_bytes = open(temp_audio_file.name, "rb").read()
    
    st.markdown("## Tu audio:")
    st.audio(audio_bytes, format="audio/mp3", start_time=0)

    st.markdown("## Texto en audio:")
    st.write(translated_text)

