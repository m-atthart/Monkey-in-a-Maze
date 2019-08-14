# Monkey in a Maze
Cambridge Immerse CompSci Project

Application designed by 7 budding software engineers in an introductory computer science course at a summer school program.

---------------------------------------------------------------------------------------

Mode Ideas:

Flawless Mode = Spaces behind you turn into walls
Flashlight Mode = Can only see small square around you
Race Mode = Against computer
Timed Mode = Play with timer
Zen Mode = No coins, no timer
Don't Stop Mode = Stop moving for 2 seconds results in automatic loss

---------------------------------------------------------------------------------------

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
    uses height and width to instantiate matrix of empty spaces, then continues to hold the matrix for rest of game

  =createWall(i, j)
    replaces empty space object at index[i][j] with wall object
  =createCoin(i, j)
    replaces empty space object at index[i][j] with coin object

  =snapshotMap
    returns encoding of object data: [[matrix height, matrix width], [player posI, player posJ], [[coin1 posI, coin1 posJ], [coin2 posI, coin2 posJ]], [[wall1 posI, wall1 posJ], [wall2 posI, wall2 posJ]]]
  =printMap
    prints matrix visualization to console

Player (self, posI = 0, posJ = 0, topWall = False, rightWall = False, bottomWall = False, leftWall = False, coins = 0, moves = 0)
  player class. sits on top of space or coin class. represented in console with 'P'
  -self.posI
    position in main list (vertical position)
  -self.posJ
    position in sublist (horizontal position)
  -self.topIsWall
    boolean. true if matrix[posI-1][posJ] (space above) is of type wall
  -self.rightIsWall
    boolean. true if matrix[posI][posJ+1] (space to the right) is of type wall
  -self.bottomIsWall
    boolean. true if matrix[posI+1][posJ] (space under) is of type wall
  -self.leftIsWall
    boolean. true if matrix[posI][posJ-1] (space to the left) is of type wall
  -self.coinCount
    counter of coins walked over
  -self.moveCount
    counter for number of successful moves

  =checkWalls
    function to update self.topIsWall, self.rightIsWall, self.bottomIsWall, self.leftIsWall values after every move
  =checkCoin
    checks if current location is of type coin and not already picked up. if so, adds 1 to coin counter and sets coin to picked up

  =move_up
    checks if self.topIsWall. if not, subtracts 1 from self.posI. then checks coin, and adds 1 to move count
  =move_right
    checks if self.rightIsWall. if not, adds 1 to self.posJ. then checks coin, and adds 1 to move count
  =move_down
    checks if self.bottomIsWall. if not, adds 1 to self.posI. then checks coin, and adds 1 to move count
  =move_left
    checks if self.leftIsWall. if not, subtracts 1 from self.posJ. then checks coin, and adds 1 to move count
