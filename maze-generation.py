#Kruskal's maze generation algorithm
import random

## START CASPAR CODE

#generating a random maze n x n with adaptable n
maze = []
width = 11
height = 11
count = 1
def printmaze():
    for pm in maze:
        print(pm)
    print("\n")
#adding the rows to the bigger list and so to the matrix
for i in range(height):
    row = []
    for j in range(width):
        row.append(0)
    maze.append(row)
#Seet some of the cells to open cells - that is, cells where we can start.
open_counter=1
for i in range(height):
    for j in range(width):
        if i%2 == 0 and j%2 == 0:
            maze[i][j]=open_counter
            open_counter+=1

##### DEN CODE STARTS
#define random even number generators. these select the first open cell 
def random_i_generator():
    random_i=random.randrange(0, height, 2)
    return(random_i)
def random_j_generator():
    random_j=random.randrange(0, width , 2)
    return(random_j)
def iterate():
    #Find random closed (wall) cell, which is an odd coordinate pair. generate a direction to go in
    #I is vertical axis, J is horizontal axis. direction=1 is vertical, direction=0 is horizontal
    random_i=random_i_generator()
    random_j=random_j_generator()
    direction=random.randint(0,1)
    #shift random_i and random_j to the coordinates of a nearby wall, depending on direction
    if direction==1: #vertical:
        if random_i+2 >= height:
            random_i = random_i -1 # use the wall below if can't go above
        else:
            random_i += 1 # else use above wall
    if direction==0: #horizontal:
        if random_j+2 >= width:
            random_j = random_j -1 # use the wall left if can't go right
        else: # use right wall
            random_j += 1
    #check if the wall has already been opened
    if maze[random_i][random_j] != 0:
        pass
    #check if the two cells on vertical are in the same group
    if direction==1:
        if  maze[random_i+1][random_j] != maze[random_i -1][random_j]:
            #set a holder variable for the top value, which will be passed down to the mid/bottom values
            top_value_holder=maze[random_i+1][random_j]
            for k in range(-1, 2):
                maze[random_i + k][random_j] = top_value_holder
        
    if direction==0:
        if maze[random_i][random_j+1] != maze[random_i][random_j-1]:
            #set a holder variable for the left value, which will be passed down to the mid/bottom values
            top_value_holder=maze[random_i][random_j -1]
            for k in range(-1, 2):
                maze[random_i][random_j + k] = top_value_holder
printmaze()
for _ in range(0, (width*height)*4):
    iterate()

printmaze()
        
