# https://pyttsx3.readthedocs.io/en/latest/
# https://www.youtube.com/watch?v=GqTsFOtZiQI      Selecting the correct Python interpreter in VSCode's Python Extension
# py -0


import pyttsx3 as ttsx3

ttsObject = ttsx3.init()
# ttsObject.say("Hello. My name is Vivian")
# ttsObject.runAndWait()


# ttsObject = ttsx3.init()
voices = ttsObject.getProperty("voices")
for voice in voices:
    ttsObject.setProperty("voice", voice.id)
    ttsObject.say("The quick brown fox jumped over the lazy dog.")
    ttsObject.runAndWait()
    print(voice.id)
