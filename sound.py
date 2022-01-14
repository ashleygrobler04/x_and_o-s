import synthizer

ctx=synthizer.Context()

class sound:
    def __init__(self, ctx, file):
        self.ctx=ctx
        self.source=synthizer.DirectSource(self.ctx)
        self.buffer=synthizer.Buffer.from_file(file)
        self.generator=None
    def play(self):
        if not self.generator:
            self.generator=synthizer.BufferGenerator(self.ctx)
            self.generator.buffer.value=self.buffer
            self.source.add_generator(self.generator)
        else:
            if self.generator.playback_position.value >= self.buffer.get_length_in_seconds():
                    self.generator.playback_position.value=0
            self.source.play()
    def pause(self):
        self.source.pause()
    def stop(self):
        if self.generator:
            self.source.remove_generator(self.generator)
            self.generator=None
        else:
            pass

class sound2d(sound):
    def __init__(self, ctx, file, default_x=0, default_y=0):
        self.ctx=ctx
        self.source=synthizer.Source3D(self.ctx)
        self.generator=None
        self.buffer=synthizer.Buffer.from_file(file)
        self.source.position.value=(default_x, default_y, 0)
    def update_position(self, x,y):
        self.source.position.value=(x,y,0)