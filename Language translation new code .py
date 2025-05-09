import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import playsound
import os

# Initialize recognizer and translator
recognizer = sr.Recognizer()
translator = Translator()

# Step 1: Capture speech
with sr.Microphone() as source:
    print("Speak now...")
    audio = recognizer.listen(source)

# Step 2: Speech to Text
try:
    text = recognizer.recognize_google(audio)
    print(f"You said: {text}")

    # Step 3: Translate to target language (e.g., French)
    translated = translator.translate(text, dest='fr')
    print(f"Translated: {translated.text}")

    # Step 4: Text to Speech
    tts = gTTS(translated.text, lang='fr')
    filename = "translated.mp3"
    tts.save(filename)

    # Step 5: Play the translated speech
    playsound.playsound(filename)
    os.remove(filename)

except Exception as e:
    print("Error:", e)
