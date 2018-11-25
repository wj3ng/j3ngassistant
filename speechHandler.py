import speech_recognition as sr
import os
from gtts import gTTS 
from io import BytesIO
from pygame import mixer

# returns object with success (bool), error (str), and transcription (str)
def getSpeech(recognizer=sr.Recognizer(), microphone=sr.Microphone()): 

    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")
    
    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught, update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response


# uses gTTS to turn text into speech in a mp3 file and play it
def gttsSay(content, language="en", slow=False):

    tts = gTTS(content,language,slow)
    tts.save('tempTTS.mp3')

    # maybe not a good idea to init every time?
    mixer.init()
    mixer.music.load('tempTTS.mp3')
    mixer.music.play()

    # waits until track finishes playing to exit the method
    while mixer.music.get_busy():
        pass
