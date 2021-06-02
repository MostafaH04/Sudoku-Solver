import solve

grid = [
    [0,7,0,0,2,0,0,4,6],
    [0,6,0,0,0,0,8,9,0],
    [2,0,0,8,0,0,7,1,5],
    [0,8,4,0,9,7,0,0,0],
    [7,1,0,0,0,0,0,5,9],
    [0,0,0,1,3,0,4,8,0],
    [6,9,7,0,0,2,0,0,8],
    [0,5,8,0,0,0,0,6,0],
    [4,3,0,0,8,0,0,7,0]    
]

solve.show(grid)


continueQ = input("Do you want to make ur own?")
if continueQ.lower() in ['yes','y']:
    for y in range(9):
        for x in range(9):
            grid[y][x] = 0

    for y in range(9):
        for x in range(9):
            while True:
                solve.show(grid)
                inNum = input(f"pick number for ({x},{y})")
                
                try:
                    inNum = int(inNum)
                    if inNum < 10 and inNum >= 0:
                        if solve.possible(y,x, inNum, grid) != True:
                            raise TypeError
                        grid[y][x] = inNum
                    else:
                        raise TypeError
                    
                    break
                
                except:
                    print("Incorrect Format Try Again\n")


solve.solve(grid)