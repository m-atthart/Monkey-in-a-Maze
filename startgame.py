import inmaze
from backend import *
import pygame
from pygame.locals import *
import random


height_easy = 2 * random.randint(3, 6) + 1
width_easy = height_easy + 2 * random.randint(2,5)
height_med = 2 * random.randint(5,11) + 1
width_med = height_med + 2 * random.randint(2,5)
height_hard = 2 * random.randint(10, 15) + 1
width_hard = height_hard + 2 * random.randint(3,5)
height_ai = 2 * random.randint(13, 15) + 1
width_ai = height_ai + 2 * random.randint(4,6)


'''
mode:
1-singleplayer
2-multiplayer
3-zen
4-flashlight
5-flawless
6-nostop
7-race
8-watch
'''


def play_easy():
    inmaze.start_game(height_easy, width_easy, 1)
    #mode1
def play_med():
    inmaze.start_game(height_med, width_med, 1)
    #mode1
def play_hard():
    inmaze.start_game(height_hard, width_hard, 1)
    #mode1
def play_watch_ai():
    inmaze.start_game(height_ai, width_ai, 8)
    #mode8. make playercomp=Player(). make findmazesolution moves trigger playercomp.move_direction()
def play_race_ai():
    pass
    #mode7. make playercomp. don't make player. pass pauser=false to findmazesolution func. if mode == 4, pauser=true -> when ai finds solution, pause for .75 sec between performing moves
def play_two_player():
    pass
    #mode2. make player2=Player(). add ifs for wasd for player2.move_direction()
def play_flashlight():
    pass
    #mode4. in drawmaze, pass position values. if position, add pos+-4 to if for spaces to get coloured. else, colour black
def play_zen():
    pass
    #mode3. pass coin=true value to generatemap. if false, generatemap without making spaces = coin. or generatemap, then change all coins to spaces before backend turns them into Coins
def play_flawless():
    pass
    #mode5. after each move, make [i][j]-1 = Wall
def play_dont_stop():
    pass
    #mode6. main game loop. start timer. if timer >= 2 sec, done = true

pygame.init()

done = False
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True # Flag that we are done so we exit this loop
        grid = []
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_1:
                play_easy()
            elif event.key == pygame.K_2:
                play_med()
            elif event.key == pygame.K_3:
                play_hard()
            elif event.key == pygame.K_4:
                play_zen()
            elif event.key == pygame.K_5:
                play_flashlight()
            elif event.key == pygame.K_6:
                play_flawless()
            elif event.key == pygame.K_7:
                play_dont_stop()
            elif event.key == pygame.K_8:
                play_two_player()
            elif event.key == pygame.K_9:
                play_race_ai()
            elif event.key == pygame.K_0:
                play_watch_ai()
            else:
                pass
