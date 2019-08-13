import time
import asyncio


class Space:
    def __init__(self, pos = False, wall = False, coin = False):
        self.pos = pos #matrix[i][j]
        self.isWall = wall
        self.isCoin = coin

    def __repr__(self):
        if self.isWall:
            return "x"
        elif self.isCoin:
            return "c"
        #elif player.pos == self.pos:
            #return "P"
        else:
            return "-"


class Player:
    def __init__(self, pos, topWall, rightWall, bottomWall, leftWall):
        self.pos = pos
        self.topIsWall = topWall
        self.rightIsWall = rightWall
        self.bottomIsWall = bottomWall
        self.leftIsWall = leftWall

    def checkWalls(self, pos):
        if matrix[i-1][j].isWall: #checks if top is wall
            self.topIsWall = True
        if matrix[i][j+1].isWall: #checks if right is wall
            self.rightIsWall = True
        if matrix[i+1][j].isWall:
            self.bottomIsWall = True
        if matrix[i][j-1].isWall:
            self.leftIsWall = True

    def move_up(self, space):
        if not self.topIsWall:
            self.pos = matrix[i-1][j]
            matrix[i][j] = "-" #replace old spot with empty spot
            game_map.refreshMap
        else:
            print("you can't go that way")
    def move_right(self, space):
        if not self.rightIsWall:
            self.pos = matrix[i][j+1]
            matrix[i][j] = "-" #replace old spot with empty spot
            game_map.refreshMap
        else:
            print("you can't go that way")
    def move_down(self, space):
        if not self.bottomIsWall:
            self.pos = matrix[i+1][j]
            matrix[i][j] = "-" #replace old spot with empty spot
            game_map.refreshMap
        else:
            print("you can't go that way")
    def move_left(self, space):
        if not self.leftIsWall:
            self.pos = matrix[i][j-1]
            matrix[i][j] = "-" #replace old spot with empty spot
            game_map.refreshMap
        else:
            print("you can't go that way")


class GameLoop:
    def __init__(self, iteration):
        self.ITERATIONS_PER_MINUTE = iteration
    async def onstep():
        player.checkWalls()
        await asyncio.sleep(60/self.ITERATIONS_PER_MINUTE)
        onstep()


class Map:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.matrix = [[Space() for i in range(width)] for j in range(height)]
    def refreshMap(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.isWall:
                    matrix[i][j] = "x"
                elif self.isCoin:
                    matrix[i][j] = "c"
                elif player.pos == self.pos:
                    matrix[i][j] = "P"
                else:
                    matrix[i][j] = "-"


game_map = Map(4, 5)
game_map.matrix[2][1].isWall = True
print(game_map.matrix)

'''
player = Player()

player.checkWalls()
options = ""
if player.topIsWall == False:
    options += "Press up to go up\n"
move = input(options)
if move == "up":
    player.move_up(space)

map =
[["-", "-", "x"],
["x", "P", "x"],
["x", "-", "x"]]
'''

#flawlessmode = spaces behind you turn into walls
#flashlightmode = can only see 4x4 around you
#racemode = against computer
#timedmode = timer
#zenmode = no coins, no time
#dontstopmode = stop moving for 2 seconds -> lose
