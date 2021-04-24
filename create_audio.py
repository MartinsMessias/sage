from gtts import gTTS
from subprocess import call         # Mac / Linux
# from playsound import playsound   # Windows


def create_audio(message: str) -> None:
    tts = gTTS(message, lang='en')
    tts.save(f'audio/message.mp3')
    print('Sage:', message)
    #call(['afplay', 'audio/hello.mp3'])    # Mac
    #playsound('audio/hello.mp3')           # Windows
    call(['mpv', 'audio/message.mp3'])        # Linux



