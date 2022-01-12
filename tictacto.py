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

def display_message(message):
    speak(message)
    displaying=True
    while displaying:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    speak(message)
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                    displaying=False
                

def winloop():
    horizontal1=grid[0]
    horizontal2=grid[1]
    horizontal3=grid[2]
    vertical1=[grid[0][0], grid[1][0], grid[2][0]]
    vertical2=[grid[0][1], grid[1][1], grid[2][1]]
    vertical3=[grid[0][2], grid[1][2], grid[2][2]]
    diagonal1=[grid[0][0],grid[1][1],grid[2][2]]
    diagonal2=[grid[0][2],grid[1][1],grid[2][0]]
    x=[0,0,0]
    o=[1,1,1]
    if horizontal1 == x or horizontal2 == x or horizontal3 == x or vertical1 == x or vertical2 == x or vertical3 == x or diagonal1 == x or diagonal2 == x:
        display_message('player1 is the winner')
        pygame.quit()
        quit()
    elif horizontal1 == o or horizontal2 == o or horizontal3 == o or vertical1 == o or vertical2 == o or vertical3 == o or diagonal1 == o or diagonal2 == o:
        display_message('player2 is the winner')
        pygame.quit()
        quit()
    else:
        pass

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
    winloop()
