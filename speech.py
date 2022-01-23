from cytolk import tolk

def speak(text):
    with tolk.tolk(False):
        tolk.speak(text)
