# Conversor de Texto para Voz em Python

Você pode usar a biblioteca "gTTS" (Google Text-to-Speech) para converter texto em fala usando Python. A gTTS é uma biblioteca que permite que você acesse a API de Text-to-Speech do Google e obtenha arquivos de áudio em formato MP3 a partir do texto fornecido. Aqui está um exemplo simples de como você pode usar a gTTS em Python:

1. Instalar a biblioteca gTTS usando pip:

pip install gTTS

2. Importar a biblioteca gTTS e o módulo "os" para manipulação de arquivos:

from gtts import gTTS
import os

3. Definir o texto que você deseja converter em fala:

texto = "Olá, mundo! Este é um exemplo de conversão de texto para voz usando Python."

4. Criar um objeto gTTS com o texto e definir o idioma da fala:

tts = gTTS(text=texto, lang='pt')

5. Salvar o arquivo de áudio em formato MP3:

tts.save("exemplo.mp3")

6. Reproduzir o arquivo de áudio usando o player de áudio padrão do sistema operacional:

os.system("mpg321 exemplo.mp3")  # Substitua "mpg321" pelo player de áudio correto para o seu sistema operacional

---------------------------------------------
Isso é um exemplo simples de como usar a biblioteca gTTS em Python para converter texto em fala. Você pode personalizar a linguagem, a velocidade da fala e outras configurações conforme necessário. Consulte a documentação oficial da biblioteca gTTS para obter mais informações sobre suas funcionalidades e opções de configuração.
