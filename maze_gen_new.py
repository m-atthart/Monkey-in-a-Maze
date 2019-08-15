#MAZE GENERATOR
#generating a random maze n x n with adaptable n
maze = []
width = int(10)
height = int(10)
count = 1
#adding the rows to the bigger list and so to the matrix
for i in range(height):
    row = []
    for j in range(width):
        row.append(count)
        count += 1
    maze.append(row)

for t in maze:
    print(t)

#first if
#finding the values attached to the indexes with odd numbers in an even row and turning them into a wall by replacing them with a zero
#second if
#finding the values attached to the odd rows and turning them into a wall by replacing them with a zero
#only the values attached to even indexes in both i(vertical) an j(horizontal) direction stay numbered

open_counter=1
for num1 in range(height):
    for num2 in range(width):
        if num1 % 2 == 0:
            if num2 % 2 == 1:
                maze[num1][num2] = 0
        if num1 % 2 == 1:
            maze[num1][num2] = 0

for t in maze:
    print(t)






















