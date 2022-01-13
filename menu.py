import speech, pygame
class menu:
    def __init__(self, items):
        self.items=items
        self.focus=0
    def show_menu(self, title):
        speech.speak(title)
        speech.speak(self.items[self.focus])
        opened=True
        while opened:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.focus>0:
                        self.focus=self.focus-1
                        speech.speak(self.items[self.focus])
                    if event.key == pygame.K_DOWN and len(self.items) > self.focus+1:
                        self.focus =self.focus+1
                        speech.speak(self.items[self.focus])
                    if event.key == pygame.K_RETURN:
                        return self.items[self.focus]
                    if event.key == pygame.K_ESCAPE:
                        self.focus=0
                        return 'cancel'
                        opened=False
