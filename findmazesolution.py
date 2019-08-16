#Code to find the optimum solution against the player
import queue, time
mainq = queue.Queue()
maze=[]
mainq.put("1,1,0")
distance = 0
#function which gets called every time
def checkAdjacent(i, j):
    if i+1 < height and maze[i+1][j] == 0:
        holderstring = str(i+1) + "," + str(j) + "," +str(distance)
        mainq.put(holderstring)
        print(holderstring)
        player.move_down
    if i-1 > -1 and maze[i-1][j] == 0:
        holderstring = str(i-1) + "," + str(j) + "," +str(distance)
        print(holderstring)
        mainq.put(holderstring)
        player.move_up
    if j+1 < width and maze[i][j+1] == 0:
        holderstring = str(i) + "," + str(j+1) + "," +str(distance)
        print(holderstring)
        mainq.put(holderstring)
        player.move_right
    if j-1 > -1 and maze[i][j-1] == 0:
        holderstring = str(i) + "," + str(j-1) + "," +str(distance)
        print(holderstring)
        mainq.put(holderstring)
        player.move_left

holder_removed_from_que = ""
holder_i = 0
holder_j = 0

while True:
        #check if the queue is empty, if it is, there are no solutions anymore, print message
    if holder_i == 0 and holder_j == width:
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
    # check if there are any adjacents
    checkAdjacent(holder_i, holder_j)
