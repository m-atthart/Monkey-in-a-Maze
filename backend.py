import time


class Space:
    def __init__(self, player = False):
        self.isPlayer = player #debugging purposes
    def __repr__(self): #debugging purposes
        if self.isPlayer:
            return "2"
        else:
            return "0"

class Coin(Space):
    def __init__(self, i, j, pickedUp = False):
        self.posI = i #debugging purposes
        self.posJ = j #debugging purposes
        self.isPickedUp = pickedUp
    def __repr__(self): #debugging purposes
        if player.posI == self.posI and player.posJ == self.posJ:
            return "2"
        elif not self.isPickedUp:
            return "4"
        else:
            return "0"

class Wall(Space):
    def __repr__(self): #debugging purposes
        return "1"

class Exit(Space):
    def __repr__(self): #debugging purposes
        return "3"

class Map:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.matrix = [[Space() for i in range(width)] for j in range(height)]

    def createWall(self, i, j):
        self.matrix[i][j] = Wall()
    def createCoin(self, i, j):
        self.matrix[i][j] = Coin(i, j)
    def createExit(self, i, j):
        self.matrix[i][j] = Exit()

    def snapshotMap(self, player, player2): #encodes data for GUI
        dimensions = [[self.height, self.width]]
        playerpos = [[player.posI, player.posJ]]
        player2pos = [[player2.posI, player2.posJ]]
        exitpos = [[]]
        coins = [[]]
        walls = [[]]
        for i in range(self.height):
            for j in range(self.width):
                if type(self.matrix[i][j]) == Exit:
                    exitpos[0].append([i, j])
                elif type(self.matrix[i][j]) == Wall:
                    walls[0].append([i, j])
                elif type(self.matrix[i][j]) == Coin:
                    if not self.matrix[i][j].isPickedUp:
                        coins[0].append([i, j])
        encoding = dimensions + playerpos + player2pos + exitpos + walls + coins
        return encoding
    def printMap(self): #debugging purposes
        for i in range(len(self.matrix)):
            print(str(self.matrix[i]) + "\n")
        print("\n")


class Player:
    def __init__(self, posI, posJ, gamemap, topWall = False, rightWall = False, bottomWall = False, leftWall = False, coins = 0, moves = 0):
        self.posI = posI
        self.posJ = posJ
        self.topIsWall = topWall #boolean. if space above is of type wall
        self.rightIsWall = rightWall
        self.bottomIsWall = bottomWall
        self.leftIsWall = leftWall
        self.coinCount = coins #coin counter
        self.moveCount = moves #move counter
        gamemap.matrix[self.posI][self.posJ].isPlayer = True #initializes player on map

    def checkWalls(self, gamemap): #checks spaces around player and changes attributes if needed
        if self.posI > 0 and type(gamemap.matrix[self.posI-1][self.posJ]) == Wall: #checks if top is wall
            self.topIsWall = True
        if self.posJ+1 < gamemap.width and type(gamemap.matrix[self.posI][self.posJ+1]) == Wall:
            self.rightIsWall = True
        if self.posI+1 < gamemap.height and type(gamemap.matrix[self.posI+1][self.posJ]) == Wall:
            self.bottomIsWall = True
        if self.posJ > 0 and type(gamemap.matrix[self.posI][self.posJ-1]) == Wall:
            self.leftIsWall = True
        if self.posI > 0 and type(gamemap.matrix[self.posI-1][self.posJ]) != Wall:
            self.topIsWall = False
        if self.posJ+1 < gamemap.width and type(gamemap.matrix[self.posI][self.posJ+1]) != Wall:
            self.rightIsWall = False
        if self.posI+1 < gamemap.height and type(gamemap.matrix[self.posI+1][self.posJ]) != Wall:
            self.bottomIsWall = False
        if self.posJ > 0 and type(gamemap.matrix[self.posI][self.posJ-1]) != Wall:
            self.leftIsWall = False

    def checkCoin(self, gamemap): #checks if current space is of type coin
        if type(gamemap.matrix[self.posI][self.posJ]) == Coin and not gamemap.matrix[self.posI][self.posJ].isPickedUp:
            self.coinCount += 1
            gamemap.matrix[self.posI][self.posJ].isPickedUp = True

    def move_up(self, gamemap): #moves player up
        self.checkWalls(gamemap)
        if not self.topIsWall:
            gamemap.matrix[self.posI-1][self.posJ].isPlayer = True #debugging purposes
            gamemap.matrix[self.posI][self.posJ].isPlayer = False #debugging purposes
            self.posI -= 1 #updates saved position values
            self.checkCoin(gamemap)
            self.moveCount += 1
        else:
            print("You can't go that way\n")
        #print(gamemap.snapshotMap(self)) #debugging purposes
        gamemap.printMap() #debugging purposes
    def move_right(self, gamemap):
        self.checkWalls(gamemap)
        if not self.rightIsWall:
            gamemap.matrix[self.posI][self.posJ+1].isPlayer = True #debugging purposes
            gamemap.matrix[self.posI][self.posJ].isPlayer = False #debugging purposes
            self.posJ += 1
            self.checkCoin(gamemap)
            self.moveCount += 1
        else:
            print("You can't go that way\n")
        #print(gamemap.snapshotMap(self)) #debugging purposes
        gamemap.printMap() #debugging purposes
    def move_down(self, gamemap):
        self.checkWalls(gamemap)
        if not self.bottomIsWall:
            gamemap.matrix[self.posI+1][self.posJ].isPlayer = True #debugging purposes
            gamemap.matrix[self.posI][self.posJ].isPlayer = False #debugging purposes
            self.posI += 1
            self.checkCoin(gamemap)
            self.moveCount += 1
        else:
            print("You can't go that way\n")
        #print(gamemap.snapshotMap(self)) #debugging purposes
        gamemap.printMap() #debugging purposes
    def move_left(self, gamemap):
        self.checkWalls(gamemap)
        if not self.leftIsWall:
            gamemap.matrix[self.posI][self.posJ-1].isPlayer = True #debugging purposes
            gamemap.matrix[self.posI][self.posJ].isPlayer = False #debugging purposes
            self.posJ -= 1
            self.checkCoin(gamemap)
            self.moveCount += 1
        else:
            print("You can't go that way\n")
        #print(gamemap.snapshotMap(self)) #debugging purposes
        gamemap.printMap() #debugging purposes







#example game
'''
game_map = Map(10, 10) #initialize map with height: 4 and width: 5
player = Player(2, 1, game_map) #instantiates player at index[2][1]
game_map.createWall(3, 2) #places a wall at index[3][2]
game_map.createWall(0, 0)
game_map.createCoin(1, 3) #places coin at index[1][3]
game_map.createCoin(2, 4)
'''
#game_map.printMap()
#player.move_right(game_map)
