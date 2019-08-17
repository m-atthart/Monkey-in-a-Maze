import inmaze
from backend import *
import pygame
from pygame.locals import *
import random



def play_easy():
    height = 2 * random.randint(3, 6) + 1
    width = height + 2 * random.randint(2,5)
    inmaze.start_game(height, width)
def play_med():
    height = 2 * random.randint(5,11) + 1
    width = height + 2 * random.randint(2,5)
    inmaze.start_game(height, width)
def play_hard():
    height = 2 * random.randint(10, 15) + 1
    width = height + 2 * random.randint(3,5)
    inmaze.start_game(height, width)
def play_watch_ai():
    height = 2 * random.randint(13, 15) + 1
    width = height + 2 * random.randint(4,6)
    inmaze.start_game(height, width)
def play_race_ai():
    pass
def play_two_player():
    pass
def play_flashlight():
    pass
def play_zen():
    pass
def play_timed():
    pass

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
                play_timed()
            elif event.key == pygame.K_5:
                play_zen()
            elif event.key == pygame.K_6:
                play_flashlight()
            elif event.key == pygame.K_7:
                play_two_player()
            elif event.key == pygame.K_8:
                play_race_ai()
            elif event.key == pygame.K_9:
                play_watch_ai()
            else:
                pass
