import pyttsx3

def text_to_speech_tts(text, output_file="output/output_audio.mp3"):
    """Convert text to speech and save as an MP3 file."""
    engine = pyttsx3.init()
    engine.save_to_file(text, output_file)
    engine.runAndWait()
    return output_file
