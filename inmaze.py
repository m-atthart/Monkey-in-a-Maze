import pygame
from pygame.locals import *
import random

import mazegen
from backend import *
import findmazesolution

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
    maze = mazegen.generate_maze(height, width)
    if findmazesolution.mainCheck(height, width):
        maze = maze
        for i in range(len(maze)):
            for j in range(len(maze[i])):
                if maze[i][j] == 1:
                    maze.createWall(i, j)
                if maze[i][j] == 2:
                    player = Player(i, j)
                    maze.matrix[self.posI][self.posJ].isPlayer = True
                if maze[i][j] == 3:
                    maze.createExit(i, j)
                if maze[i][j] == 4:
                    maze.createCoin(i, j)
    else:
        start_game(height, width, mode)
    player = Player(1, 1, maze)

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

    inital_grid = get_maze(maze, player)
    draw_maze(get_maze(maze, player), screen, cell_height, cell_width, margin)
    pygame.display.update()

    done = False
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True # Flag that we are done so we exit this loop
            grid = []
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    done = True
                elif event.key == pygame.K_LEFT:
                    player.move_left(maze)
                    grid = get_maze(maze, player)
                elif event.key == pygame.K_RIGHT:
                    player.move_right(maze)
                    grid = get_maze(maze, player)
                elif event.key == pygame.K_UP:
                    player.move_up(maze)
                    grid = get_maze(maze, player)
                elif event.key == pygame.K_DOWN:
                    player.move_down(maze)
                    grid = get_maze(maze, player)
                else:
                    grid = get_maze(maze, player)

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


def get_maze(maze, player):
    encoding = maze.snapshotMap(player)
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


# -------- Main Program Loop -----------

# init map
'''
maze = mazegen.generate_maze(height, width)
maze = Map(len(maze), len(maze[0]))
for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == 1:
            maze.createWall(i, j)
        if maze[i][j] == 2:
            player = Player(i, j)
            maze.matrix[self.posI][self.posJ].isPlayer = True
        if maze[i][j] == 3:
            maze.createExit(i, j)
        if maze[i][j] == 4:
            maze.createCoin(i, j)
player = Player(1, 1, maze)
'''
'''
game_map = [[1] * (width+2) for i in range(height+2)]
for i in range(1,height+1):
    for j in range(1,width+1):
        game_map[i][j] = maze[i-1][j-1]

for x in game_map:
    print(x)

player_i = 1
player_j = 1
game_map[player_i][player_j] = 2
print('ss')
for x in game_map:
    print(x)
print('ss')

def move_up(game_map):
    global player_i, player_j
    if game_map[player_i-1][player_j] == 0:
        game_map[player_i][player_j] = 0
        player_i -= 1
        game_map[player_i][player_j] = 2

def move_down(game_map):
    global player_i, player_j
    if game_map[player_i+1][player_j] == 0:
        game_map[player_i][player_j] = 0
        player_i += 1
        game_map[player_i][player_j] = 2

def move_left(game_map):
    global player_i, player_j
    if game_map[player_i][player_j-1] == 0:
        game_map[player_i][player_j] = 0
        player_j -= 1
        game_map[player_i][player_j] = 2


def move_right(game_map):
    global player_i, player_j
    if game_map[player_i][player_j+1] == 0:
        game_map[player_i][player_j] = 0
        player_j += 1
        game_map[player_i][player_j] = 2
'''
'''
# initialize pygame
pygame.init()

# init screen
window_size = init_window_size(maze, margin, cell_width, cell_height)
screen = pygame.display.set_mode(window_size)

# Set title of screen
pygame.display.set_caption("Monkey in the Maze")

# not sure what's this far - not used later
# TODO: remove?
clock = pygame.time.Clock()  # how fast the screen takes to update

inital_grid = get_maze(maze, player)
draw_maze(get_maze(maze, player), screen, cell_height, cell_width, margin)
pygame.display.update()

done = False
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True # Flag that we are done so we exit this loop
        grid = []
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_LEFT:
                player.move_left(maze)
                grid = get_maze(maze, player)
            elif event.key == pygame.K_RIGHT:
                player.move_right(maze)
                grid = get_maze(maze, player)
            elif event.key == pygame.K_UP:
                player.move_up(maze)
                grid = get_maze(maze, player)
            elif event.key == pygame.K_DOWN:
                player.move_down(maze)
                grid = get_maze(maze, player)
            else:
                grid = get_maze(maze, player)

            # Set the screen background
            draw_maze(grid, screen, cell_height, cell_width, margin)

            # Limit to 60 frames per second
            #clock.tick(8)

            #pygame.display.flip()
            #screen.blit(screen, (25, 25))
            pygame.display.update()


# exit.
pygame.quit()
'''
