import synthizer

ctx=synthizer.Context()

class sound:
    def __init__(self, ctx, file):
        self.source=synthizer.DirectSource(ctx)
        self.buffer=synthizer.Buffer.from_file(file)
        self.generator=None
    def play(self):
        if not self.generator:
            self.generator=synthizer.BufferGenerator(ctx)
            self.generator.buffer.value=self.buffer
            self.generator.config_delete_behavior(linger=True)
            self.source.add_generator(self.generator)
        else:
            self.source.play()
    def pause(self):
        self.source.pause()
    def stop(self):
        self.source.remove_generator(self.generator)
        self.generator=None
