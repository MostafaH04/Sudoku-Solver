gridExample = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]    
]

def show(grid = gridExample):
    prevPosX = -1
    prevPosY = -1
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            posX = int(x/3)
            posY = int(y/3)
            if posY != prevPosY:
                if posY > 0:
                    print("|", end = '')
                print("\n  - - -   - - -   - - -")
            elif x == 0:
                print('|')
            if posX != prevPosX:
                print("| ", end = '')
            if grid[y][x] != 0:
                print(grid[y][x],end = ' ')
            else: print(" ", end = ' ')
            prevPosY, prevPosX = posY, posX
    print('|\n  - - -   - - -   - - -')

def possible(y, x , num, grid = gridExample):
    for i in range(9):
        if grid[y][i] == num:
            return False
        if grid[i][x] == num:
            return False
    startPosX = int(x/3)*3
    startPosY = int(y/3)*3
    for yIter in range(3):
        for xIter in range(3):
            if grid[startPosY+yIter][startPosX+xIter] == num:
                return False 
    return True

def solve(grid = gridExample):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                for i in range(1,10):
                    if possible(y,x,i,grid):
                        grid[y][x] = i
                        solve(grid)
                        grid[y][x] = 0
                return
    show(grid)

solve(gridExample)


