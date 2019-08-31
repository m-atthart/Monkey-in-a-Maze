import pygame
from pygame.locals import *
import random

import mazedoer
import mazegen
from backend import *

# SETTINGS

# Define colours
camblue = (163, 193, 173)
black = (0, 0, 0)
white = (255, 255, 255)
brown = (222, 184, 135)
green = (107, 142, 35)
blue = (135, 206, 250)
yellow = (255, 215, 0)
neon = (180, 250, 45)
magenta = (230, 5, 235)

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
                playercomp = Player(i, j, gamemap)
            if maze[i][j] == 3:
                gamemap.createExit(i, j)
            if maze[i][j] == 4:
                gamemap.createCoin(i, j)


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

    draw_maze(get_maze(gamemap, player, player2, playercomp), screen, cell_height, cell_width, margin)
    pygame.display.update()

    if global_mode == 6:
        done = False
        while not done:
            if global_mode == 8:
                solution = mazedoer.ai_solve(maze)
                for move in solution:
                    pygame.time.wait(1000)
                    if move == "right":
                        playercomp.move_right(gamemap)
                    elif move == "down":
                        playercomp.move_down(gamemap)
                    elif move == "up":
                        playercomp.move_up(gamemap)
                    elif move == "left":
                        playercomp.move_left(gamemap)

                    if gamemap.matrix[-2][-2].isPlayer == True: # if user gets to end
                        done = True

                    draw_maze(get_maze(gamemap, player, player2, playercomp), screen, cell_height, cell_width, margin)
                    pygame.display.update()

    done = False
    move2 = -1
    solution = mazedoer.ai_solve(maze)
    while not done:
        if global_mode == 8:
            if move2 >= 0:
                direction = solution[move2]
                if direction == "right":
                    playercomp.move_right(gamemap)
                elif direction == "down":
                    playercomp.move_down(gamemap)
                elif direction == "up":
                    playercomp.move_up(gamemap)
                elif direction == "left":
                    playercomp.move_left(gamemap)
            draw_maze(get_maze(gamemap, player, player2, playercomp), screen, cell_height, cell_width, margin)
            pygame.display.update()
            if move2 < len(solution) - 1:
                move2 += 1
            pygame.time.wait(200)
            if gamemap.matrix[-2][-2].isPlayer == True: # if user gets to end
                done = True
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True # Flag that we are done so we exit this loop
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    done = True
                if event.key == pygame.K_LEFT:
                    player.move_left(gamemap)
                if event.key == pygame.K_RIGHT:
                    player.move_right(gamemap)
                if event.key == pygame.K_UP:
                    player.move_up(gamemap)
                if event.key == pygame.K_DOWN:
                    player.move_down(gamemap)

                if global_mode == 5:
                    if event.key == pygame.K_w:
                        player2.move_up(gamemap)
                    if event.key == pygame.K_a:
                        player2.move_left(gamemap)
                    if event.key == pygame.K_s:
                        player2.move_down(gamemap)
                    if event.key == pygame.K_d:
                        player2.move_right(gamemap)



                if gamemap.matrix[-2][-2].isPlayer == True: # if user gets to end
                    done = True

                # Set the screen background
                draw_maze(get_maze(gamemap, player, player2, playercomp), screen, cell_height, cell_width, margin)
                pygame.display.update()

    pygame.quit()

def init_window_size(maze, margin, cell_width, cell_height):
    # set Window size
    height = (len(maze)) * cell_height + 2 * margin
    width = (len(maze[0])) * cell_width + 2 * margin
    return width, height

def draw_maze(maze, screen, cell_height, cell_width, margin):
    def draw_wall(row, column, colour):
        pygame.draw.rect(screen, colour,
                         [margin + cell_width * column,
                          margin + cell_height * row,
                          cell_width, cell_height])
    def draw_void(row, column, colour):
        draw_wall(row, column, colour)

    def draw_finish(row, column, colour):
        draw_wall(row, column, colour)

    def draw_player(row, column, colour):
        pygame.draw.rect(screen, white,
                         [margin + cell_width * column,
                          margin + cell_height * row,
                          cell_width, cell_height])
        pygame.draw.circle(screen, colour, [margin + cell_width * column + cell_width // 2,
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
            # set colours for the elements:
            if maze[row][column] == 1: # wall
                colour = camblue
                draw_wall(row, column, colour)
            elif global_mode != 8 and maze[row][column] == 2: # player
                colour = brown
                draw_player(row, column, colour)
            elif maze[row][column] == 3: # exit
                colour = neon
                draw_finish(row, column, colour)
            elif maze[row][column] == 4: # coin
                colour = yellow
            elif global_mode == 2 and maze[row][column] == 5: # player 2
                colour = black
                draw_player(row, column, colour)
            elif global_mode == 7 and maze[row][column] == 6: # ai player
                colour = magenta
                draw_player(row, column, colour)
            elif global_mode == 8 and maze[row][column] == 6:
                colour = magenta
                draw_player(row, column, colour)
            else: # default colour
                colour = white
                draw_void(row, column, colour)


def get_maze(gamemap, player, player2, playercomp):
    encoding = gamemap.snapshotMap(player, player2, playercomp)
    maze_height = encoding[0][0]
    maze_width = encoding[0][1]
    matrix = [[0 for j in range(maze_width)] for i in range(maze_height)]
    if global_mode == 2:
        playercomp_pos = encoding[6]
        matrix[playercomp_pos[0]][playercomp_pos[1]] = 6
        player2_pos = encoding[2]
        matrix[player2_pos[0]][player2_pos[1]] = 5
    elif global_mode == 7 or global_mode == 8:
        player2_pos = encoding[2]
        matrix[player2_pos[0]][player2_pos[1]] = 5
        playercomp_pos = encoding[6]
        matrix[playercomp_pos[0]][playercomp_pos[1]] = 6
    if global_mode != 8:
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
