import time

class timer:
    def __init__(self):
        self.time=time.time()
    @property
    def elapsed(self):
        current_time=time.time()
        return int(round((current_time-self.time)*1000))
    def restart(self):
        self.time=time.time()
