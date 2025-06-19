import whisper
import tempfile

# Load model once on startup
model = whisper.load_model("base")  # You can switch to "small" if needed

def transcribe_audio(audio_bytes: bytes) -> str:
    # Save uploaded bytes to a temporary file
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        tmp.write(audio_bytes)
        tmp_path = tmp.name
    # Run Whisper transcription
    result = model.transcribe(tmp_path)
    return result["text"]
