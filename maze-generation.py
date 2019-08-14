#Kruskal's maze generation algorithm
import random
#first, initialise a matrix of size n*n


#Seet some of the cells to open cells - that is, cells where we can start.
open_counter=1
for i in range(5):
    for j in range(5):
        if i%2 != 0 and j%2 != 0:
            maze[i][j]=open_counter
            open_counter+=1




def iterate():
    #Find random closed (wall) cell, which is an odd coordinate pair. generate a direction to go in
    #I is vertical axis, J is horizontal axis. direction=1 is vertical, direction=0 is horizontal
    random_i=random.randrange(1, height, 2)
    random_j=random.randrange(1, width, 2)
    direction=random.randint(0, 1)
    #check if the wall has already been opened
    if maze[random_i][random_j] != 0:
    #pass this time
        pass
    #check if the two cells on vertical are in the same group
    if direction==1:
        if maze[random_i - 1][random_j] != maze[random_i+1][random_j]:
            #set a holder variable for the top value, which will be passed down to the mid/bottom values
            top_value_holder=maze[random_i+1][random_j]
            for k in range(-1, 2):
                maze[random_i + k][random_j] = top_value_holder
        if direction==0:
            if maze[random_i][random_j - 1] != maze[random_i][random_j+1]:
                #set a holder variable for the left value, which will be passed down to the mid/bottom values
                top_value_holder=maze[random_i][random_j -1]
                for k in range(-1, 2):
                    maze[random_i][random_j + k] = top_value_holder
    for i in maze:
        print(i)
        
        
 #begin iteration
for i in range(0, ((height*width)//4)):
    iterate()
