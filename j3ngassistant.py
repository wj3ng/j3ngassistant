import speechHandler
import commandHandler


assistantName = 'alexa'

def listenForSpeech():

    while True:

        response = speechHandler.getSpeech()

        if response['error'] is not None:
            print('Speech not recognized.')
        else:
            transcription = response['transcription'].lower()
            print('"' + transcription.replace(assistantName + ' ', assistantName.upper() + ' ', 1) + '"')
            if assistantName + ' ' in transcription:
                command = transcription[transcription.index(assistantName + ' ') + len(assistantName) + 1:]
                commandHandler.parseCommand(command)
                # deal with command


if __name__ == '__main__':

    listenForSpeech()

    # print('What do you want me to say?')
    # speechHandler.gttsSay(input())

    # while True:
    #     print(speechHandler.getSpeech())