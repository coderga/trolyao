from gtts import gTTS
import os
from playsound import playsound
tts = gTTS('Xin chào các bạn',tld='com.vn',lang='vi')

tts.save("hello.mp3")
playsound("hello.mp3")
