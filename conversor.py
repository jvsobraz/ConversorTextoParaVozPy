from gtts import gTTS
import os

texto = "Olá, mundo! Este é um exemplo de conversão de texto para voz usando Python."

tts = gTTS(text=texto, lang='pt')

tts.save("exemplo.mp3")

os.system("mpg321 exemplo.mp3")  # Substitua "mpg321" pelo player de áudio correto para o seu sistema operacional

