import whisper

# Load model (first time download hoga)
model = whisper.load_model("base")

# Convert audio to text
result = model.transcribe("meeting.mp3")

print("\n===== TRANSCRIPT =====\n")
print(result["text"])