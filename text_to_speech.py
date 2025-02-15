import requests

def text_to_speech(text, api_key):
    url = "https://api.sarvam.ai/text-to-speech"
    headers = {
        "api-key": api_key,
        "Content-Type": "application/json"
    }
    data = {
        "text": text
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        audio_content = response.content
        with open("output_audio.mp3", "wb") as audio_file:
            audio_file.write(audio_content)
        print("Audio content written to output_audio.mp3")
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    sarvam_api_key = "270d52d7-1f85-4cd3-8cf7-a7beac13882a"
    sample_text = "Hello, this is a test of the Sarvam text-to-speech API."
    text_to_speech(sample_text, sarvam_api_key)
