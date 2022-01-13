import speech
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
            speech.speak("Object placed.")
            return True
        else:
            speech.speak("Something's already on that square.")
            return False
    def getpos(self, x,y):
        if x==0:
            speech.speak("A")
        elif x==1:
            speech.speak("B")
        elif x==2:
            speech.speak("C")
        speech.speak(f"{y+1}")
    def reset(self):
        self.__init__()
