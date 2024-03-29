# implementation of Kruskal's maze generation algorithm

import random


# global definitions
DEBUG_FLAG = False


def printmaze(maze):
    for pm in maze:
        print(pm)
    print("\n")


## START CASPAR CODE (MATRIX INIT)
def init_maze(height, width):
    #generating a random maze n x n with adaptable n
    maze = []

    count = 1
    #adding the rows to the bigger list and so to the matrix
    for i in range(height):
        row = []
        for j in range(width):
            row.append(count)
            count += 1
        maze.append(row)

    if DEBUG_FLAG:
        printmaze(maze)

    #first if
    #finding the values attached to the indexes with odd numbers in an even row and turning them into a wall by replacing them with a zero
    #second if
    #finding the values attached to the odd rows and turning them into a wall by replacing them with a zero
    #only the values attached to even indexes in both i(vertical) an j(horizontal) direction stay numbered
    #open_counter = 1
    for num1 in range(height):
        for num2 in range(width):
            if num1 % 2 == 0 and num2 % 2 == 1:
                    maze[num1][num2] = 0
            if num1 % 2 == 1:
                maze[num1][num2] = 0

    if DEBUG_FLAG:
        print('matrix init:')
        printmaze(maze)

    return maze
#Code to add a series of 0s in a wall around the maze if required
'''
#add a block of walls around the maze
altMaze = [[0] * (width + 2) for i in range(height + 2)]
for i in range(1,height+1):
    for j in range(1,width+1):
        altMaze[i][j] = maze[i-1][j-1]

maze = altMaze
width = len(maze[0])
height = len(maze)
distance = 0 '''
## END OF MATRIX INIT


def random_coord(sz):
    return random.randrange(0, sz, 2)


def colorit(maze, i, j, color):
    if DEBUG_FLAG:
        print('colorit')
        printmaze(maze)

    if maze[i][j] != 0:
        maze[i][j] = color
        # color the neighbours
        di = [-1, 0, 1, 0]
        dj = [0, 1, 0, -1]
        for idx in range(len(di)):
            ii = i + di[idx]
            jj = j + dj[idx]
            # check are we in the range
            if 0 <= ii < len(maze) and 0 <= jj < len(maze[0]) and maze[ii][jj] != color:
                colorit(maze, ii, jj, color)


def iterate(maze, height, width):
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
                colorit(maze, random_i+1, random_j, curr_color)
                return 1
        elif direction == 1: # right
            if maze[random_i][random_j+1] != maze[random_i][random_j-1]:
                curr_color = maze[random_i][random_j-1]
                maze[random_i][random_j] = curr_color
                colorit(maze, random_i, random_j+1, curr_color)
                return 1
        elif direction == 2: # up
            if maze[random_i-1][random_j] != maze[random_i+1][random_j]:
                curr_color = maze[random_i+1][random_j]
                maze[random_i][random_j] = curr_color
                colorit(maze, random_i-1, random_j, curr_color)
                return 1
        else: # (direction == 3) left
            if maze[random_i][random_j-1] != maze[random_i][random_j+1]:
                curr_color = maze[random_i][random_j+1]
                maze[random_i][random_j] = curr_color
                colorit(maze, random_i, random_j-1, curr_color)
                return 1
    # !
    return 0


def generate_maze(height, width):
    assert (N % 2 == 1 and M % 2 == 1)
    maze = init_maze(height, width)
    cnt = 0
    while cnt < (height // 2) * (2 + (width // 2)):
        cnt += iterate(maze, height, width)
    if DEBUG_FLAG:
        printmaze(maze)

    # normalise (walls = 0)
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] > 0:
                maze[i][j] = 0
            else:
                maze[i][j] = 1


    # add exit
    maze[-1][-1] = 3
    maze[0][0] = 2

    # add walls around maze
    for i in range(len(maze)):
        last_value = maze[i][-1]
        for j in range(len(maze[i])):
            if j+1 == len(maze[i]):
                maze[i][0] = 1
            else:
                maze[i][-(j+1)] = maze[i][-(j+2)]
        maze[i].append(last_value)
        maze[i].append(1)
    width += 2


    last_row = maze[-1]
    for i in range(len(maze)):
        if i+1 == len(maze):
            maze[0] = [1] * width
        else:
            maze[-(i+1)] = maze[-(i+2)]
    maze.append(last_row)
    maze.append([1] * width)
    height += 2
    return maze


# MAIN PART
N = 11
M = 11
res = generate_maze(N, M)
#printmaze(res)
