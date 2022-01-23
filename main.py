import kit
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'softi ' in command:
                command = command.replace('softi', '')
                return command
            else:
                  command="sorry"

                  return command
    except:
        pass


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('search for' + time)
    elif 'search for' in command:
        person = command.replace('search for ', '')
        info = wikipedia.summary(person, 10)
        print(info)
        talk(info)
    elif 'who developed you' in command:
        talk('gautham and krishnadev is my boss')

    elif 'where are you working at' in command:
        talk('i am working at softrix tech solutions')

    elif 'tell audience about my company' in command:
           talk('softrics tech solutions is founded on 10 jan 2022. softrics was founded by gautham v nair and krishnadev p melevila. softrics is a kerala based company')
    elif 'my items' in command:
        print('Iphone 13, Iphone XR, HP Pavilion, Lenovo Ideapad Gaming & Circle Gaming PC')

    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke)

    elif 'open our website' in command:
        webbrowser.open('https://softrics.in')

    elif ' local' in command:
        os.system(r"C:\Users\USER\AppData\Local\Programs\Local\Local.exe")

    elif 'open my photo' in command:
        os.system(r"C:\Users\USER\Desktop\1yr/2.jpg")

    elif 'search fort' in command:
        def search_on_wikipedia(query):
            results = wikipedia.summary(query, sentences=2)
            return results

    elif 'search google' in command:
        def search_on_google(query):
            kit.search(query)

    elif 'send message' in command:
        def send_whatsapp_message(number, message):
            kit.sendwhatmsg_instantly(f"+91{9048042009}", "hi")






    else:
        talk('Please say that again')


while True:
    run_alexa()

