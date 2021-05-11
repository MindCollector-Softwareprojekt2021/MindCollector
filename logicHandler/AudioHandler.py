import speech_recognition

def getAudioText(path):
    r = speech_recognition.Recognizer()
    with speech_recognition.AudioFile(path) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data, language="de-DE")
        return text