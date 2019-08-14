
maze = [
    # j ---->
    [0, -1, -1, -1], #i
    [0, -1, 0, -1], #/
    [0, 0, 0, 0], #/
    [0, -1, 1, 0], #/
    [0, 0, -1, 0], #/
]

width = len(maze[0])
heigth = len(maze)


#altMaze = [[1] * (width + 2)] * (heigth + 2) <- interesting!!
altMaze = [[-1] * (width + 2) for i in range(heigth + 2)]
for i in range(1,heigth+1):
    for j in range(1,width+1):
        altMaze[i][j] = maze[i-1][j-1]

for i in altMaze:
    print(i)

dx = [-1, 0, 1,  0]
dy = [ 0, 1, 0, -1]

def traverse(i, j):
    altMaze[i][j] = 1
    print()
    for k in altMaze:
        print(k)
    for k in range(len(dx)):
        if altMaze[i+dx[k]][j+dy[k]] == 0:
            traverse(i+dx[k], j+dy[k])

traverse(1, 1)
