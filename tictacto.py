import pygame, time
from cytolk import tolk
from pygame import key
from pygame.constants import KEYDOWN
pygame.init()
screen=pygame.display.set_mode((400,600))
pygame.display.set_caption("2D Grid Testing")

grid=[[-1,-1,-1], [1,1,1], [0,0,0]]

def checkTile(x,y):
    if grid[x][y]==-1:
        return "empty"
    elif grid[x][y] ==0:
        return "x"
    elif grid[x][y]==1:
        return "o"

def speak(text):
    with tolk.tolk():
        tolk.speak(text)

class player:
    def __init__(self):
        self.x=0
        self.y=0
p=player()
running=True
while running:
    time.sleep(0.02)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP and p.y<2:
                p.y+=1
                speak(f"{checkTile(p.x,p.y)}")
            elif event.key==pygame.K_DOWN and p.y>0:
                p.y-=1
                speak(f"{checkTile(p.x,p.y)}")
            elif event.key==pygame.K_LEFT and p.x>0:
                p.x-=1
                speak(f"{checkTile(p.x,p.y)}")
            elif event.key==pygame.K_RIGHT and p.x<2:
                p.x+=1
                speak(f"{checkTile(p.x,p.y)}")
            if event.key==pygame.K_q:
                pygame.QUIT()
                quit()
                running=False
