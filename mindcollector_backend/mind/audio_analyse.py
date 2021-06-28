import speech_recognition
import logging

def audio_analyse(file):  #eintrag

    recognizer = speech_recognition.Recognizer()
    with speech_recognition.AudioFile("/home/McCurly/mindcollector/media/" + file) as source:

        audio_data = recognizer.record(source)

        text = recognizer.recognize_google(audio_data, language="de-DE")

        logging.info('audio_analyse used. Result: ' + str(text))
        #return text