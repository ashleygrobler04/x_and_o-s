import pygame, speech
def display_message(message):
    speech.speak(message)
    displaying=True
    while displaying:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    speech.speak(message)
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                    displaying=False
