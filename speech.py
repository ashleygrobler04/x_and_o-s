from cytolk import tolk

def speak(text):
    with tolk.tolk():
        tolk.speak(text)
