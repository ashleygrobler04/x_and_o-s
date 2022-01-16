def moves_left(bord):
    for x in range(3):
        for y in range(3):
            if bord.squares[x][y] == -1:
                return True
    return False

def evaluate(bord):
    horizontal1=bord.squares[0]
    horizontal2=bord.squares[1]
    horizontal3=bord.squares[2]
    vertical1=[bord.squares[0][0], bord.squares[1][0], bord.squares[2][0]]
    vertical2=[bord.squares[0][1], bord.squares[1][1], bord.squares[2][1]]
    vertical3=[bord.squares[0][2], bord.squares[1][2], bord.squares[2][2]]
    diagonal1=[bord.squares[0][0],bord.squares[1][1],bord.squares[2][2]]
    diagonal2=[bord.squares[0][2],bord.squares[1][1],bord.squares[2][0]]
    x=[0,0,0]
    o=[1,1,1]
    if horizontal1 == x or horizontal2 == x or horizontal3 == x or vertical1 == x or vertical2 == x or vertical3 == x or diagonal1 == x or diagonal2 == x: return -10
    elif horizontal1 == o or horizontal2 == o or horizontal3 == o or vertical1 == o or vertical2 == o or vertical3 == o or diagonal1 == o or diagonal2 == o: return 10
    else: return 0



def minimax(bord, depth, is_max):
    score=evaluate(bord)
    if abs(score) == 10: return score
    if not moves_left(bord): return 0
    if is_max:
        best=-1000
        for x in range(3):
            for y in range(3):
                if bord.squares[x][y] == -1:
                    bord.squares[x][y]=1
                    best = max(best, minimax(bord, depth+1, not is_max))-depth
                    bord.squares[x][y]=-1
        return best
    else:
        best=1000
        for x in range(3):
            for y in range(3):
                if bord.squares[x][y] == -1:
                    bord.squares[x][y]=0
                    best=min(best,minimax(bord, depth+1, not is_max))+depth
                    bord.squares[x][y]=-1
        return best

def predict_best_move(bord):
    best_val=-1000
    best_move=(-1,-1)
    for x in range(3):
        for y in range(3):
            if bord.squares[x][y] == -1:
                bord.squares[x][y]=1
                move_val=minimax(bord, 0, False)
                bord.squares[x][y]=-1
                if move_val > best_val:
                    best_val=move_val
                    best_move=(x,y)
    return best_move