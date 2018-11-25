import speechHandler


# responds to tracer memes
def illBeTracer(command):
    tracer = {
        'i want to be tracer',
        'i wanna be tracer',
        'maybe i\'ll be tracer',
        'maybe i\'ll beat racer',
        'i\'ll be tracer',
        'what about tracer'
    }

    if command in tracer:
        speechHandler.gttsSay('I\'m already Tracer.')
        return True

    return False

def parseCommand(command):

    if command[-6:] == 'cancel':
        return
    # print('received command "{0}"'.format(command))

    if illBeTracer(command):
        return