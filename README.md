# 🍰 Bakllava Llama C++ Tutorial 🦙

Welcome to the delicious world of Bakllava Llama with C++! Follow these steps to get your code running and indulge in AI sweetness! 😋

🚨 Properly tested only with Apple silicon chip

[youtube installation guide](https://youtu.be/UyRFbGK9QmI)

similar relevant project: [Be My Eyes" web app](https://github.com/lxe/llavavision#getting-started)

<a href="https://twitter.com/Karmedge" target="_blank"><img src="https://img.shields.io/badge/Twitter-%40karmedge-00000"></a>

<a href="https://www.linkedin.com/in/karmedge" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-karmedge-informational"></a>

## 🚀 Step 1: Install Llama C++

First things first, let's get the Llama C++ installed.

🔗 Clone the repository from GitHub:
```jsx
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
```
### On Linux & macOS:
🛠 Build with make:
```
make
```
🏗 Or, if you prefer cmake:
```
cmake --build . --config Release
```

## 📦 Step 2: Download the Model!
### To use llava
1. 📥 Download from Hugging Face - [mys/ggml_bakllava-1](https://huggingface.co/mys/ggml_bakllava-1/tree/main) this 2 files:
* 🌟 ggml-model-q4_k.gguf (or any other quantized model) - only one is required!
* 🧊 mmproj-model-f16.gguf
---
### To use ShareGPT4V-7B
1. 📥 Download from Hugging Face - [nakodanei/ShareGPT4V-7B_GGUF](https://huggingface.co/nakodanei/ShareGPT4V-7B_GGUF/tree/main) this 2 files:
* 🌟 ShareGPT4V-7B_Q5_K_M.gguf
* 🧊 mmproj-model-f16.gguf
---

2. ✂️ Copy the paths of those 2 files.
3. 🏃‍♂️ Run this in the llama.cpp repository (replace YOUR_PATH with the paths to the files you downloaded):

    #### macOS
    *llava*
    ```
    ./server -m YOUR_PATH/ggml-model-q4_k.gguf --mmproj YOUR_PATH/mmproj-model-f16.gguf -ngl 1
    ```
    *ShareGPT4V*
    ```
    ./server -m YOUR_PATH/ShareGPT4V-7B_Q5_K_M.gguf --mmproj YOUR_PATH/mmproj-model-f16.gguf -ngl 1
    ```
    #### Windows
    *llava*
   ```
    server.exe -m REPLACE_WITH_YOUR_PATH\ggml-model-q4_k.gguf --mmproj REPLACE_WITH_YOUR_PATH\mmproj-model-f16.gguf -ngl 1

    ```
    *ShareGPT4V*
    ```
    server.exe -m REPLACE_WITH_YOUR_PATH\ShareGPT4V-7B_Q5_K_M.gguf --mmproj REPLACE_WITH_YOUR_PATH\mmproj-model-f16.gguf -ngl 1

    ```
4. 🎉 The llama server is now up and running!
    
    ⚠️ NOTE: Keep the server running in the background.
5. 📹 Let's run the script to use the webcam or send it a single picture!

## 🏃‍♀️ Step 3: Running the Demo
Open a new terminal window and clone the demo app:
```
git clone https://github.com/Fuzzy-Search/realtime-bakllava.git
cd realtime-bakllava
```
### 🛠 (Optional) Create a new Python virtual environment and activate it
```
python3 -m venv bakllava-venv
source bakllava-venv/bin/activate
pip3 install -r requirements.txt
```
### 🎥 Webcam Script
To start streaming from your webcam:

! if you have problem with FFMPEG lib, download the source code and in file src/video_stream.py modify second line of code

```
python3 src/video_stream.py
```

### 🖼 Simple Picture Drop
![Export-1699182386675](https://github.com/Fuzzy-Search/realtime-bakllava/assets/40468118/cc2384d9-1e16-4e94-a02c-47bd703d8ed7)

```
pip install -r picture_requirements.txt
python src/picture_drop.py --path src/sample_pic.png
```


## 📝 Enjoy your adventure with Llama C++! 🚀🦙

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Fuzzy-Search/realtime-bakllava&type=Date)](https://star-history.com/#Fuzzy-Search/realtime-bakllava&Date)
