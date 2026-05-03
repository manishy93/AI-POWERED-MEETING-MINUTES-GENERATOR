import whisper

# Load model
model = whisper.load_model("base")

def generate_minutes_from_audio(audio_file):
    result = model.transcribe(audio_file)
    text = result["text"]

    lines = text.split(".")

    summary = " ".join(lines[:2])

    key_points = "\n".join(
        [f"- {line.strip()}" for line in lines if line.strip()]
    )

    action_items = []
    for line in lines:
        if "will" in line.lower():
            action_items.append(f"- {line.strip()}")

    return f"""
===== AI MEETING MINUTES =====

Summary:
{summary}

Key Points:
{key_points}

Action Items:
{''.join(action_items)}
"""

# 🔥 IMPORTANT: this line should use audio file
if __name__ == "__main__":
    print(generate_minutes_from_audio("meeting.mp3"))