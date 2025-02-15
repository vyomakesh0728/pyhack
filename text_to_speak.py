import requests

def text_to_speech(text, api_key):
    url = "https://api.elevenlabs.io/v1/text-to-speech/JBFqnCBsd6RMkjVDRZzb?output_format=mp3_44100_128"
    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2"
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
    eleven_labs_api_key = "sk_e82df97a20042d63e0c246687accdd22ae77e44e30c1970a"
    sample_text = "Hello, this is a test of the Eleven Labs text-to-speech API."
    text_to_speech(sample_text, eleven_labs_api_key)
