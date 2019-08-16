# Array-Backed Grids_Test

from backend import *
import pygame
from pygame.locals import *
import numpy as np

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
brown = (222, 184, 135)
green = (107, 142, 35)
blue = (135, 206, 250)
yellow = (255, 215, 0)


# sides of a grid
width = 40
height = 40

x, y = 21, 34

# set Window size
WINDOW_SIZE = [315, 510]  # (width,height)
screen = pygame.display.set_mode(WINDOW_SIZE)

# initialize pygame
pygame.init()

# Set title of screen
pygame.display.set_caption("Monkey in the Maze")

done = False  # close button

clock = pygame.time.Clock()  # how fast the screen takes to update

# -------- Main Program Loop -----------

def draw_maze():
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

    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        done = True

    if keys[K_LEFT]:
        player.move_left()
        draw_maze()
        #pygame.display.flip()
    elif keys[K_RIGHT]:
        player.move_right()
        draw_maze()
        #pygame.display.flip()
    elif keys[K_UP]:
        player.move_up()
        draw_maze()
        #pygame.display.flip()
    elif keys[K_DOWN]:
        player.move_down()
        draw_maze()
        #pygame.display.flip()

    # Set the screen background
    screen.fill(white)

    # Draw the grid

    #new way to make maze
    # for row in range(34):
    maze = draw_maze()
    for row in range(len(maze)):
        for column in range(len(maze[0])):
            # for column in range(21):
            color = white
            # set colors for the elements
            # wall = 1
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
