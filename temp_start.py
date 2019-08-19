import inmaze
from backend import *
import pygame
from pygame.locals import *
import random
from findmazesolution import * 

height_easy = 2 * random.randint(3, 6) + 1
width_easy = height_easy + 2 * random.randint(2,5)
height_med = 2 * random.randint(5,11) + 1
width_med = height_med + 2 * random.randint(2,5)
height_hard = 2 * random.randint(10, 15) + 1
width_hard = height_hard + 2 * random.randint(3,5)
height_ai = 2 * random.randint(13, 15) + 1
width_ai = height_ai + 2 * random.randint(4,6)

inmaze.start_game(height_hard, width_hard, 1)
