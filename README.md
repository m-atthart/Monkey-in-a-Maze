# Monkey in a Maze
Cambridge Immerse CompSci Project

Application designed by 7 budding software engineers in an introductory computer science course at a summer school program.

---------------------------------------------------------------------------------------

Classes
  -Attributes
    Description
  =Methods
    Description


Space (self, wall = False, coin = False, player = False)
  -self.isWall
    boolean. true means space is wall.
  -self.isCoin
    boolean. true means space is coin.
  -self.isPlayer
    boolean. true means space is player.
  =repr
    defines how 'space' object is printed in matrix. empty: -; wall: x; coin: c; player: p

Map (self, height, width)
  -self.height
    height of matrix
  -self.width
    width of matrix
  -self.matrix
    uses height and width to instantiate matrix of empty spaces, then continues to hold the matrix for rest of game
  =refreshMap
    reprints matrix

Player (self, posI, posJ, topWall = False, rightWall = False, bottomWall = False, leftWall = False)
  -self.posI
    position in main list (vertical position)
  -self.posJ
    position in sublist (horizontal position)
  -self.topIsWall
    boolean. true if matrix[posI-1][posJ].isWall
  -self.rightIsWall
    boolean. true if matrix[posI][posJ+1].isWall
  -self.bottomIsWall
    boolean. true if matrix[posI+1][posJ].isWall
  -self.leftIsWall
    boolean. true if matrix[posI][posJ-1].isWall

  =checkWalls
    function to update self.topIsWall, self.rightIsWall, self.bottomIsWall, self.leftIsWall values after every move

  =move_up
    checks if self.topIsWall. if not, changes matrix[posI-1][posJ].isPlayer to True, matrix[posI][posJ].isPlayer to False, and self.posI to posI-1
  =move_right
    checks if self.rightIsWall. if not, changes matrix[posI][posJ+1].isPlayer to True, matrix[posI][posJ].isPlayer to False, and self.posJ to posJ+1
  =move_down
    checks if self.bottomIsWall. if not, changes matrix[posI+1][posJ].isPlayer to True, matrix[posI][posJ].isPlayer to False, and self.posI to posI+1
  =move_left
    checks if self.leftIsWall. if not, changes matrix[posI][posJ-1].isPlayer to True, matrix[posI][posJ].isPlayer to False, and self.posJ to posJ-1
