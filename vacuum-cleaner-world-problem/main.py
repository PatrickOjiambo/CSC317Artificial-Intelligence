import sys
from world import World
algorithm = sys.argv[1]
initial_world = sys.argv[2]
file = open(initial_world)
raw_world_grid = file.readlines()
start_row = None
start_col = None
number_of_dirts = 0
dirt_locations = []
world_grid = []
for r in range(len(raw_world_grid)):
    line = []
    if raw_world_grid[r][-1] == '\n':
        raw_world_grid[r] = raw_world_grid[r][:-1]
    world_grid.append(line)
    for c in (range(len(raw_world_grid[r]))):
        line.append(raw_world_grid[r][c])
        if raw_world_grid[r][c] == 'a':
            world_grid[r][c] = ' '
            start_row = r
            start_col = c
        if raw_world_grid[r][c].isdigit():
            dirt_locations.append((r,c))
            number_of_dirts +=int(raw_world_grid[r][c])
"""Up until this point, I have just recorded the starting position of the 
cleaning agent as well as the number of dirts and their current positions(like a point in a plane)
"""
expanded_nodes = None
path = None
cost = None
initial_heuristic=None
if(algorithm == "depth_first"):
    expanded_nodes, path, cost = World.depth_first_search()
elif(algorithm == "greedy_search"):
    expanded_nodes, path, cost = World.greedy_search()
else:
    "Check your commandline arguments you lambistic motherfucker"
print(f"The number of nodes that have been expanded: {expanded_nodes}")
print("path taken by the vacuum cleaner to the goal:", end=' ')
print(*path, sep=' ')
print(f"Path cost of the solution: {cost}")
print("If you watched the videos I sent you would have known that greedy search is supposed to be better")
print("NB Depth first search is uninformed search- no intelligence\nGreedy search on the other hand has some information about the environment hence more intelligent. It falls under informed search.")