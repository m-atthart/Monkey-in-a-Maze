class Space:
    def __init__(self, pos, wall = False, coin = False):
        self.pos = pos #matrix[i][j]
        self.isWall = wall
        self.isCoin = coin

class Player:
    def __init__(self, pos, topWall, rightWall):
        self.pos = pos
        self.topIsWall = topWall
        self.rightIsWall = rightWall
    def checkWalls(self, pos):
        if pos[i-1][j].isWall: #checks if top is wall
            self.topIsWall = True
        if pos[i][j+1].isWall: #checks if right is wall
            self.rightIsWall = True
    def move_up(space):
        if not self.topIsWall:
            self.pos = matrix[i+1][j]
            map.refreshMap
        else:
            print("you can't go that way")


class FoundExit:

class Map:
    def refreshMap(self):


player = Player()

player.checkWalls()
options = ""
if player.topIsWall == False:
    options += "Press up to go up\n"
move = input(options)d
if move == "up":
    player.move_up(space)

map =d
[[-, -, x],
[x, P, x],
[x, -, x]]


#flawlessmode = spaces behind you turn into walls
#flashlightmode = can only see 4x4 around you
#racemode = against computer
#timedmode = timer
#zenmode = no coins, no time
#dontstopmode = stop moving for 2 seconds -> lose
