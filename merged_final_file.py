#FINAL MERGED PYTHON FILE
#IMPORTS:
import random, queue, time, pygame
from pygame.locals import *
# initiate required variables
DEBUG_FLAG = False
height=0
width=0

distance=0

#-------------------------------------------------------------------------------------------------------------------------------------


#Firstly, generate the maze! (from mazegen.py)
# implementation of Kruskal's maze generation algorithm
def printmaze(maze):
    for pm in maze:
        print(pm)
    print("\n")

#Initiate the matrix
def init_maze(height, width):
    #generating a random maze n x n with adaptable n
    maze = []
    count = 1
    #add the rows to the bigger list and then to the matrix
    for _ in range(height):
        row = []
        for _ in range(width):
            row.append(count)
            count += 1
        maze.append(row)
    if DEBUG_FLAG:
        printmaze(maze)
    #first if:
    #finds the values attached to the indexes with odd numbers in an even row and turns them into a wall by replacing them with a zero
    #second if:
    #finds the values attached to the odd rows and turns them into a wall by replacing them with a zero
    #only the values attached to even indexes in both i(vertical) and j(horizontal) direction stay numbered
    for num1 in range(height):
        for num2 in range(width):
            if num1 % 2 == 0 and num2 % 2 == 1:
                    maze[num1][num2] = 0
            if num1 % 2 == 1:
                maze[num1][num2] = 0
    #For debug: Print empty initiated matrix
    if DEBUG_FLAG:
        print('matrix init:')
        printmaze(maze)
    return maze

#Define random coordinate generator
def random_coord(sz):
    return random.randrange(0, sz, 2)

#Function that's used to change the merged numbers of two groups to the same number
#Called colorit as colours were used during design for visualisation
def colorit(maze, i, j, color):
    if DEBUG_FLAG:
        print('colorit')
        printmaze(maze)
    #if not wall:
    if maze[i][j] != 0:
        maze[i][j] = color
        # color the neighbours
        di = [-1, 0, 1, 0]
        dj = [0, 1, 0, -1]
        #iterate through the neighbours
        for idx in range(len(di)):
            ii = i + di[idx]
            jj = j + dj[idx]
            # check if in the matrix or out of range
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

    # (random_i, random_j) are now = coordinates of the wall under consideration

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
    
    return 0


def generate_maze(height, width):
    assert (height % 2 == 1 and height % 2 == 1)
    maze = init_maze(height, width)
    cnt = 0
    while cnt < (height // 2) * (2 + (width // 2)):
        cnt += iterate(maze, height, width)
    if DEBUG_FLAG:
        print("GENERATE_MAZE DEBUG:")
        printmaze(maze)

    # normalise (walls = 0)
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] > 0:
                maze[i][j] = 0
            else:
                maze[i][j] = 1


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

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Then, check that the maze can be solved! (from findmazesolution.py)
#Code to find the optimum solution against the player

mainq = queue.Queue()
mainq.put("1,1,0")
#function which gets called every time
def check_iter(i, j, maze):
    print("I="+str(i)+" J="+str(j))
    if i+1 < height and maze[i+1][j] == 0:
        holderstring = str(i+1) + "," + str(j) + "," +str(distance)
        mainq.put(holderstring)
        print(holderstring)
        #player.move_down
    if i-1 > -1 and maze[i-1][j] == 0:
        holderstring = str(i-1) + "," + str(j) + "," +str(distance)
        print(holderstring)
        mainq.put(holderstring)
        #player.move_up
    if j+1 < width and maze[i][j+1] == 0:
        holderstring = str(i) + "," + str(j+1) + "," +str(distance)
        print(holderstring)
        mainq.put(holderstring)
        #player.move_right
    if j-1 > -1 and maze[i][j-1] == 0:
        holderstring = str(i) + "," + str(j-1) + "," +str(distance)
        print(holderstring)
        mainq.put(holderstring)
        #player.move_left

def mainCheck(height, width, maze):
    if DEBUG_FLAG:
        print("Checking maze to ensure it's solveable by the user!")
    holder_removed_from_que = ""
    holder_i = 0
    holder_j = 0
    while True:
        #check if the queue is empty, if it is, there are no solutions anymore, print message
        if holder_i == 1 and holder_j == width-1:
            return(True)

        if mainq.empty():
            return(False)
        
        #split the que into two integers
        holder_removed_from_que = mainq.get()
        str.split(holder_removed_from_que, ",")
        if DEBUG_FLAG:
            print(str(holder_removed_from_que) + " has been removed from queue and will now be checked" )
        holder_i = int(holder_removed_from_que[0])
        holder_j = int(holder_removed_from_que[2])
        distance = int(holder_removed_from_que[4])
        # check if there are any adjacents
        print("\n")
        
        check_iter(holder_i, holder_j, maze)

#------------------------------------------------------------------------------------------------------------------------------------------------
#Initialise the "backend" - this contains all of the classes for the player, coins etc.


class Space:
    def __init__(self, player = False):
        self.isPlayer = player #debugging purposes
    def __repr__(self): #debugging purposes
        if self.isPlayer:
            return "2"
        else:
            return "0"

class Coin(Space):
    def __init__(self, i, j, pickedUp = False):
        self.posI = i #debugging purposes
        self.posJ = j #debugging purposes
        self.isPickedUp = pickedUp
    def __repr__(self): #debugging purposes
        if Player.posI == self.posI and Player.posJ == self.posJ:
            return "2"
        elif not self.isPickedUp:
            return "4"
        else:
            return "0"

class Wall(Space):
    def __repr__(self): #debugging purposes
        return "1"

class Exit(Space):
    def __repr__(self): #debugging purposes
        return "3"

class MazeMap:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.matrix = [[Space() for i in range(width)] for j in range(height)]

    def createWall(self, i, j):
        self.matrix[i][j] = Wall()
    def createCoin(self, i, j):
        self.matrix[i][j] = Coin(i, j)
    def createExit(self, i, j):
        self.matrix[i][j] = Exit(i, j)

    def snapshotMap(self, player): #encodes data for GUI
        dimensions = [[self.height, self.width]]
        playerpos = [[player.posI, player.posJ]]
        exitpos = [[]]
        coins = [[]]
        walls = [[]]
        for i in range(self.height):
            for j in range(self.width):
                if type(self.matrix[i][j]) == Exit:
                    exitpos[0].append(i, j)
                elif type(self.matrix[i][j]) == Wall:
                    walls[0].append([i, j])
                elif type(self.matrix[i][j]) == Coin:
                    if not self.matrix[i][j].isPickedUp:
                        coins[0].append([i, j])
        encoding = dimensions + playerpos + exitpos + walls + coins
        return encoding
    def printMap(self): #debugging purposes
        for i in range(len(self.matrix)):
            print(str(self.matrix[i]) + "\n")
        print("\n")


class Player:
    def __init__(self, posI, posJ, gamemap, topWall = False, rightWall = False, bottomWall = False, leftWall = False, coins = 0, moves = 0):
        self.posI = posI
        self.posJ = posJ
        self.topIsWall = topWall #boolean. if space above is of type wall
        self.rightIsWall = rightWall
        self.bottomIsWall = bottomWall
        self.leftIsWall = leftWall
        self.coinCount = coins #coin counter
        self.moveCount = moves #move counter
        gamemap.matrix[self.posI][self.posJ].isPlayer = True #initializes player on map

    def checkWalls(self, gamemap): #checks spaces around player and changes attributes if needed
        if self.posI > 0 and type(gamemap.matrix[self.posI-1][self.posJ]) == Wall: #checks if top is wall
            self.topIsWall = True
        if self.posJ+1 < gamemap.width and type(gamemap.matrix[self.posI][self.posJ+1]) == Wall:
            self.rightIsWall = True
        if self.posI+1 < gamemap.height and type(gamemap.matrix[self.posI+1][self.posJ]) == Wall:
            self.bottomIsWall = True
        if self.posJ > 0 and type(gamemap.matrix[self.posI][self.posJ-1]) == Wall:
            self.leftIsWall = True
        if self.posI > 0 and type(gamemap.matrix[self.posI-1][self.posJ]) != Wall:
            self.topIsWall = False
        if self.posJ+1 < gamemap.width and type(gamemap.matrix[self.posI][self.posJ+1]) != Wall:
            self.rightIsWall = False
        if self.posI+1 < gamemap.height and type(gamemap.matrix[self.posI+1][self.posJ]) != Wall:
            self.bottomIsWall = False
        if self.posJ > 0 and type(gamemap.matrix[self.posI][self.posJ-1]) != Wall:
            self.leftIsWall = False

    def checkCoin(self, gamemap): #checks if current space is of type coin
        if type(gamemap.matrix[self.posI][self.posJ]) == Coin and not gamemap.matrix[self.posI][self.posJ].isPickedUp:
            self.coinCount += 1
            gamemap.matrix[self.posI][self.posJ].isPickedUp = True

    def move_up(self, gamemap): #moves player up
        self.checkWalls(gamemap)
        if not self.topIsWall:
            gamemap.matrix[self.posI-1][self.posJ].isPlayer = True #debugging purposes
            gamemap.matrix[self.posI][self.posJ].isPlayer = False #debugging purposes
            self.posI -= 1 #updates saved position values
            self.checkCoin(gamemap)
            self.moveCount += 1
        else:
            print("You can't go that way\n")
        print(gamemap.snapshotMap(self)) #debugging purposes
        gamemap.printMap() #debugging purposes
    def move_right(self, gamemap):
        self.checkWalls(gamemap)
        if not self.rightIsWall:
            gamemap.matrix[self.posI][self.posJ+1].isPlayer = True #debugging purposes
            gamemap.matrix[self.posI][self.posJ].isPlayer = False #debugging purposes
            self.posJ += 1
            self.checkCoin(gamemap)
            self.moveCount += 1
        else:
            print("You can't go that way\n")
        print(gamemap.snapshotMap(self)) #debugging purposes
        gamemap.printMap() #debugging purposes
    def move_down(self, gamemap):
        self.checkWalls(gamemap)
        if not self.bottomIsWall:
            gamemap.matrix[self.posI+1][self.posJ].isPlayer = True #debugging purposes
            gamemap.matrix[self.posI][self.posJ].isPlayer = False #debugging purposes
            self.posI += 1
            self.checkCoin(gamemap)
            self.moveCount += 1
        else:
            print("You can't go that way\n")
        print(gamemap.snapshotMap(self)) #debugging purposes
        gamemap.printMap() #debugging purposes
    def move_left(self, gamemap):
        self.checkWalls(gamemap)
        if not self.leftIsWall:
            gamemap.matrix[self.posI][self.posJ-1].isPlayer = True #debugging purposes
            gamemap.matrix[self.posI][self.posJ].isPlayer = False #debugging purposes
            self.posJ -= 1
            self.checkCoin(gamemap)
            self.moveCount += 1
        else:
            print("You can't go that way\n")
        print(gamemap.snapshotMap(self)) #debugging purposes
        gamemap.printMap() #debugging purposes

#------------------------------------------------------------------------------------------------------------------------------------------------
#The actual pygame loop! Merged from inputmaze.py

# SETTINGS

# Define colors
camblue = (163, 193, 173)
black = (0, 0, 0)
white = (255, 255, 255)
brown = (222, 184, 135)
green = (107, 142, 35)
blue = (135, 206, 250)
yellow = (255, 215, 0)

# maze size
#height = 2 * random.randint(5,11) + 1
#width = height + 2 * random.randint(2,5)

# sets margin
margin = -12

# sides of a cell
cell_width = 28
cell_height = 28

def start_game(height, width, mode):
    maze = generate_maze(height, width)
    correct=mainCheck(height, width, maze)
    print(correct)
    if True:
    #if mainCheck(height, width, maze):
        gamemap = MazeMap(len(maze), len(maze[0]))
        for i in range(len(maze)):
            for j in range(len(maze[i])):
                if maze[i][j] == 1:
                    gamemap.createWall(i, j)
                if maze[i][j] == 2:
                    player = Player(i, j)
                    gamemap.matrix[self.posI][self.posJ].isPlayer = True
                if maze[i][j] == 3:
                    gamemap.createExit(i, j)
                if maze[i][j] == 4:
                    gamemap.createCoin(i, j)
    else:
        print("oh no :/ it doesn't work, sorry, you're trapped?")
        #start_game(height, width, mode)
    player = Player(1, 1, gamemap)

    # initialize pygame
    #pygame.init()

    # init screen
    window_size = init_window_size(maze, margin, cell_width, cell_height)
    screen = pygame.display.set_mode(window_size)

    # Set title of screen
    pygame.display.set_caption("Monkey in the Maze")

    # not sure what's this far - not used later
    # TODO: remove?
    clock = pygame.time.Clock()  # how fast the screen takes to update

    inital_grid = get_maze(gamemap, player)
    draw_maze(get_maze(gamemap, player), screen, cell_height, cell_width, margin)
    pygame.display.update()

    done = False
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True # Flag that we are done so we exit this loop
            grid = []
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    done = correctTrue
                elif event.key == pygame.K_LEFT:
                    player.move_left(gamemap)
                    grid = get_maze(gamemap, player)
                elif event.key == pygame.K_RIGHT:
                    player.move_right(gamemap)
                    grid = get_maze(gamemap, player)
                elif event.key == pygame.K_UP:
                    player.move_up(gamemap)
                    grid = get_maze(gamemap, player)
                elif event.key == pygame.K_DOWN:
                    player.move_down(gamemap)
                    grid = get_maze(gamemap, player)
                else:
                    grid = get_maze(gamemap, player)

                # Set the screen background
                draw_maze(grid, screen, cell_height, cell_width, margin)

                # Limit to 60 frames per second
                #clock.tick(8)

                #pygame.display.flip()
                #screen.blit(screen, (25, 25))
                pygame.display.update()


    # exit.
    pygame.quit()

def init_window_size(maze, margin, cell_width, cell_height):
    # set Window size
    height = (len(maze)) * cell_height + 2 * margin
    width = (len(maze[0])) * cell_width + 2 * margin
    return width, height

def draw_maze(maze, screen, cell_height, cell_width, margin):
    def draw_wall(row, column, color):
        pygame.draw.rect(screen, color,
                         [margin + cell_width * column,
                          margin + cell_height * row,
                          cell_width, cell_height])
    def draw_void(row, column, color):
        draw_wall(row, column, color)

    def draw_finish(row, column, color):
        draw_wall(row, column, color)

    def draw_player(row, column, color):
        pygame.draw.rect(screen, white,
                         [margin + cell_width * column,
                          margin + cell_height * row,
                          cell_width, cell_height])
        pygame.draw.circle(screen, color, [margin + cell_width * column + cell_width // 2,
                                           margin + cell_height * row + cell_height // 2], cell_height//2)
        pygame.draw.circle(screen, yellow, [margin + cell_width * column + cell_width // 2,
                                           margin + cell_height * row + cell_height // 2], cell_height // 4)
        # TODO: fix/decide -- circle vs. elipse

    # fresh canvas
    screen.fill(camblue)
    # Draw the maze
    # for row in range(34):
    for row in range(len(maze)):
        for column in range(len(maze[0])):
            # set colors for the elements
            # wall = 1
            if maze[row][column] == 1:
                color = camblue
                draw_wall(row, column, color)
            # player is 2
            elif maze[row][column] == 2:
                color = brown
                draw_player(row, column, color)
            # finishing point
            elif maze[row][column] == 3:
                color = blue
                draw_finish(row, column, color)
            # what is this?
            elif maze[row][column] == 4:
                color = yellow
            else:
                # set default color
                color = white
                draw_void(row, column, color)


def get_maze(gamemap, player):
    encoding = gamemap.snapshotMap(player)
    maze_height = encoding[0][0]
    maze_width = encoding[0][1]
    matrix = [[0 for j in range(maze_width)] for i in range(maze_height)]
    player_pos = encoding[1]
    matrix[player_pos[0]][player_pos[1]] = 2
    #exit_pos = encoding[2]
    #matrix[exit_pos[0]][exit_pos[1]] = 3
    for i in range(len(encoding[3])):
        wall = encoding[3][i]
        matrix[wall[0]][wall[1]] = 1
    for i in range(len(encoding[4])):
        coin = encoding[4][i]
        matrix[coin[0]][coin[1]] = 4
    return matrix


print("Starting game! \n")
start_game(23, 23, 1)