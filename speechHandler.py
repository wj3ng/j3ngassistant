import speech_recognition as sr
import os
from gtts import gTTS 
from io import BytesIO
from pygame import mixer


class VoiceRecorder:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def __callback(self, r, audio):

        try:
            transcription = r.recognize_google(audio)
            print('"{0}"'.format(transcription))
        except sr.UnknownValueError:
            print('Could not understand audio.')
        except sr.RequestError as e:
            print('ERROR: {0}'.format(e))

    def startListening(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
        self.stopListening = self.recognizer.listen_in_background(self.microphone,self.__callback)



# # uses gTTS to turn text into speech in a mp3 file and play it
# def gttsSay(content, language='en', slow=False):

#     tts = gTTS(content,language,slow)
#     tts.save('tempTTS.mp3')

#     # maybe not a good idea to init every time?
#     mixer.init()
#     mixer.music.load('tempTTS.mp3')
#     mixer.music.play()

#     # waits until track finishes playing to exit the method
#     while mixer.music.get_busy():
#         pass
