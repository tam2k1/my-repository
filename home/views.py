from django.shortcuts import render
import requests
from .main import GenericAssistant
from .voice_assistant import *
from django.http import HttpResponse
import os 
import time

jsondir_url = os.getcwd() + "/home/intents_test.json"
assistant = GenericAssistant(jsondir_url, intent_methods = mapping)
assistant.load_model('MyAssistanModel')

def start(requests):
    return render(requests, 'index.html')
def userCommand(requests):
    path = os.getcwd()
    name = "output.mp3"
    for root, dirs, files in os.walk(path):
        if name in files:
            os.remove("output.mp3")
    try:
        with speech_recognition.Microphone() as mic:
            print("Đang nghe...")
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)         
            message = recognizer.recognize_google(audio, language="vi-VI")
            time.sleep(3)
            message = message.lower()
            print("Bạn vừa nói: " + message)
        response = assistant.request(message)
    except Exception:   #in any case of On Internet
        message = "Mời bạn nhắc lại"
        response = "Xin lỗi tôi chưa hiểu ý bạn, bạn có thể nhắc lại không!"
    # return render(requests, 'index.html',{"command":data[0], "result":data[1]})
    return render(requests, 'index.html',{"command":message, "result":response})


