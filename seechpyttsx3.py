import pyttsx3
import os, numpy

os.system('cls')
# os.system('color %s' % numpy.random.randint(9))
os.system('color 6')
engine = pyttsx3.init()
# engine = pyttsx3.init('sapi5') 
# engine = pyttsx3.init(driverName='sapi5') 


voices = engine.getProperty("voices")

for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)


vi_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An"
#vi_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\Hong Vi"
# vi_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\quynhchau"
# vi_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\SPEECH\Voices\Tokens\eSpeak_1"
# vi_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\SPEECH\Voices\Tokens\eSpeak"
# vi_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\SPEECH\Voices\Tokens\MSTTS_V110_viVN_An"



# engine.setProperty('voice', voices[3].id) 
engine.setProperty("voice",vi_voice_id)
engine.say("Xin chào các bạn, các bạn có khỏe không")
engine.runAndWait()

