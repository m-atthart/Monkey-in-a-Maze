import pygame
from pygame.locals import *
import random

import mazegen


# SETTINGS

# Define colors
CAMBLUE = (163, 193, 173)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (222, 184, 135)
GREEN = (107, 142, 35)
BLUE = (135, 206, 250)
YELLOW = (255, 215, 0)

# grid size
HEIGHT = 2 * random.randint(5,11) + 1
WIDTH = HEIGHT + 2 * random.randint(2,5)

# sets margin
MARGIN = 12

# sides of a grid
CELL_WIDTH = 28
CELL_HEIGHT = 28


def init_window_size(maze, margin, cell_width, cell_height):
    # set Window size
    height = len(maze) * cell_height + 2 * margin
    width = len(maze[0]) * cell_width + 2 * margin
    return width, height


def draw_maze(grid, screen, cell_height, cell_width, margin):
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
        pygame.draw.rect(screen, WHITE,
                         [margin + cell_width * column,
                          margin + cell_height * row,
                          cell_width, cell_height])
        pygame.draw.circle(screen, color, [margin + cell_width * column + cell_width // 2,
                                           margin + cell_height * row + cell_height // 2], cell_height//2)
        pygame.draw.circle(screen, YELLOW, [margin + cell_width * column + cell_width // 2,
                                           margin + cell_height * row + cell_height // 2], cell_height // 4)
        # TODO: fix/decide -- circle vs. elipse

    # fresh canvas
    screen.fill(CAMBLUE)
    # Draw the grid
    # for row in range(34):
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            # set colors for the elements
            # wall = 1
            if grid[row][column] == 1:
                color = CAMBLUE
                draw_wall(row, column, color)
            # player is 2
            elif grid[row][column] == 2:
                color = BROWN
                draw_player(row, column, color)
            # finishing point
            elif grid[row][column] == 3:
                color = BLUE
                draw_finish(row, column, color)
            # what is this?
            elif grid[row][column] == 4:
                color = YELLOW
            else:
                # set default color
                color = WHITE
                draw_void(row, column, color)



maze = mazegen.generate_maze(HEIGHT, WIDTH)
grid = maze

# initialize pygame
pygame.init()
window_size = init_window_size(maze, MARGIN, CELL_WIDTH, CELL_HEIGHT)
screen = pygame.display.set_mode(window_size)

# Set title of screen
pygame.display.set_caption("Monkey in the Maze")

done = False  # close button

clock = pygame.time.Clock()  # how fast the screen takes to update

ccolumn = 0
rrow = 0
grid[rrow][ccolumn] = 2
grid[HEIGHT-1][WIDTH-1] = 3

draw_maze(maze, screen, CELL_HEIGHT, CELL_WIDTH, MARGIN)
pygame.display.update()

# -------- Main Program Loop -----------
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
                # player.move_left()
            elif event.key == pygame.K_RIGHT:
                grid[ccolumn][rrow] = 0
                print("pre " + str(rrow))
                rrow += 1
                grid[ccolumn][rrow] = 2
                print(rrow)
                print("right")
            elif event.key == pygame.K_UP:
                grid[ccolumn][rrow] = 0
                ccolumn -= 1
                grid[ccolumn][rrow] = 2
            elif event.key == pygame.K_DOWN:
                grid[ccolumn][rrow] = 0
                ccolumn += 1
                grid[ccolumn][rrow] = 2
                print("down")

            # Set the screen background
            draw_maze(maze, screen, CELL_HEIGHT, CELL_WIDTH, MARGIN)

            # Limit to 60 frames per second
            #clock.tick(8)

            #pygame.display.flip()
            #screen.blit(screen, (25, 25))
            pygame.display.update()


# exit.
pygame.quit()
