from cytolk import tolk

def speak(text):
    tolk.try_sapi(True)
    tolk.prefer_sapi(False)
    with tolk.tolk():
        tolk.detect_screen_reader()
        tolk.speak(text)
