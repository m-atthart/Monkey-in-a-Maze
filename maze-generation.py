#Kruskal's maze generation algorithm
import random
#first, initialise a matrix of size n*n




def iterate():
    #Find random closed (wall) cell, which is an even coordinate pair. generate a direction to go in
    #I is vertical axis, J is horizontal axis. direction=1 is vertical, direction=0 is horizontal
    random_i = int(random.randint(0,height)*2)
    random_j = int(random.randint(0,width)*2)
    direction=random.randint(0, 1)
    #check if the wall has already been opened
    if maze[random_i][random_j] != 0:
    #pass this time
        pass
    #check if the two cells on vertical are in the same group
    if direction==1:
        if maze[random_i - 1][random_j] != maze[random_i+1][random_j]:
            #set a holder variable for the top value, which will be passed down to the mid/bottom values
            top_value_holder=0
            for k in range(-1, 2):
                maze[random_i + k][random_j] = top_value_holder
