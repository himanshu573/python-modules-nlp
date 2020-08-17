import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator

r=sr.Recognizer()
translator = Translator()
with sr.Microphone() as source:
    print("Say Something:")
    audio=r.listen(source)
    print("Done")

texter=r.recognize_google(audio,language="hi-IN")
translated = translator.translate(texter, src='hi', dest='gu')
a=translated;
print(" Translated string:" +a.text)
print(r.recognize_google(audio))

