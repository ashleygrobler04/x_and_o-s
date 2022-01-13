import pygame, time, os
from cytolk import tolk
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
pygame.init()
screen=pygame.display.set_mode((400,600))
pygame.display.set_caption("2D Grid Testing")

def speak(text):
    with tolk.tolk():
        tolk.speak(text)

class menu:
    def __init__(self, items):
        self.items=items
        self.focus=0
    def show_menu(self, title):
        speak(title)
        speak(self.items[self.focus])
        opened=True
        while opened:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if self.focus>0:
                            self.focus=self.focus-1
                        speak(self.items[self.focus])
                    if event.key == pygame.K_DOWN:
                        if len(self.items) > self.focus+1:
                            self.focus =self.focus+1
                        speak(self.items[self.focus])
                    if event.key == pygame.K_RETURN:
                        self.focus=0
                        return self.items[self.focus]
                    if event.key == pygame.K_ESCAPE:
                        self.focus=0
                        return 'cancel'
                        opened=False

class bord:
    def __init__(self):
        self.squares=[[-1,-1,-1], [-1,-1,-1], [-1,-1,-1]]
    def checkTile(self,x,y):
        if self.squares[x][y]==-1:
            return "empty"
        elif self.squares[x][y] ==0:
            return "x"
        elif self.squares[x][y]==1:
            return "o"

    def placeObject(self, x,y,type):
        if self.squares[x][y]==-1:
            self.squares[x][y]=type
            speak("Object placed.")
        else:
            speak("Something's already on that square.")
    def getpos(self, x,y):
        if x==0:
            speak("A")
        elif x==1:
            speak("B")
        elif x==2:
            speak("C")
        speak(f"{y+1}")
    def reset(self):
        self.__init__()

class player:
    def __init__(self, name, obj):
        self.x=0
        self.y=0
        self.name=name
        self.obj=obj
Grid=bord()
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
    global running
    horizontal1=Grid.squares[0]
    horizontal2=Grid.squares[1]
    horizontal3=Grid.squares[2]
    vertical1=[Grid.squares[0][0], Grid.squares[1][0], Grid.squares[2][0]]
    vertical2=[Grid.squares[0][1], Grid.squares[1][1], Grid.squares[2][1]]
    vertical3=[Grid.squares[0][2], Grid.squares[1][2], Grid.squares[2][2]]
    diagonal1=[Grid.squares[0][0],Grid.squares[1][1],Grid.squares[2][2]]
    diagonal2=[Grid.squares[0][2],Grid.squares[1][1],Grid.squares[2][0]]
    x=[0,0,0]
    o=[1,1,1]
    if horizontal1 == x or horizontal2 == x or horizontal3 == x or vertical1 == x or vertical2 == x or vertical3 == x or diagonal1 == x or diagonal2 == x:
        display_message('player1 is the winner')
        running=False
        Grid.reset()
        p1.x=0
        p1.y=0
        p2.x=0
        p2.y=0
        p=p1
    elif horizontal1 == o or horizontal2 == o or horizontal3 == o or vertical1 == o or vertical2 == o or vertical3 == o or diagonal1 == o or diagonal2 == o:
        display_message('player2 is the winner')
        running=False
        Grid.reset()
        p1.x=0
        p1.y=0
        p2.x=0
        p2.y=0
        p=p1
    else:
        pass

def main_menu():
    mainmenu=menu(['play', 'exit'])
    while 1:
        pygame.display.update()
        choice=mainmenu.show_menu('select an option with up and down arrow keys. press enter to activate the option')
        if choice == 'play':
            start_game()
        if choice == 'exit' or choice == 'cancel':
            pygame.quit()
            quit()
p1=player('player1', 0)
p2=player('player2', 1)
p=p1

running=True
def start_game():
    global running
    global p1
    global p2
    global p
    if not running:
        running=True
    while running:
        time.sleep(0.02)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP and p.y<2:
                    p.y+=1
                    Grid.getpos(p.x,p.y)
                    speak(f"{Grid.checkTile(p.x,p.y)}")
                elif event.key==pygame.K_DOWN and p.y>0:
                    p.y-=1
                    Grid.getpos(p.x,p.y)
                    speak(f"{Grid.checkTile(p.x,p.y)}")
                elif event.key==pygame.K_LEFT and p.x>0:
                    p.x-=1
                    Grid.getpos(p.x,p.y)
                    speak(f"{Grid.checkTile(p.x,p.y)}")
                elif event.key==pygame.K_RIGHT and p.x<2:
                    p.x+=1
                    Grid.getpos(p.x,p.y)
                    speak(f"{Grid.checkTile(p.x,p.y)}")
                elif event.key==pygame.K_RETURN:
                    Grid.placeObject(p.x,p.y,p.obj)
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

main_menu()
