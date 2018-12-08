from gtts import gTTS
import speech_recognition as sr
import pygame
import os

def say_gtts(content, lang='en', slow=False):
    """Plays Google TTS of a sentence"""
    # TODO: use TemporaryFile instead of saving mp3 file
    tts = gTTS(content, lang, slow)
    tts.save('tempTTS.mp3')
    pygame.mixer.music.load('tempTTS.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy(): 
        pygame.time.Clock().tick(10)

def parse_command(transcription):
    """Deals with said sentences"""
    pass

def listen_callback(r, audio):
    """called when listening to voice in background"""
    try:
        transcription = r.recognize_google(audio)
        print('"{0}"'.format(transcription))
    except sr.UnknownValueError:
        print('Could not understand audio.')
    except sr.RequestError as e:
        print('ERROR: {0}'.format(e))


# # initialize voice recording and speech recognition
# recognizer = sr.Recognizer()
# microphone = sr.Microphone()
# 
# # adjust for ambient noise (should make longer)
# with microphone as source:
    # recognizer.adjust_for_ambient_noise(source)
# 
# init pygame and pygame pygame.mixer
pygame.init()
pygame.mixer.init()

say_gtts('hello world okay, playing despacito')

# # starts listening in background, use stopListening() to stop
# stopListening = recognizer.listen_in_background(microphone,listen_callback)