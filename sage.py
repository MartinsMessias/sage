import speech_recognition as sr

#Hotwords
hotword = 'sage'

def mic_monitor() -> None:
    # obtain audio from the microphone
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Waiting for instructions")
            mic.adjust_for_ambient_noise(source, duration=3)
            audio = mic.listen(source)

            # recognize speech using Google Speech Recognition
            try:
                trigger = mic.recognize_google(audio, language='en')
                trigger = trigger.lower()
                print(trigger)

                if hotword in trigger:
                    print('Command: ', trigger)
                    ## then
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
