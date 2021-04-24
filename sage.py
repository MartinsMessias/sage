from subprocess import call         # Mac / Linux
# from playsound import playsound   # Windows
from bs4 import BeautifulSoup
from create_audio import create_audio

import requests
import speech_recognition as sr
import webbrowser as browser


#Hotwords

hotword = 'sage'

def mic_monitor() -> None:
    # obtain audio from the microphone
    mic = sr.Recognizer()

    responds('hello')

    with sr.Microphone() as source:
        while True:
            print("Waiting for instructions")
            mic.adjust_for_ambient_noise(source, duration=1)
            audio = mic.listen(source)

            # recognize speech using Google Speech Recognition
            try:
                trigger = mic.recognize_google(audio, language='en')
                trigger = trigger.lower()
                print(trigger)

                if hotword or 'stage' in trigger:
                    print('Command:', trigger)
                    exec_commands(trigger)
                    break

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return trigger

def responds(file) -> None:
    call(['mpv', f'audio/{file}.mp3'])  # Linux


def exec_commands(trigger):
    if 'news' in trigger:
        last_news()
    elif 'play' in trigger:
        playlists()
    else:
        message = trigger.strip(hotword)

        if len(message) <= 1:
            responds('hello')
        else:
            create_audio(message)
            print('Invalid command: ', message)
            responds('invalid_command')

def last_news():
    url = 'https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt'
    news = requests.get(url)
    news = BeautifulSoup(news.text, 'html.parser')

    for item in news.findAll('item')[:5]:
        message = item.title.text
        create_audio(message)


def playlists():
    browser.open('https://open.spotify.com/playlist/37i9dQZF1DXcmaoFmN75bi?si=pbKRmoETQMmoEwHVEgs5sg&nd=1')

if __name__ == '__main__':
    mic_monitor()