from cytolk import tolk


tolk.try_sapi(True)
tolk.prefer_sapi(False)
with tolk.tolk():
    tolk.detect_screen_reader()
    speak(text)

def speak(text):
    tolk.speak(text)
