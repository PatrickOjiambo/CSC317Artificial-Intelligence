"""The module world"""
from goal_state import define_goal_state
from main import world_grid, start_col,start_row

goal_state = define_goal_state(world_grid)
R = len(world_grid)
C = len(world_grid[0])

class World:
    """
    The world as it is Group whatever AI
    """
    def __init__(self, row, column, data):
        self.data = self.copy_world(data)
        self.location = (row, column)

        self.state = (self.location, self.data)

        self.dirt_locations = self.find_dirty_places()

        self.cost = 0
        self.heuristic = self.calc_manhattan_distance()
        self.combined_heuristic = self.cost + self.heuristic
        self.my_heuristic = self.cost + self.my_calculate_manhattan()
        self.action = None
        self.parent = None

        
    def is_dirt(self):
        """
        Checks if this is dirt
        """
        if self.data[self.location[0]][self.location[1]].isdigit():
            return True
        else:
            return False
    def suck(self):
        """
        Sucks the dirt
        """
        nDirts = int(self.data[self.location[0]][self.location[1]])
        nDirts -= 1
        self.data[self.location[0]][self.location[1]] = str(nDirts)
        if nDirts == 0:
            self.data[self.location[0]][self.location[1]] = ' '
    def find_path(self):
        """Find path to the dirt"""
        def reverse_list(list):
            """
            Reverse list.
            """
            temp = []
            while got_list:
                temp.append(got_list.pop())
            return temp
        path = [self.action]
        current_node = self.parent
        while current_node.parent is not None:
            path.append(current_node.action)
            current_node = current_node.parent
        return reverse_list(path)
    def find_dirty_places(self):
        """Self explanatory
        """
        temp_dirt_locations = []
        for r in range(len(self.data)):
            for c in range(len(self.data[r])):
                if self.data[r][c].isdigit():
                    temp_dirt_locations.append((r, c))
        return temp_dirt_locations
    def calc_manhattan_distance(self):
        """Calculates the manhattan distance
        for Greedy search"""
        manhattan = float('inf')
        for dirt_loc in self.dirt_locations:
            dirt_r = dirt_loc[0]
            dirt_c = dirt_loc[1]
            temp_manhattan = abs(dirt_r - self.location[0]) + abs(dirt_c - self.location[1])
            if temp_manhattan < manhattan:
                manhattan = temp_manhattan
        return manhattan
    def my_calculate_manhattan(self):
        manhattan = float('inf')
        for dirt_loc in self.dirt_locations:
            dirt_r = dirt_loc[0]
            dirt_c = dirt_loc[1]
            temp_manhattan =  2 * abs(dirt_r - self.location[0]) + abs(dirt_c - self.location[1])
            if temp_manhattan < manhattan:
                manhattan = temp_manhattan
        return manhattan
    @staticmethod
    def copy_world(data):
        """Copy of our environment"""
        copy_map = []
        for r in range(0, len(data)):
            line = []
            copy_map.append(line)
            for c in range(0, len(data[r])):
                line.append(data[r][c])
        return copy_map
    def is_exists_frontier(self):
        """Watch CS50"""
        for element in queue:
            if element.state == node.state:
                return queue.index(element)
    def actions(current_node):
        """The actions UP, DOWN, LEFT, RIGHT, SUCK"""
        current_r, current_c = current_node.location

        children = []

        dr = [0, 0, 0, 1, -1]
        dc = [0, -1, +1, 0, 0]

        for i in range(0, 5):

            possible_r = current_r + dr[i]
            possible_c = current_c + dc[i]

            if world_grid[possible_r][possible_c] == 'j':
                possible_r = possible_r + dr[i]
                possible_c = possible_c + dc[i]

            # Check it is not out of bounds.
            if possible_r < 0 or possible_c < 0:
                continue
            if possible_r >= R or possible_c >= C:
                continue
            if world_grid[possible_r][possible_c] == '#':
                continue

            child = Node(possible_r, possible_c, current_node.data)
            child.parent = current_node
            if i == 0 and child.isDirt():
                child.action = "suck"
                child.suck()
                child.cost = child.parent.cost + 2
                children.append(child)
            elif i == 1:
                child.action = "left"
                child.cost = child.parent.cost + 1
                children.append(child)
            elif i == 2:
                child.action = "right"
                child.cost = child.parent.cost + 1
                children.append(child)
            elif i == 3:
                child.action = "down"
                child.cost = child.parent.cost + 1
                children.append(child)
            elif i == 4:
                child.action = "up"
                child.cost = child.parent.cost + 1
                children.append(child)

        return children
    def depth_first_search(self):
        """Implementation using depth_first search algorithm"""
        start_node = Node(start_row, start_col, world_grid)

        visited = []
        stack = [start_node]
        while stack:
            current_node = stack.pop()

            if current_node.state[1] == goal_state:
                return len(visited), current_node.find_path(), current_node.cost

            if current_node.state not in visited:
                visited.append(current_node.state)

            children = actions(current_node)

            for child in children:
                if child.state not in visited:
                    stack.append(child)
    def greedy_search():
        """Implementaion using greedy search"""
        start_node = Node(start_row, start_col, world_grid)

        visited = []
        p_queue = [start_node]
        while p_queue:
            p_queue = sorted(p_queue, key=lambda x: x.heuristic)
            current_node = p_queue.pop(0)

            if current_node.state[1] == goal_state:
                return len(visited), current_node.find_path(), current_node.cost

            if current_node.state not in visited:
                visited.append(current_node.state)

            children = actions(current_node)

            for child in children:
                if child.state not in visited:
                    p_queue.append(child)
        
    