matrix = [];
size = 5;
for i in range(size):
    matrix.append(list(map(int, input().split())))

def matrixRun(x, y):
    if (matrix[x][y] == 1 or matrix[x][y] == -1 or
        x == size or y == size):
        return
    else:
        matrix[x][y] = -1;
        moveLeft(x,y);
        moveRight(x, y);
        moveTop(x,y);
        moveBottom(x,y);

def moveLeft(prevX, prevY):
    if (prevY - 1 >= 0):
        matrixRun(prevX, prevY-1);
             
def moveRight(prevX, prevY):
    if (prevY + 1 < size):
        matrixRun(prevX, prevY+1);
    return;
            
def moveTop(prevX, prevY):
    if (prevX - 1  >= 0):
        matrixRun(prevX-1, prevY);
    return;
            
def moveBottom(prevX, prevY):
    if (prevX + 1 < size):
        matrixRun(prevX+1, prevY);
    return;
    
matrixRun(0, 0)
robbersWin = matrix[4][4] != -1
if (robbersWin):
    print('ROBBERS')
else:
    print('COPS')
