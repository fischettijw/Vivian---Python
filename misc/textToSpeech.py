# https://pyttsx3.readthedocs.io/en/latest/

import pyttsx3 as ttsx3

ttsObject = ttsx3.init()
ttsObject.setProperty("voice","HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0")
ttsObject.say("Hello. My name is John")
ttsObject.runAndWait()


# ttsObject = ttsx3.init()
voices = ttsObject.getProperty("voices")
print(voices[0].id)
for voice in voices:
    ttsObject.setProperty("voice", voice.id)
    ttsObject.say("The quick brown fox jumped over the lazy dog.")
    ttsObject.runAndWait()
    print(voice.id)
