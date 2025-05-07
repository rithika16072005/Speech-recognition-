import speech_recognition as sr
from google_trans_new import google_translator
from gtts import gTTs
from playsound import playsound
import os

r = sr.Recognizer()
translator = google_translator()

while True:
    with sr.Microphone()as source:
        print("speak now!")
        audio = r.listen(source)
        try:
            sperech_text= r.recognize_google(audio)
            print(speech_text)
        except sr.unknownValueError:
            print("could not understand ")
        except sr.RequestError:
            print("colud not request result from google ")
            
        translated_text = translator.translate(speech_text, lang_tgt='fr')
        print(translated text)
        
        voice= gTTS(translated_text,lang='fr')
        voice.save("voice.mp3")
        playsound("voice.mp3")
        os.remove("voice.mp3")
