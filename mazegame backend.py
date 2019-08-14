import time
#import asyncio


class Space:
    def __init__(self, wall = False, coin = False, player = False):
        self.isWall = wall
        self.isCoin = coin
        self.isPlayer = player

    def __repr__(self):
        if self.isWall:
            return "x"
        elif self.isPlayer:
            return "P"
        elif self.isCoin:
            return "c"
        else:
            return "-"

class Coin(Space):
    def __init__(self, i, j, pickedUp = False):
        self.posI = i
        self.posJ = j
        self.isPickedUp = pickedUp
    def __repr__(self):
        if not self.isPickedUp:
            return "c"
        else:
            return "-"

class Wall(Space):
    def __repr__(self):
        return "x"

class Map:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.matrix = [[Space() for i in range(width)] for j in range(height)]
    def refreshMap(self):
        self.matrix[player.posI][player.posJ].isPlayer = True
        print(self.matrix)
        '''
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.isWall:
                    matrix[i][j] = "x"
                elif self.isCoin:
                    matrix[i][j] = "c"
                elif self.isPlayer:
                    matrix[i][j] = "P"
                else:
                    matrix[i][j] = "-"
                '''


class Player:
    def __init__(self, posI, posJ, topWall = False, rightWall = False, bottomWall = False, leftWall = False, coins = 0, moves = 0):
        self.posI = posI
        self.posJ = posJ
        self.topIsWall = topWall
        self.rightIsWall = rightWall
        self.bottomIsWall = bottomWall
        self.leftIsWall = leftWall
        self.coinCount = coins
        self.moveCount = moves

    def checkWalls(self):
        if self.posI > 0 and type(game_map.matrix[self.posI-1][self.posJ]) == Wall: #checks if top is wall
            self.topIsWall = True
        if self.posJ+1 < game_map.width and type(game_map.matrix[self.posI][self.posJ+1]) == Wall:
            self.rightIsWall = True
        if self.posI+1 < game_map.height and type(game_map.matrix[self.posI+1][self.posJ]) == Wall:
            self.bottomIsWall = True
        if self.posJ > 0 and type(game_map.matrix[self.posI][self.posJ-1]) == Wall:
            self.leftIsWall = True

    def checkCoin(self):
        if type(game_map.matrix[self.posI][self.posJ]) == Coin:
            self.coinCount += 1
            game_map.matrix[self.posI][self.posJ].isPickedUp = True

    def move_up(self):
        self.checkWalls()
        if not self.topIsWall:
            game_map.matrix[self.posI-1][self.posJ].isPlayer = True
            game_map.matrix[self.posI][self.posJ].isPlayer = False #moves player up one spot
            self.posI -= 1 #changes saved position values
            self.checkCoin()
            self.moveCount += 1
        else:
            print("You can't go that way")
        game_map.refreshMap() #redraws map
    def move_right(self):
        self.checkWalls()
        if not self.rightIsWall:
            game_map.matrix[self.posI][self.posJ+1].isPlayer = True
            game_map.matrix[self.posI][self.posJ].isPlayer = False
            self.posJ += 1
            self.checkCoin()
            self.moveCount += 1
        else:
            print("You can't go that way")
        game_map.refreshMap()
    def move_down(self):
        self.checkWalls()
        if not self.bottomIsWall:
            game_map.matrix[self.posI+1][self.posJ].isPlayer = True
            game_map.matrix[self.posI][self.posJ].isPlayer = False
            self.posI += 1
            self.checkCoin()
            self.moveCount += 1
        else:
            print("You can't go that way")
        game_map.refreshMap()
    def move_left(self):
        self.checkWalls()
        if not self.leftIsWall:
            game_map.matrix[self.posI][self.posJ-1].isPlayer = True
            game_map.matrix[self.posI][self.posJ].isPlayer = False
            self.posJ -= 1
            self.checkCoin()
            self.moveCount += 1
        else:
            print("You can't go that way")
        game_map.refreshMap()




game_map = Map(4, 5) #initialize map with height: 4 and width: 5)

def createWall(i, j):
    game_map.matrix[i][j].isWall = True
def createCoin(i, j):
    coin = Coin(i, j)
    game_map.matrix[i][j] = coin

createWall(3, 2) #places a wall at index[3][2]
player = Player(2, 1) #instantiates player at index[2][1]
createCoin(1, 3) #places coin at index[1][3]
game_map.refreshMap() #draws map
player.move_up() #moves player up
player.move_right()
print("Coins: " + str(player.coinCount))
player.move_right() #moves over coin
print("Coins: " + str(player.coinCount)) #shows that player.coinCount gets affected
player.move_right()
player.move_down()
player.move_down()
player.move_left() #tries to move player left into wall
player.move_left()
print("Moves: " + str(player.moveCount))




'''
class GameLoop:
    def __init__(self, iteration):
        self.ITERATIONS_PER_MINUTE = iteration
    async def onstep():
        player.checkWalls()
        await asyncio.sleep(60/self.ITERATIONS_PER_MINUTE)
        Map.refreshMap()
        onstep()
'''

#flawlessmode = spaces behind you turn into walls
#flashlightmode = can only see 4x4 around you
#racemode = against computer
#timedmode = timer
#zenmode = no coins, no time
#dontstopmode = stop moving for 2 seconds -> lose


"""
TODO

-make coin/wall subclasses
-player move counter
-coin to coin that has been picked up, not class change

"""
