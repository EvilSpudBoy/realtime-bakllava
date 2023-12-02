import os
import requests
import time
from PIL import Image
import base64
import io
import imageio
import json
from gtts import gTTS
from playsound import playsound

url = "http://localhost:8080/completion"
headers = {"Content-Type": "application/json"}

print("Starting video stream with TTS... Wait for a few seconds for the stream to the output to start generating.")
cap = imageio.get_reader('<video0>')

while True:
    frame = cap.get_next_data()
    imageio.imsave('temp.png', frame)
    with open('temp.png', 'rb') as file:
        encoded_string = base64.b64encode(file.read()).decode('utf-8')

    image_data = [{"data": encoded_string, "id": 12}]

    data = {"prompt": "USER:[img-12]Describe the image.\nASSISTANT:", "n_predict": 128, "image_data": image_data, "stream": True}

    response = requests.post(url, headers=headers, json=data, stream=True)

    with open("output.txt", "a") as write_file:
        write_file.write("---"*10 + "\n\n")

    for chunk in response.iter_content(chunk_size=128):
        with open("output.txt", "a") as write_file:
            content = chunk.decode().strip().split('\n\n')[0]
            try:
                content_split = content.split('data: ')
                if len(content_split) > 1:
                    content_json = json.loads(content_split[1])
                    write_file.write(content_json["content"])
                    print(content_json["content"], end='', flush=True)
                    tts = gTTS(content_json["content"], lang='en')
                    tts.save("output.mp3")
                    playsound("output.mp3")
                write_file.flush()
            except json.JSONDecodeError:
                print("JSONDecodeError: Expecting property name enclosed in double quotes")

cap.close()