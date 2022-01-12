import pygame, time, os
from cytolk import tolk
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
pygame.init()
screen=pygame.display.set_mode((400,600))
pygame.display.set_caption("2D Grid Testing")

grid=[[-1,-1,-1], [-1,-1,-1], [-1,-1,-1]]

def checkTile(x,y):
    if grid[x][y]==-1:
        return "empty"
    elif grid[x][y] ==0:
        return "x"
    elif grid[x][y]==1:
        return "o"

def placeObject(x,y,type):
    if grid[x][y]==-1:
        grid[x][y]=type
        speak("Object placed.")
    else:
        speak("Something's already on that square.")
def speak(text):
    with tolk.tolk():
        tolk.speak(text)

def getpos(x,y):
    if x==0:
        speak("A")
    elif x==1:
        speak("B")
    elif x==2:
        speak("C")
    speak(f"{y+1}")

class player:
    def __init__(self, name, obj):
        self.x=0
        self.y=0
        self.name=name
        self.obj=obj
p1=player('player1', 0)
p2=player('player2', 1)
p=p1


running=True
while running:
    time.sleep(0.02)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP and p.y<2:
                p.y+=1
                getpos(p.x,p.y)
                speak(f"{checkTile(p.x,p.y)}")
            elif event.key==pygame.K_DOWN and p.y>0:
                p.y-=1
                getpos(p.x,p.y)
                speak(f"{checkTile(p.x,p.y)}")
            elif event.key==pygame.K_LEFT and p.x>0:
                p.x-=1
                getpos(p.x,p.y)
                speak(f"{checkTile(p.x,p.y)}")
            elif event.key==pygame.K_RIGHT and p.x<2:
                p.x+=1
                getpos(p.x,p.y)
                speak(f"{checkTile(p.x,p.y)}")
            elif event.key==pygame.K_RETURN:
                placeObject(p.x,p.y,p.obj)
                if p==p1:
                    p=p2
                else:
                    p=p1
                speak(f"it's now {p.name}'s turn")
            if event.key==pygame.K_q:
                pygame.QUIT()
                quit()
                running=False
