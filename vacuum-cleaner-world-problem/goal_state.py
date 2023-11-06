"""Defines the goal test"""
def define_goal_state(world):
    """Defines the goal state. Replaces all digits with spaces.
    Essentially checks that there is no dirt.
    Args:
        world - A list of strings representing the rows in a grid
    """
    world_copy = []
    for position in range(0, len(world)):
        line = []
        world_copy.append(line)
        for alpha in range(0, len(world[position])):
            if world[position][alpha].isdigit():
                    line.append(' ')
            else:
                line.append(world[position][alpha])
    return world_copy
