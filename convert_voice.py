import pyttsx3
converter = pyttsx3.init()

# convert the male voice to female voice
voices = converter.getProperty('voices')
for voice in voices:
   converter.setProperty('voice', voice.id)
   converter.say('The quick brown fox jumped over the lazy dog.')
converter.runAndWait()
