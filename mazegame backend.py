import time


class Space:
    def __init__(self, player = False):
        self.isPlayer = player #debugging purposes
    def __repr__(self): #debugging purposes
        if self.isPlayer:
            return "P"
        else:
            return "-"

class Coin(Space):
    def __init__(self, i, j, pickedUp = False):
        self.posI = i #debugging purposes
        self.posJ = j #debugging purposes
        self.isPickedUp = pickedUp
    def __repr__(self): #debugging purposes
        if player.posI == self.posI and player.posJ == self.posJ:
            return "P"
        elif not self.isPickedUp:
            return "c"
        else:
            return "-"

class Wall(Space):
    def __repr__(self): #debugging purposes
        return "x"


class Map:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.matrix = [[Space() for i in range(width)] for j in range(height)]

    def createWall(self, i, j):
        self.matrix[i][j] = Wall()
    def createCoin(self, i, j):
        self.matrix[i][j] = Coin(i, j)

    def snapshotMap(self): #encodes data for GUI
        dimensions = [[self.height, self.width]]
        playerpos = [[player.posI, player.posJ]]
        coins = [[]]
        walls = [[]]
        for i in range(self.height):
            for j in range(self.width):
                if type(self.matrix[i][j]) == Wall:
                    walls[0].append([i, j])
                elif type(self.matrix[i][j]) == Coin:
                    if not self.matrix[i][j].isPickedUp:
                        coins[0].append([i, j])
        encoding = dimensions + playerpos + coins + walls
        return encoding
    def printMap(self): #debugging purposes
        for i in range(len(self.matrix)):
            print(str(self.matrix[i]) + "\n")
        print("\n")


class Player:
    def __init__(self, posI = 0, posJ = 0, topWall = False, rightWall = False, bottomWall = False, leftWall = False, coins = 0, moves = 0):
        self.posI = posI
        self.posJ = posJ
        self.topIsWall = topWall #boolean. if space above is of type wall
        self.rightIsWall = rightWall
        self.bottomIsWall = bottomWall
        self.leftIsWall = leftWall
        self.coinCount = coins #coin counter
        self.moveCount = moves #move counter
        game_map.matrix[self.posI][self.posJ].isPlayer = True #initializes player on map

    def checkWalls(self): #checks spaces around player and changes attributes if needed
        if self.posI > 0 and type(game_map.matrix[self.posI-1][self.posJ]) == Wall: #checks if top is wall
            self.topIsWall = True
        if self.posJ+1 < game_map.width and type(game_map.matrix[self.posI][self.posJ+1]) == Wall:
            self.rightIsWall = True
        if self.posI+1 < game_map.height and type(game_map.matrix[self.posI+1][self.posJ]) == Wall:
            self.bottomIsWall = True
        if self.posJ > 0 and type(game_map.matrix[self.posI][self.posJ-1]) == Wall:
            self.leftIsWall = True
    def checkCoin(self): #checks if current space is of type coin
        if type(game_map.matrix[self.posI][self.posJ]) == Coin and not game_map.matrix[self.posI][self.posJ].isPickedUp:
            self.coinCount += 1
            game_map.matrix[self.posI][self.posJ].isPickedUp = True

    def move_up(self): #moves player up
        self.checkWalls()
        if not self.topIsWall:
            game_map.matrix[self.posI-1][self.posJ].isPlayer = True #debugging purposes
            game_map.matrix[self.posI][self.posJ].isPlayer = False #debugging purposes
            self.posI -= 1 #updates saved position values
            self.checkCoin()
            self.moveCount += 1
        else:
            print("You can't go that way\n")
        print(game_map.snapshotMap()) #debugging purposes
        game_map.printMap() #debugging purposes
    def move_right(self):
        self.checkWalls()
        if not self.rightIsWall:
            game_map.matrix[self.posI][self.posJ+1].isPlayer = True #debugging purposes
            game_map.matrix[self.posI][self.posJ].isPlayer = False #debugging purposes
            self.posJ += 1
            self.checkCoin()
            self.moveCount += 1
        else:
            print("You can't go that way\n")
        print(game_map.snapshotMap()) #debugging purposes
        game_map.printMap() #debugging purposes
    def move_down(self):
        self.checkWalls()
        if not self.bottomIsWall:
            game_map.matrix[self.posI+1][self.posJ].isPlayer = True #debugging purposes
            game_map.matrix[self.posI][self.posJ].isPlayer = False #debugging purposes
            self.posI += 1
            self.checkCoin()
            self.moveCount += 1
        else:
            print("You can't go that way\n")
        print(game_map.snapshotMap()) #debugging purposes
        game_map.printMap() #debugging purposes
    def move_left(self):
        self.checkWalls()
        if not self.leftIsWall:
            game_map.matrix[self.posI][self.posJ-1].isPlayer = True #debugging purposes
            game_map.matrix[self.posI][self.posJ].isPlayer = False #debugging purposes
            self.posJ -= 1
            self.checkCoin()
            self.moveCount += 1
        else:
            print("You can't go that way\n")
        print(game_map.snapshotMap()) #debugging purposes
        game_map.printMap() #debugging purposes







#example game
game_map = Map(4, 5) #initialize map with height: 4 and width: 5
player = Player(2, 1) #instantiates player at index[2][1]
game_map.createWall(3, 2) #places a wall at index[3][2]
game_map.createWall(0, 0)
game_map.createCoin(1, 3) #places coin at index[1][3]
game_map.createCoin(2, 4)
print(game_map.snapshotMap()) #prints encoding of map
game_map.printMap() #prints map to console
player.move_up() #moves player up
player.move_right()
print("Coins: " + str(player.coinCount))
player.move_right() #moves player on top of coin
print("Coins: " + str(player.coinCount)) #shows that player.coinCount increases
player.move_right()
player.move_down()
print("Coins: " + str(player.coinCount))
player.move_down()
player.move_left()
player.move_left() #tries to move player left into wall
print("Moves: " + str(player.moveCount)) #shows final successful move count
