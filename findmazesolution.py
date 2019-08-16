#matrix trial
import queue
mainq = queue.Queue()
mainq.put("1,1,0")
#maze in form of a matrix
maze = [
    # j ---->
    [0, 1, 1, 1], #i
    [0, 1, 0, 1], #/
    [0, 0, 0, 0], #/
    [0, 1, 1, 0], #/
    [0, 0, 1, 0], #/
]
width = len(maze[0])
height = len(maze)
distance = 0

altMaze = [[-1] * (width + 2) for i in range(height + 2)]
for i in range(1,height+1):
    for j in range(1,width+1):
        altMaze[i][j] = maze[i-1][j-1]

maze = altMaze
width = len(maze[0])
height = len(maze)
distance = 0



#function which gets called every time
def checkAdjacent(i, j):
    if i+1 < height and maze[i+1][j] == 0:
        holderstring = str(i+1) + "," + str(j) + "," +str(distance)
        mainq.put(holderstring)
        print(holderstring)
    if i-1 > -1 and maze[i-1][j] == 0:
        holderstring = str(i-1) + "," + str(j) + "," +str(distance)
        print(holderstring)
        mainq.put(holderstring)
    if j+1 < width and maze[i][j+1] == 0:
        holderstring = str(i) + "," + str(j+1) + "," +str(distance)
        print(holderstring)
        mainq.put(holderstring)
    if j-1 > -1 and maze[i][j-1] == 0:
        holderstring = str(i) + "," + str(j-1) + "," +str(distance)
        print(holderstring)
        mainq.put(holderstring)

holder_removed_from_que = ""
holder_i = 0
holder_j = 0

while True:
        #check if the queue is empty, if it is, there are no solutions anymore, print message
    if holder_i == 5 and holder_j == 4:
        solution = True
        print("The solution is found!")
        break

    if mainq.empty():
        print("There is no solution")
        break
    #split the que into two integers
    holder_removed_from_que = mainq.get()
    str.split(holder_removed_from_que, ",")
    print(holder_removed_from_que)
    holder_i = int(holder_removed_from_que[0])
    holder_j = int(holder_removed_from_que[2])
    distance = int(holder_removed_from_que[4])



    distance += 1
    # check if there are any adjacents
    checkAdjacent(holder_i, holder_j)

    #now set it back to a wall if it's passed
    maze[holder_i][holder_j] = distance

for t in maze:
    print(t)
