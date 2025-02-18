from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import yaml
import requests

app = FastAPI()

class TextToSpeechRequest(BaseModel):
    text: str
    api_key: str

class AgentConfig(BaseModel):
    role: str
    goal: str
    backstory: str

@app.get("/")
def read_root():
    return {"message": "Welcome to NAVANA AI Backend"}

@app.post("/text-to-speech/")
async def convert_text_to_speech(request: TextToSpeechRequest):
    try:
        response = requests.post(
            "https://api.elevenlabs.io/v1/text-to-speech/JBFqnCBsd6RMkjVDRZzb?output_format=mp3_44100_128",
            headers={
                "xi-api-key": request.api_key,
                "Content-Type": "application/json"
            },
            json={
                "text": request.text,
                "model_id": "eleven_multilingual_v2"
            }
        )
        response.raise_for_status()
        return {"status": "success", "message": "Audio conversion successful"}
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/agents/{agent_name}")
async def get_agent_config(agent_name: str):
    try:
        with open("agents.yaml", "r") as file:
            agents = yaml.safe_load(file)
            if agent_name in agents:
                return AgentConfig(**agents[agent_name])
            raise HTTPException(status_code=404, detail="Agent not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
