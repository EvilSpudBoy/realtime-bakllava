#import os
# Change path to ffmpeg if needed
# os.environ["IMAGEIO_FFMPEG_EXE"] = "/path_to/ffmpeg"


import requests
import base64
import imageio
import json
import subprocess

url = "http://localhost:8080/completion"
headers = {"Content-Type": "application/json"}

print("Starting video stream with TTS on macOS... Wait for a few seconds for the stream to the output to start "
      "generating.")
cap = imageio.get_reader('<video0>')

while True:
    # Capture frame-by-frame
    frame = cap.get_next_data()
    # Save the image to a file
    imageio.imsave('temp.png', frame)
    # Open the file in binary mode and convert to base64
    with open('temp.png', 'rb') as file:
        encoded_string = base64.b64encode(file.read()).decode('utf-8')

    image_data = [{"data": encoded_string, "id": 12}]

    data = {"prompt": "USER:[img-12]Describe the image.\nASSISTANT:", "n_predict": 128, "image_data": image_data, "stream": True}

    response = requests.post(url, headers=headers, json=data, stream=True)

    with open("output.txt", "a") as write_file:
        full_content = ""
        write_file.write("---"*10 + "\n\n")

    for chunk in response.iter_content(chunk_size=128):
        with open("output.txt", "a") as write_file:
            content = chunk.decode().strip().split('\n\n')[0]
            try:
                content_split = content.split('data: ')
                if len(content_split) > 1:
                    content_json = json.loads(content_split[1])
                    full_content += content_json["content"]
                    print(content_json["content"], end='', flush=True)
                write_file.flush()
            except json.JSONDecodeError:
                print("JSONDecodeError: Expecting property name enclosed in double quotes")

    if full_content:
        subprocess.run(['say', full_content])

cap.close()