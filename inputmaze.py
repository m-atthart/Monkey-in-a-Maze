# Array-Backed Grids_Test

import backend
import pygame
from pygame.locals import *
import random
import mazegen


# Define colors
CAMBLUE = (163, 193, 173)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (222, 184, 135)
GREEN = (107, 142, 35)
BLUE = (135, 206, 250)
YELLOW = (255, 215, 0)

# grid size
HEIGHT = 2 * random.randint(3,9) + 1
WIDTH = HEIGHT + 2 * random.randint(1,3)

# sets margin
margin = 12

# sides of a grid
width = 28
height = 28


def init_window_size(maze, margin, cell_width, cell_height):
    # set Window size
    height = len(maze) * cell_height + 2 * margin
    width = len(maze[0]) * cell_width + 2 * margin
    return width, height

def draw_maze(grid, screen, cell_height, cell_width, margin):
    # fresh canvas
    screen.fill(camblue)
    # Draw the grid
    # for row in range(34):
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            # set colors for the elements
            # wall = 1
            if grid[row][column] == 1:
                color = camblue
            # character is 2
            elif grid[row][column] == 2:
                color = GREEN
            # finishing point
            elif grid[row][column] == 3:
                color = BLUE
            # what is this?
            elif grid[row][column] == 4:
                color = YELLOW
            else:
                # set default color
                color = WHITE
            pygame.draw.rect(screen, color,
                             [margin + cell_width * column,
                              margin + cell_height * row,
                              cell_width, cell_height])

maze = mazegen.generate_maze(HEIGHT, WIDTH)

# initialize pygame
pygame.init()
window_size = init_window_size(maze, MARGIN, CELL_WIDTH, CELL_HEIGHT)
screen = pygame.display.set_mode(window_size)

# Set title of screen
pygame.display.set_caption("Monkey in the Maze")

done = False  # close button

clock = pygame.time.Clock()  # how fast the screen takes to update

# -------- Main Program Loop -----------

def get_maze():
    encoding = game_map.snapshotMap()
    maze_height = encoding[0][0]
    maze_width = encoding[0][1]
    matrix = [[0 for j in range(maze_width)] for i in range(maze_height)]
    player_pos = encoding[1]
    matrix[player_pos[0]][player_pos[1]] = 2
    for i in range(len(encoding[3])):
        wall = encoding[3][i]
        matrix[wall[0]][wall[1]] = 1
    for i in range(len(encoding[2])):
        coin = encoding[2][i]
        matrix[coin[0]][coin[1]] = 4
    return matrix

while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True # Flag that we are done so we exit this loop

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_ESCAPE:
            done = True
        elif event.key == pygame.K_LEFT:
            grid[ccolumn][rrow] = 0
            rrow -= 1
            grid[ccolumn][rrow] = 2

            player.move_left()
            get_maze()
        elif event.key == pygame.K_RIGHT:
            grid[ccolumn][rrow] = 0
            print("pre " + str(rrow))
            rrow += 1
            grid[ccolumn][rrow] = 2
            print(rrow)

            player.move_right()
            get_maze()
        elif event.key == pygame.K_UP:
            grid[ccolumn][rrow] = 0
            ccolumn -= 1
            grid[ccolumn][rrow] = 2

            player.move_up()
            get_maze()
        elif event.key == pygame.K_DOWN:
            grid[ccolumn][rrow] = 0
            ccolumn += 1
            grid[ccolumn][rrow] = 2
            print("down")

            player.move_down()
            get_maze()

    # Set the screen background
    screen.fill(white)

    # Draw the grid

    #new way to make maze
    # for row in range(34):
    maze = get_maze()
    for row in range(len(maze)):
        for column in range(len(maze[0])):
            # for column in range(21):
            color = white
            # set colors for the elements
            # wall = 1
            if grid[row][column] == 1:
                color = brown
            # character is 2
            if grid[row][column] == 2:
                color = green
            # finishing point
            if grid[row][column] == 3:
                color = blue
            if grid[row][column] == 4:
                color = yellow

            pygame.draw.rect(screen, color,
                             [300/len(maze) * column, 300/len(maze[0]) * row, 300/len(maze), 300/len(maze[0])])



    # Limit to 60 frames per second
    clock.tick(10)

    pygame.display.flip()
    #screen.blit(screen, (25, 25))
    pygame.display.update()


    if maze[row][column] == 1:
        color = brown
    # character is 2
    if maze[row][column] == 2:
        color = green
    # finishing point
    if maze[row][column] == 3:
        color = blue
    if maze[row][column] == 4:
        color = yellow

    pygame.draw.rect(screen, color,
                             [300/len(maze) * column, 300/len(maze[0]) * row, 300/len(maze), 300/len(maze[0])])

    # Limit to 10 frames per second
    clock.tick(10)

    pygame.display.flip()
    pygame.display.update()

# exit.
pygame.quit()
