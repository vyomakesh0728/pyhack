import requests
import json
import base64
import scipy.io.wavfile
import numpy as np

def text_to_speech(text, api_key):
    url = "https://api.sarvam.ai/text-to-speech"
    headers = {
        "api-subscription-key": api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "inputs": [text],
        "target_language_code": "en-IN",  # Default to Hindi
        "speaker": "meera",  # Default speaker
        "model": "bulbul:v1"
    }
    
    try:
        response = requests.request("POST", url, headers=headers, json=payload)
        response.raise_for_status()
        
        # Check if response contains base64 encoded audio
        response_data = response.json()
        if 'audioContent' in response_data:
            # Decode base64 audio content
            audio_content = base64.b64decode(response_data['audioContent'])
            
            # Convert JSON data to numpy array
            audio_data = np.frombuffer(audio_content, dtype=np.int16)
            
            # Write to WAV file using scipy
            scipy.io.wavfile.write("output_audio.wav", 44100, audio_data)
            print("Audio content successfully written to output_audio.wav")
        else:
            # Enhanced error handling for missing audio content
            print("Error: No audio content found in the response")
            print("Response status code:", response.status_code)
            print("Response headers:", response.headers)
            print("Response content:", response.text)
            return False
        return True
    except requests.exceptions.RequestException as e:
        print("An error occurred during the API request:", e)
        return False
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON response from the API")
        return False
    except base64.binascii.Error:
        print("Error: Failed to decode base64 audio content")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

if __name__ == "__main__":
    sarvam_api_key = "270d52d7-1f85-4cd3-8cf7-a7beac13882a"  # Replace with your actual API key
    
    try:
        # Load text from prompts.txt
        with open("/Users/v/pyhack/promtps.txt", "r") as file:
            prompts_data = json.load(file)
        
        # Extract sample text from the prompts
        sample_text = prompts_data["conversation_flow"]["opening_greetings"][0]
        print("Text to convert:", sample_text)
        
        success = text_to_speech(sample_text, sarvam_api_key)
        if not success:
            print("Failed to generate audio. Please check the API response and configuration.")
    except FileNotFoundError:
        print("Error: The file 'prompts.txt' was not found. Please ensure it exists in the correct directory.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from 'prompts.txt'. Please check the file format.")
    except KeyError as e:
        print(f"Error: Missing expected key in prompts data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
