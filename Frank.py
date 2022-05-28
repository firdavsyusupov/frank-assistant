# Голосовой ассистент Френк 1.0 BETA | Voice assistent FRANK 1.0 BETA
import os
import time
import speech_recognition as sr # Используется для распознания речи  
from fuzzywuzzy import fuzz
import pyttsx3  # Используется для перевода текста в речь
import datetime
 
# Настройки | Settings
opts = {
    "name": ('Фрэнк','Френк','франк','фк','фрэн','фран','фрак','франк', 'frank', 'пранк'), # Activate the bot | Активировать бота 
    "call": ('скажи','расскажи','покажи','сколько','произнести'), # Auxiliary words | Вспомогательные слова
    "cmds": {  # Bot commands | Команды бота
        "ctime": ('время сейчас','сколько времени','часы','time now','what time','what time is it'), # Time | Время
        "radio": ('где музыка','','включи музыку','музыка','музика'), # turn on music | Включить музыку 
        "stupid1": ('расскажи анекдот','анекдот','пошутим'), # Not understanding words | Не понимаюющие слова
        "info": ('информация о тебе','инфо','расскажи о себе'), # Information about the bot | Информация о боте
        "talk": ('поговорим','поговорить','общаться','привет'), # Talk to the bot | Говорить с ботом
        "stop": ('стоп','стой','остановись','выключайся')  # Stop the bot | Остановить бота
             }
        }
 
# Функции | Functions
def speak(what):
    print( what )
    speak_engine.say( what )
    speak_engine.runAndWait()
    speak_engine.stop()
 
def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language = "ru-RU").lower()
        print("[log] Recognized: " + voice)
    
        if voice.startswith(opts["name"]):
            # Обращаются к ассистенту | Turn to the assistant
            cmd = voice
 
            for x in opts['name']:
                cmd = cmd.replace(x, "").strip()
            
            for x in opts['call']:
                cmd = cmd.replace(x, "").strip()
            
            # Распознаем и выполняем команду | We recognize and execute the command
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])
 
    except sr.UnknownValueError:
        print("[log] Команда не расспознана!")
    except sr.RequestError as e:
        print("[log] Связь прервана! Пожалуйста проверьте ваш интернет!")
 
def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c,v in opts['cmds'].items():
 
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    
    return RC
 
def execute_cmd(cmd):
    if cmd == 'ctime':
        # Cказать текущее время | Tell the current time 
        now = datetime.datetime.now()
        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))
        #stop_listening = r.listen_in_background(m, callback)
        #while True: time.sleep(0.1) # infinity loop
    
    elif cmd == 'radio':
        # Воспроизвести радио | Turn on music
        os.system("G:\\music\\Taksist_Rusik_-_Gde_spasibo_Despacito_Parodiya_Sover_(iPleer.fm).mp3")
        #os.system("Disk:\\folder\\folder\\musik.mp3")
    
    elif cmd == 'stupid1':
        # Not understanding words | Не понимаюющие слова
        speak("Пока что, я не умею шутить. Но вскором времени мой разработчик научит меня шутить как человек")
        stop_listening = r.listen_in_background(m, callback)
        while True: time.sleep(0.01) # infinity loop

    elif cmd == 'info':
        speak("Меня зовут Френк. Для друзей просто Кеша")
        speak("Я умею помогать, разговаривать свами")
        speak("Подробно вы можете прочитать обо мне на оффициальном портале")

    elif cmd == 'talk':
        speak("Привет, как поживает мой господин?")
        time.sleep(2)
        speak("Давайте вы будете, продолжать свою работу!")

    elif cmd == 'stop':
        # Выключается | Turn off the bot
        speak("Вот тут обидно было. Могли бы просто выключить меня, я бы не заметил бы.")

    else:
        print('Ваш голос не расспознан!')
        print('Пожалуйста повторите попытку!')
 
# Запуск | Start
r = sr.Recognizer()
m = sr.Microphone(device_index = 1)
 
with m as source:
    r.adjust_for_ambient_noise(source) # Слушает фон, для распознания речи
 
speak_engine = pyttsx3.init()
 
# Включить можно если работает синтезатор речи
#voices = speak_engine.getProperty('voices')
#speak_engine.setProperty('voice', voices[4].id)
 
#  cmd test
#speak("Мой разработчик не научил меня анекдотам ... Ха ха ха")
speak("Здравствуйте мой повелитель")
speak("Френк вас слушает...")

stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.1) # infinity loop