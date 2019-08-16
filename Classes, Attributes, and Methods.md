Classes
  -Attributes
    Description
  =Methods
    Description


Space
  is main space class. empty space represented in console with '-'


Coin(Space) (pickedUp = False)
  coin class. represented in console with 'c'

  -self.isPickedUp
    boolean. true means coin has been picked up


Wall(Space)
  wall class. represented in console with 'x'


Map (height, width)
  map class. holds all data and methods for game map

  -self.height
    height of matrix
  -self.width
    width of matrix
  -self.matrix
    holds matrix of game's objects

  =createWall(i, j)
    replaces empty space object at index[i][j] with wall object
  =createCoin(i, j)
    replaces empty space object at index[i][j] with coin object

  =snapshotMap
    returns encoding of object positions: [[matrix height, matrix width], [player posI, player posJ], [[coin1 posI, coin1 posJ], [coin2 posI, coin2 posJ]], [[wall1 posI, wall1 posJ], [wall2 posI, wall2 posJ]]]
  =printMap
    prints matrix visualization to console

Player (self, posI = 0, posJ = 0, topWall = False, rightWall = False, bottomWall = False, leftWall = False, coins = 0, moves = 0)
  player class. sits on top of space or coin class. represented in console with 'P'

  -self.posI
    position in main list (vertical position)
  -self.posJ
    position in sublist (horizontal position)

  -self.topIsWall
    boolean. true if space above is a wall
  -self.rightIsWall
    true if space to right is a wall
  -self.bottomIsWall
    true if space under is a wall
  -self.leftIsWall
    true if space to the left is a wall

  -self.coinCount
    counter of coins walked over
  -self.moveCount
    counter of successful moves

  =checkWalls
    updates which spaces around the player are walls after every move
  =checkCoin
    checks if current location is of type coin and not already picked up. if so, adds 1 to coin counter and sets coin to picked up

  =move_up
    checks if self.topIsWall. if not, changes position attributes one space up. then checks if a coin was walked over, and adds 1 to move count
  =move_right
    moves to the right
  =move_down
    moves down
  =move_left
    moves to the left
