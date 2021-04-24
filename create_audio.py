from gtts import gTTS
from subprocess import call         # Mac / Linux
# from playsound import playsound   # Windows


def create_audio(audio: str) -> None:
    tts = gTTS(audio, lang='en')
    tts.save('audio/hello.mp3')

    #call(['afplay', 'audio/hello.mp3'])    # Mac
    #playsound('audio/hello.mp3')           # Windows
    call(['mpv', 'audio/hello.mp3'])        # Linux



create_audio('Hello I\'m Zera, how can I help you?')