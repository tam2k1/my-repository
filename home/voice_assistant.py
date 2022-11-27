import speech_recognition
from .texttospeech import texttospeech
from .main import GenericAssistant
import wikipedia
from datetime import datetime
import webbrowser
import time
import wolframalpha
import requests, json
import random
import os
from gtts import gTTS
import playsound

recognizer = speech_recognition.Recognizer()
now = datetime.now()

def OpenYoutube():
    webbrowser.open_new_tab("https://www.youtube.ca")
    texttospeech("Đã mở Youtube theo yêu cầu của bạn")
def SearchGoogle():
    webbrowser.open_new_tab("https://www.google.com")
    texttospeech("Đã mở Google theo yêu cầu của bạn")
def Time():
    global now
    time = now.strftime("%H:%M:%S")
    texttospeech(time)
    print (time)
def Date():
    global now
    answer = now.strftime("Ngày: %d, tháng: %m, năm: %Y")
    texttospeech(answer)
    print(answer)
def SearchWiki():
    pass
def Weather():
    pass
mapping = {
    "Mở Youtube": OpenYoutube,
    "Mở Google": SearchGoogle,
    "ngày tháng năm": Date,
    "Mấy giờ": Time,
    "Tìm kiếm trên Wikipedia": SearchWiki,
    "Thời tiết": Weather
}
#jsondir_url = os.getcwd() + "\home\intents_test.json"
#assistant = GenericAssistant(jsondir_url, intent_methods = mapping)
#assistant.train_model()
#assistant.save_model('MyAssistanModel')
#assistant.load_model('MyAssistanModel')
# def working():
    
#     while True:
#         path = os.getcwd()
#         name = "output.mp3"
#         for root, dirs, files in os.walk(path):
#             if name in files:
#                 os.remove("output.mp3")
#         try:
#             with speech_recognition.Microphone() as mic:
#                 print("Đang nghe...")
#                 recognizer.adjust_for_ambient_noise(mic, duration=0.2)
#                 audio = recognizer.listen(mic)

#                 message = recognizer.recognize_google(audio, language="vi-VI")
#                 message = message.lower()
#                 print("Bạn vừa nói: " + message)
#             #assistant.request(message)

#         except:
#             #recognizer = speech_recognition.Recognizer()
#             resp = "Xin lỗi tôi chưa hiểu ý bạn, bạn có thể nhắc lại không!"
#             texttospeech(resp)
#             print("Trợ lý ảo: ", resp)
#         return message
# def training():
#     assistant = GenericAssistant(jsondir_url, intent_methods = mapping)
#     assistant.load_model('MyAssistanModel')
#     print("Training successfull!")
# def takeCommand():
#     training
#     while True:
#         try:
#             with speech_recognition.Microphone() as mic:
#                 print("Đang nghe...")
#                 recognizer.adjust_for_ambient_noise(mic, duration=0.2)
#                 audio = recognizer.listen(mic)         
#                 message = recognizer.recognize_google(audio, language="vi-VI")
#                 message = message.lower()
#                 print("Bạn vừa nói: " + message)
#             response = assistant.request(message)
#         except Exception:   #in any case of On Internet
#             message = "Mời bạn nhắc lại"
#             response = "Xin lỗi tôi chưa hiểu ý bạn, bạn có thể nhắc lại không!"
        
#         return message, response
# def excuteCommand():
#     pass