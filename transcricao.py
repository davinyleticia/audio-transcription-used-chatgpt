
import openai
import json
import os

path = './dir_mp3'
for filename in os.listdir(path):
    print(filename)
    if (filename.endswith(".mp3")):
        get_text = []
        openai.api_key = '<coloca aqui a chave da api do chatgpt>'
        audio_file = open(f"./dir_mp3/{filename}", "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        with open(f"dir_json/{filename.replace('.mp3','')}.json", "w", ) as out_file:
            json.dump(transcript, out_file, indent=6)
        out_file.close()
    else:
        continue
