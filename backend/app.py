from fastapi import FastAPI, UploadFile, File
from whisper_module import transcribe_audio

app = FastAPI()

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    audio_bytes = await file.read()
    transcript = transcribe_audio(audio_bytes)
    return {"transcript": transcript}
