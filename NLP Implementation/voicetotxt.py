import speech_recognition as sr

filename = "Voice 020.wav"
filename = "Voice 019.wav"
filename = "Voice 018.wav"
filename = "Voice 017.wav"
filename = "Voice 016.wav"
filename = "Voice 015.wav"
filename = "Voice 014.wav"

r = sr.Recognizer()

with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)
