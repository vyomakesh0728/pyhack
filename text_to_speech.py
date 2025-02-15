import requests
import json

def text_to_speech(text, api_key):
    url = "https://api.elevenlabs.io/v1/text-to-speech/JBFqnCBsd6RMkjVDRZzb?output_format=mp3_44100_128"
    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "model_id": "vQr4tFgr8biGsPoCuPNl"
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
    eleven_labs_api_key = "api_key"
    
    try:
        # Load text from prompts.txt
        with open("/Users/v/pyhack/promtps.txt", "r") as file:
            prompts_data = json.load(file)
        
        # Extract sample text from the prompts
        sample_text = prompts_data["conversation_flow"]["opening_greetings"][0]
        
        text_to_speech(sample_text, eleven_labs_api_key)
    except FileNotFoundError:
        print("Error: The file 'prompts.txt' was not found. Please ensure it exists in the correct directory.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from 'prompts.txt'. Please check the file format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
