from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, List
import yaml
import requests
import boto3
from twilio.rest import Client
from navana_ai import SpeechToText
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from datetime import datetime

app = FastAPI()

# Database setup
DATABASE_URL = "mongodb://localhost:27017"
client = AsyncIOMotorClient(DATABASE_URL)
db = client.navana_ai

# Twilio setup
TWILIO_ACCOUNT_SID = "your_twilio_sid"
TWILIO_AUTH_TOKEN = "your_twilio_token"
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# AWS Polly setup
polly_client = boto3.client('polly')

# NAVANA AI setup
stt_client = SpeechToText()

class TextToSpeechRequest(BaseModel):
    text: str
    voice_id: str = "Joanna"
    output_format: str = "mp3"

class SpeechToTextRequest(BaseModel):
    audio_url: str
    language: str = "en-US"

class CallRequest(BaseModel):
    to_number: str
    from_number: str
    text: str

class CallLog(BaseModel):
    call_sid: str
    from_number: str
    to_number: str
    start_time: datetime
    duration: int
    transcription: Optional[str] = None

@app.get("/")
def read_root():
    return {"message": "Welcome to NAVANA AI Backend with SST, TTS, and Telephony"}

@app.post("/text-to-speech/")
async def convert_text_to_speech(request: TextToSpeechRequest):
    try:
        response = polly_client.synthesize_speech(
            Text=request.text,
            OutputFormat=request.output_format,
            VoiceId=request.voice_id
        )
        audio_stream = response['AudioStream'].read()
        return {"status": "success", "audio": audio_stream}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/speech-to-text/")
async def convert_speech_to_text(request: SpeechToTextRequest):
    try:
        transcription = stt_client.transcribe(
            audio_url=request.audio_url,
            language=request.language
        )
        return {"status": "success", "transcription": transcription}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/make-call/")
async def make_call(request: CallRequest):
    try:
        call = twilio_client.calls.create(
            twiml=f"<Response><Say>{request.text}</Say></Response>",
            to=request.to_number,
            from_=request.from_number
        )
        return {"status": "success", "call_sid": call.sid}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/call-logs/")
async def get_call_logs(limit: int = 10):
    logs = await db.call_logs.find().sort("start_time", -1).limit(limit).to_list(limit)
    return {"status": "success", "logs": logs}

@app.post("/store-call-log/")
async def store_call_log(log: CallLog):
    try:
        result = await db.call_logs.insert_one(log.dict())
        return {"status": "success", "inserted_id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
