from googletrans import Translator
from gtts import gTTS
import os

# Solicita la frase y el idioma de destino
frase = input("Ingresa la frase que quieres traducir: ")
idioma_destino = input("Ingresa el idioma de destino (por ejemplo, 'es' para español): ")

# Crea una instancia del traductor y traduce la frase al idioma de destino
traductor = Translator()
traduccion = traductor.translate(frase, dest=idioma_destino)
frase_traducida = traduccion.text

# Crea una instancia de gTTS para generar el audio
def text_to_speech(text, tld):

    tts = gTTS(text, lang=tld, slow=False)

    try:

        my_file_name = text[0:20]

    except:

        my_file_name = "audio"

    tts.save(f"temp/{my_file_name}.mp3")

    return my_file_name, textt


# Reproduce el archivo de audio usando playsound
#result, output_text = text_to_speech(translated_text, target_lang_code)


 
    #audio_file = open(f"temp/{result}.mp3", "rb")

    #audio_bytes = audio_file.read()
