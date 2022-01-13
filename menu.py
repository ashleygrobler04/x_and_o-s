import speech, pygame
import synthizer
synthizer.initialize()
from sound import ctx, sound

class menu:
    def __init__(self, items):
        self.items=items
        self.focus=0
        self.scrolling_sound=sound(ctx, "sounds/menu_scroll.flac")
        self.enter_sound=sound(ctx, "sounds/menu_enter.flac")
    def show_menu(self, title):
        speech.speak(title)
        speech.speak(self.items[self.focus])
        opened=True
        while opened:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.focus>0:
                        self.scrolling_sound.play()
                        self.focus=self.focus-1
                        speech.speak(self.items[self.focus])
                    if event.key == pygame.K_DOWN and len(self.items) > self.focus+1:
                        self.scrolling_sound.play()
                        self.focus =self.focus+1
                        speech.speak(self.items[self.focus])
                    if event.key == pygame.K_RETURN:
                        self.enter_sound.play()
                        return self.items[self.focus]
                    if event.key == pygame.K_ESCAPE:
                        self.focus=0
                        return 'cancel'
                        opened=False
