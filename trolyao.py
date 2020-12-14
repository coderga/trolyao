#trợ lý ảo tiếng việt bằng python
import speech_recognition as sr
from gtts import gTTS
import os
import playsound
from datetime import datetime,date
import wikipedia

now = datetime.now()
today = date.today()
r = sr.Recognizer()

from path import Path

def speak(text):
    tts = gTTS(text=text, lang='vi')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    #os.remove("voice.mp3")
    Path('voice.mp3').remove_p()


while True:
    with sr.Microphone() as source:
        audio_data = r.record(source, duration=4)
        # print("Recognizing...")
        try:
            text = r.recognize_google(audio_data, language="vi")
            text = text.lower()
        except:
            text = ""
        print(text)

        if text == "":
            robot_brain = "Tôi đang lắng nghe bạn đây"
            print(robot_brain)
            speak(robot_brain)
        elif "xin chào" in text:
            robot_brain = "Chào bạn bạn khỏe không"
            print(robot_brain)
            speak(robot_brain)
        elif "ngày bao nhiêu" in text:
            today = date.today()
            robot_brain = today.strftime("Hôm nay là ngày %d/%m/%Y")
            print(robot_brain)
            speak(robot_brain)
        elif "mấy giờ" in text:
            robot_brain = "Bây giờ là " + now.strftime("%H {x} %M {y} %S {z}").format(x = 'giờ', y = 'phút', z = 'giây')
            print(robot_brain)
            speak(robot_brain)

        elif "Goodbye" in text or "tạm biệt" in text:
            robot_brain = "tạm biệt"
            print(robot_brain)
            speak(robot_brain)
            break
        else:
            robot_brain = "Bạn muốn nói gì với tôi"
            print(robot_brain)
            speak(robot_brain)


