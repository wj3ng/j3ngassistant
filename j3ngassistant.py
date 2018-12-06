from speechHandler import VoiceRecorder

if __name__ == '__main__':

    vr = VoiceRecorder()
    
    vr.startListening()

    input('press enter to end')
    vr.stopListening()

    # print('What do you want me to say?')
    # speechHandler.gttsSay(input())

    # while True:
    #     print(speechHandler.getSpeech())