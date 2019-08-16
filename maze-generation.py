#Kruskal's maze generation algorithm

import random

## START CASPAR CODE (MATRIX INIT)

N = 11
M = 11
assert(N % 2 == 1 and M % 2 == 1)
DEBUG_FLAG = False


def printmaze():
    for pm in maze:
        print(pm)
    print("\n")


#generating a random maze n x n with adaptable n
maze = []
height = int(N)
width = int(M)
count = 1

#adding the rows to the bigger list and so to the matrix
for i in range(height):
    row = []
    for j in range(width):
        row.append(count)
        count += 1
    maze.append(row)

if DEBUG_FLAG:
    printmaze()

#first if
#finding the values attached to the indexes with odd numbers in an even row and turning them into a wall by replacing them with a zero
#second if
#finding the values attached to the odd rows and turning them into a wall by replacing them with a zero
#only the values attached to even indexes in both i(vertical) an j(horizontal) direction stay numbered
open_counter=1
for num1 in range(height):
    for num2 in range(width):
        if num1 % 2 == 0 and num2 % 2 == 1:
                maze[num1][num2] = 0
        if num1 % 2 == 1:
            maze[num1][num2] = 0

if DEBUG_FLAG:
    print('matrix init:')
    printmaze()

## END OF MATRIX INIT


##### DEN CODE STARTS
#define random even number generators. these select the first open cell 
#def random_i_generator():
#    random_i=random.randrange(0, height, 2)
#    return(random_i)
#def random_j_generator():
#    random_j=random.randrange(0, width , 2)
#    return(random_j)

di = [-1, 0, 1,  0]
dj = [ 0, 1, 0, -1]

def random_coord(sz):
    return random.randrange(0, sz, 2)

def colorit(maze, i, j, color):
    if DEBUG_FLAG:
        print('colorit')
        printmaze()

    if maze[i][j] != 0:
        maze[i][j] = color
        # color the neighbours
        for idx in range(len(di)):
            ii = i + di[idx]
            jj = j + dj[idx]
            # check are we in the range
            if 0 <= ii < len(maze) and 0 <= jj < len(maze[0]) and maze[ii][jj] != color:
                colorit(maze, ii, jj, color)


def iterate():
    global cnt
    print(cnt)

    # Find random closed cell (wall), which is an odd coordinate pair.
    # Generate a direction to go in
    # I is vertical axis; J is horizontal axis.
    #   direction = 1 is vertical
    #   direction = 0 is horizontal
    random_i = random_coord(height)
    random_j = random_coord(width)

    # random direction
    direction = random.randint(0, 3)

    # shift random_i and random_j to the coordinates of a nearby wall, depending on direction
    if direction == 0: # down
        if random_i + 2 >= height:
            random_i = random_i - 1 # use the wall above if can't go below
        else:
            random_i += 1 # else use the wall below
    elif direction == 1: # right
        if random_j + 2 >= width:
            random_j = random_j - 1 # use the wall left if can't go right
        else: # use right wall
            random_j += 1
    elif direction == 2: # up
        if random_i - 2 < 0:
            random_i = random_i + 1 # use the wall below if can't go above
        else: # use the wall above
            random_i -= 1
    else: # (direction == 3)
        if random_j - 2 < 0:
            random_j = random_j + 1 # use the wall right if can't go left
        else:
            random_j -= 1 # use left wall

    if DEBUG_FLAG:
        print('(random_i, random_j) = (' + str(random_i) + ', ' + str(random_j) + ')')
        print('maze[random_i][random_j] = ' + str(maze[random_i][random_j]))

    # (random_i, random_j) -- the coordinate of the wall under consideration

    # check if the wall has already been opened
    if maze[random_i][random_j] == 0:
        # check if the two cells on vertical are in the same group
        if direction == 0: # down
            if maze[random_i+1][random_j] != maze[random_i-1][random_j]:
                curr_color = maze[random_i-1][random_j]
                maze[random_i][random_j] = curr_color
                cnt += 1
                colorit(maze, random_i+1, random_j, curr_color)
        elif direction == 1: # right
            if maze[random_i][random_j+1] != maze[random_i][random_j-1]:
                curr_color = maze[random_i][random_j-1]
                maze[random_i][random_j] = curr_color
                cnt += 1
                colorit(maze, random_i, random_j+1, curr_color)
        elif direction == 2: # up
            if maze[random_i-1][random_j] != maze[random_i+1][random_j]:
                curr_color = maze[random_i+1][random_j]
                maze[random_i][random_j] = curr_color
                cnt += 1
                colorit(maze, random_i-1, random_j, curr_color)
        else: # (direction == 3) left
            if maze[random_i][random_j-1] != maze[random_i][random_j+1]:
                curr_color = maze[random_i][random_j+1]
                maze[random_i][random_j] = curr_color
                cnt += 1
                colorit(maze, random_i, random_j-1, curr_color)


# MAIN PART
if DEBUG_FLAG:
    printmaze()

cnt = 0
while cnt < (N // 2) * (2 + (M // 2)):
    #print(cnt)
    iterate()

if DEBUG_FLAG or True:
    printmaze()


'''
def countnonzero(mat):
    cc = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] > 0:
                cc += 1
    return cc

print('helou: ' + str(M*N - countnonzero(maze)))
'''