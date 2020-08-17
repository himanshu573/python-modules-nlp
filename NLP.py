import speech_recognition as sr
import webbrowser
from googletrans import Translator

translator = Translator()
sr.Microphone(device_index=1)

r=sr.Recognizer()

r.energy_threshold=5000

with sr.Microphone() as source:
    
    print("Speak Up!")
    audio=r.listen(source)
    print("Done")
    
    texter=r.recognize_google(audio,language="hi-IN")
    translated = translator.translate(texter, src='hi', dest='gu')
    print(" Translated string:" + translated.text) 
    print(r.recognize_google(audio))

    try:
        translated=r.recognize_google(audio)
        print("You said : {}".format(translated))
        urlyou='https://www.google.co.in/search?q='
        search_urlyou=urlyou+translated
        webbrowser.open(search_urlyou)

        urlyou='https://www.youtube.com/results?search_query=farming+hindi/'
        search_urlyou=urlyou+translated
        webbrowser.open(search_urlyou)
        
    except:
        print("Can't recognize")
