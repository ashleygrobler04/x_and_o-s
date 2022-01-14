import synthizer
import random
synthizer.initialize()
import pygame, time, os, speech, bord, player, menu, display
from sound import ctx, sound2d

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
pygame.init()
screen=pygame.display.set_mode((400,600))
pygame.display.set_caption("2D Grid Testing")
Grid=bord.bord()
p1=player.player("player 1", 0)
p2=player.player("player 2", 1)
grid_moved=sound2d(ctx, "sounds/grid_moved.flac")
object_placed=sound2d(ctx, "sounds/object_placed.flac")



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
        display.display_message('player1 is the winner')
        Grid.reset()
        running=False
        p1.x=0
        p1.y=0
        p2.x=0
        p2.y=0
        p=p1
    elif horizontal1 == o or horizontal2 == o or horizontal3 == o or vertical1 == o or vertical2 == o or vertical3 == o or diagonal1 == o or diagonal2 == o:
        display.display_message('player2 is the winner')
        Grid.reset()
        running=False
        p1.x=0
        p1.y=0
        p2.x=0
        p2.y=0
        p=p1
    else:
        pass

def main_menu():
    mainmenu=menu.menu(['play human vs human', 'play human vs computer', 'exit'])
    while 1:
        pygame.display.update()
        choice=mainmenu.show_menu('select an option with up and down arrow keys. press enter to activate the option')
        if choice == 'play human vs human':
            start_game()
        if choice == 'play human vs computer':
            start_game(computer=True)
        else:
            pygame.quit()
            quit()
p=p1

def make_computer_move():
    x=0
    y=0
    positions=[]
    while x<=2:
        while y<=2:
            if Grid.checkTile(x,y) == 'empty':
                positions.append((x,y))
            y+=1
        x+=1
    pos=random.choice(positions)
    Grid.placeObject(*pos, 1)

running=True
def start_game(computer=False):
    global running
    global p1
    global p2
    global p
    if not running:
        running=True
    while running:
        time.sleep(0.02)
        grid_moved.update_position(p.x,p.y)
        object_placed.update_position(p.x,p.y)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP and p.y<2:
                    p.y+=1
                    Grid.getpos(p.x,p.y)
                    speech.speak(f"{Grid.checkTile(p.x,p.y)}")
                    grid_moved.stop()
                    grid_moved.play()
                elif event.key==pygame.K_DOWN and p.y>0:
                    p.y-=1
                    Grid.getpos(p.x,p.y)
                    speech.speak(f"{Grid.checkTile(p.x,p.y)}")
                    grid_moved.stop()
                    grid_moved.play()
                elif event.key==pygame.K_LEFT and p.x>0:
                    p.x-=1
                    Grid.getpos(p.x,p.y)
                    speech.speak(f"{Grid.checkTile(p.x,p.y)}")
                    grid_moved.stop()
                    grid_moved.play()
                elif event.key==pygame.K_RIGHT and p.x<2:
                    p.x+=1
                    Grid.getpos(p.x,p.y)
                    speech.speak(f"{Grid.checkTile(p.x,p.y)}")
                    grid_moved.stop()
                    grid_moved.play()
                elif event.key==pygame.K_RETURN:
                    object_placed.stop()
                    object_placed.play()
                    if Grid.placeObject(p.x,p.y,p.obj):
                        if not computer:
                            if p==p1:
                                p=p2
                            else:
                                p=p1
                        else:
                            make_computer_move()
                        speech.speak(f"it's now {p.name}'s turn")
                if event.key==pygame.K_q:
                    running=False
                    main_menu()
        winloop()
if __name__ == "__main__":
    main_menu()
