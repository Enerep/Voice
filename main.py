#Import Modules
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS


class HearAndTell:
    
    # Speaking function
    def tell(self, text):
        tts = gTTS(text=text, lang="en")
        filename = "voice.mp3"
        tts.save(filename)
        playsound.playsound(filename)

     # Hearing our audio function
    def hear(self):
        recog = sr.Recognizer()
        with sr.Microphone() as source:
            audio = recog.listen(source)
            said = ""

            try:
                said = recog.recognize_google(audio)
                print(said)
            except Exception as e:
                print("Exception: " + str(e))

        return said


do = HearAndTell()

text = do.hear()

if "hello" in text:
    do.Tell("hello, how are you?")
elif "what is your name" in text:
    do.Tell("My name is Bat")
