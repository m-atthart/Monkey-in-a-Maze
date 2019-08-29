import pygame
from pygame.locals import *
import random

import mazedoer
import mazegen
from backend import *

# SETTINGS

# Define colors
camblue = (163, 193, 173)
black = (0, 0, 0)
white = (255, 255, 255)
brown = (222, 184, 135)
green = (107, 142, 35)
blue = (135, 206, 250)
yellow = (255, 215, 0)
neon = (180, 250, 45)

# maze size
#height = 2 * random.randint(5,11) + 1
#width = height + 2 * random.randint(2,5)

# sets margin
margin = -12

# sides of a cell
cell_width = 28
cell_height = 28

global_mode = None

def start_game(height, width, mode):
    global global_mode
    global_mode = mode
    solvable_maze = False
    while not solvable_maze:
        maze = mazegen.generate_maze(height, width)
        try:
            mazedoer.solve_maze(maze)
            solvable_maze = True
        except (KeyError, TypeError):
            pass
    gamemap = Map(len(maze), len(maze[0]))
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 1:
                gamemap.createWall(i, j)
            if maze[i][j] == 2:
                player = Player(i, j, gamemap)
                gamemap.matrix[i][j].isPlayer = True
                player2 = Player(i, j, gamemap)
                gamemap.matrix[i][j].isPlayer = True
            if maze[i][j] == 3:
                gamemap.createExit(i, j)
            if maze[i][j] == 4:
                gamemap.createCoin(i, j)
    #player = Player(1, 1, gamemap)

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

    draw_maze(get_maze(gamemap, player, player2), screen, cell_height, cell_width, margin)
    pygame.display.update()

    done = False
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True # Flag that we are done so we exit this loop
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    done = True
                elif event.key == pygame.K_LEFT:
                    player.move_left(gamemap)
                elif event.key == pygame.K_RIGHT:
                    player.move_right(gamemap)
                elif event.key == pygame.K_UP:
                    player.move_up(gamemap)
                elif event.key == pygame.K_DOWN:
                    player.move_down(gamemap)

                elif event.key == pygame.K_w:
                    player2.move_up(gamemap)
                elif event.key == pygame.K_a:
                    player2.move_left(gamemap)
                elif event.key == pygame.K_s:
                    player2.move_down(gamemap)
                elif event.key == pygame.K_d:
                    player2.move_right(gamemap)

                if gamemap.matrix[-2][-2].isPlayer == True: # if user gets to end
                    done = True

                # Set the screen background
                draw_maze(get_maze(gamemap, player, player2), screen, cell_height, cell_width, margin)

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
        for column in range(len(maze[row])):
            # set colors for the elements:
            # wall
            if maze[row][column] == 1:
                color = camblue
                draw_wall(row, column, color)
            # player
            elif maze[row][column] == 2:
                color = brown
                draw_player(row, column, color)
            # exit
            elif maze[row][column] == 3:
                color = neon
                draw_finish(row, column, color)
            # coin
            elif maze[row][column] == 4:
                color = yellow
            # player2
            elif global_mode == 2 and maze[row][column] == 5:
                #print("printing p2")
                color = black
                draw_player(row, column, color)
            else:
                # set default color
                color = white
                draw_void(row, column, color)


def get_maze(gamemap, player, player2):
    encoding = gamemap.snapshotMap(player, player2)
    maze_height = encoding[0][0]
    maze_width = encoding[0][1]
    matrix = [[0 for j in range(maze_width)] for i in range(maze_height)]
    player2_pos = encoding[2]
    matrix[player2_pos[0]][player2_pos[1]] = 5
    player_pos = encoding[1]
    matrix[player_pos[0]][player_pos[1]] = 2
    exit_pos = encoding[3][0]
    matrix[exit_pos[0]][exit_pos[1]] = 3
    for i in range(len(encoding[4])):
        wall = encoding[4][i]
        matrix[wall[0]][wall[1]] = 1
    for i in range(len(encoding[5])):
        coin = encoding[5][i]
        matrix[coin[0]][coin[1]] = 4
    return matrix
