from math import floor

maze = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
[1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
[1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

nodelist = [
[[1,1],      [1,5],[1,7],[1,9],       [1,13]],
[[3,1],[3,3],            [3,9],[3,11]       ],
[[5,1],[5,3],      [5,7],[5,9],[5,11],[5,13]],
[[7,1],[7,3],[7,5],            [7,11],[7,13]]
]

big_maze = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
[1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
[1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
[1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
[1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
[1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

def get_nodes(maze):
    nodes = []
    node_rows = [i*2+1 for i in range(len(maze)//2)]

    for i in node_rows:
        for j in range(len(maze[i])):
            numOfWalls = 0
            topIsWall = False
            rightIsWall = False
            bottomIsWall = False
            leftIsWall = False
            if i > 0 and maze[i-1][j] == 1:
                topIsWall = True
                numOfWalls += 1
            if j+1 < len(maze[i]) and maze[i][j+1] == 1:
                rightIsWall = True
                numOfWalls += 1
            if i+1 < len(maze) and maze[i+1][j] == 1:
                bottomIsWall = True
                numOfWalls += 1
            if j > 0 and maze[i][j-1] == 1:
                leftIsWall = True
                numOfWalls += 1

            if maze[i][j] != 1:
                if numOfWalls != 4:
                    if numOfWalls != 2:
                        nodes.append([i,j])
                    elif not (topIsWall and bottomIsWall):
                        if not (rightIsWall and leftIsWall):
                            nodes.append([i,j])
    return nodes


def pairing(i, j):
    if i >= j:
        return i**2 + i + j
    else:
        return j**2 + i

def unpairing(k):
    if k - (floor(k**(1/2)))**2 < floor(k**(1/2)):
        return [k - (floor(k**(1/2)))**2, floor(k**(1/2))]
    else:
        return [floor(k**(1/2)), k - (floor(k**(1/2)))**2 - floor(k**(1/2))]


def get_ref(nodes): #debugging purposes
    ref_dict = {}
    for [i, j] in nodes:
        ref_dict[pairing(i, j)] = [i, j]
    return ref_dict


def get_graph(maze):
    nodes = get_nodes(maze)
    graph_dict = {}
    for node in nodes:
        i, j = node
        current_i = i
        current_j = j
        while maze[i][j] != 1:
            i -= 1
            if [i, j] in nodes:
                key = pairing(current_i, current_j)
                value = pairing(i, j)
                try:
                    graph_dict[key].append(value)
                    break
                except KeyError:
                    graph_dict[key] = [value]
                    break
                break
        i = current_i
        j = current_j
        while maze[i][j] != 1:
            j += 1
            if [i, j] in nodes:
                key = pairing(current_i, current_j)
                value = pairing(i, j)
                try:
                    graph_dict[key].append(value)
                    break
                except KeyError:
                    graph_dict[key] = [value]
                    break
                break
        i = current_i
        j = current_j
        while maze[i][j] != 1:
            i += 1
            if [i, j] in nodes:
                key = pairing(current_i, current_j)
                value = pairing(i, j)
                try:
                    graph_dict[key].append(value)
                    break
                except KeyError:
                    graph_dict[key] = [value]
                    break
                break
        i = current_i
        j = current_j
        while maze[i][j] != 1:
            j -= 1
            if [i, j] in nodes:
                key = pairing(current_i, current_j)
                value = pairing(i, j)
                try:
                    graph_dict[key].append(value)
                    break
                except KeyError:
                    graph_dict[key] = [value]
                    break
                break
        i = current_i
        j = current_j
    return graph_dict



def bfs_shortest_path(graph, start, goal):
    explored = []
    queue = [[start]]
    if start == goal:
        return start
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path
            explored.append(node)
    return None

def solve_maze(maze):
    return [unpairing(node) for node in bfs_shortest_path(get_graph(maze), pairing(1, 1), pairing(len(maze)-2, len(maze[-2])-2))]
