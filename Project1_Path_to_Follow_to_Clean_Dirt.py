# Declare magic variables at the start of the program
WALL = "W"
VACUUMINATOR = "X"
EMPTY = "E"
DIRTY = "D"

DIR_UP = "u"
DIR_DOWN = "d"
DIR_LEFT = "l"
DIR_RIGHT = "r"

def find_vacuuminator_coordinates(world_vacuum):
    """This function accepts the input world, and computes the coordinates of 
    the vacuuminator in terms of the row and the column it is in, returning the
    row and column numbers of the vacuuminator as integers.
    """
    # Here we access each coordinate in the world grid
    for row in range(len(world_vacuum)):
        for column in range(len(world_vacuum[row])):
            if VACUUMINATOR == world_vacuum[row][column]:
                return row, column

def up_sensor(world, row_number, column_number):
    """This function accepts the world, the row and the column the vacuuminator
    is in, and scans in an upward direction for the closest dirt (not scanning
    through walls). The function returns the row and column number until it 
    scanned, as well as the distance as an integer if dirt is detected.
    """
    new_row_number = row_number - 1
    while new_row_number >= 0:
        if world[new_row_number][column_number] == DIRTY:
            distance = row_number - new_row_number
            return (new_row_number, column_number, distance)
        # In the case the vacuuminator scans a wall or detects no dirt,
        # distance (of the nearest dirt) is set to None
        elif world[new_row_number][column_number] == WALL:
            return (new_row_number, column_number, None)
        new_row_number -= 1
    return(new_row_number, column_number, None)
    
def right_sensor(world, row_number, column_number):
    """This function accepts the world, the row and the column the vacuuminator
    is in, and scans right for the closest dirt (not scanning through walls). 
    The function returns the row and column number until it scanned, as well as
    the distance as an integer if dirt is detected.
    """
    new_column_number = column_number + 1
    for new_column_number in range(new_column_number, len(world[row_number])):
        if world[row_number][new_column_number] == DIRTY:
            distance = new_column_number - column_number
            return (row_number, new_column_number, distance)
        # In the case the vacuuminator scans a wall or detects no dirt,
        # distance (of the nearest dirt) is set to None
        elif world[row_number][new_column_number] == WALL:
            return (row_number, new_column_number, None)
        new_column_number += 1
    return (row_number, new_column_number, None)

def down_sensor(world, row_number, column_number):
    """This function accepts the world, the row and the column the vacuuminator
    is in, and scans downwards for the closest dirt (not scanning through 
    walls). The function returns the row and column number until it scanned, as
    well as the distance as an integer if dirt is detected.
    """
    new_row_number = row_number + 1
    for new_row_number in range(new_row_number, len(world)):
        if world[new_row_number][column_number] == DIRTY:
            distance = new_row_number - row_number
            return (new_row_number, column_number, distance)
        # In the case the vacuuminator scans a wall or detects no dirt,
        # distance (of the nearest dirt) is set to None
        elif world[new_row_number][column_number] == WALL:
            return (new_row_number, column_number, None)
        new_row_number += 1
    return (new_row_number, column_number, None)

def left_sensor(world, row_number, column_number):
    """This function accepts the world, the row and the column the vacuuminator
    is in, and scans left for the closest dirt (not scanning through walls). 
    The function returns the row and column number until it scanned, as well as
    the distance as an integer if dirt is detected.
    """
    new_column_number = column_number - 1
    while new_column_number >= 0:
        if world[row_number][new_column_number] == DIRTY:
            distance = column_number - new_column_number
            return (row_number, new_column_number, distance)
        # In the case the vacuuminator scans a wall or detects no dirt,
        # distance (of the nearest dirt) is set to None
        elif world[row_number][new_column_number] == WALL:
            return (row_number, new_column_number, None)
        new_column_number -= 1
    return (row_number, new_column_number, None)

def return_output(shortest_distance, direction):
    """ This function takes the shortest distance of dirt scanned and the 
    direction it was scanned, and calculates the moves to reach this dirt. The 
    output is the list of moves.
    """
    list_of_moves = []
    # The moves will represent the steps taken to reach the nearest dirt 
    # visible to the vacuum's sensors
    for i in range(shortest_distance):
        list_of_moves.append(direction)
    return list_of_moves

def path_to_next(world):
    """This function takes world as input, and computes the shortest distance 
    of dirt visible to the vacuuminator's sensors with priority on sensors 
    defined resolving ties. The function returns the next moves as a list.
    """    
    
    # Firstly, we determine the position of the vacuuminator
    vacuum_position = find_vacuuminator_coordinates(world)
    row_number = vacuum_position[0]
    column_number = vacuum_position[1]
        
    # We scan in all four directions for dirt and keep track of distances 
    # between the vacuum and the nearest dirt it detects from each sensor
    up = up_sensor(world, row_number, column_number)
    right = right_sensor(world, row_number, column_number)
    down = down_sensor(world, row_number, column_number)
    left = left_sensor(world, row_number, column_number)
    distances = [up[2], right[2], down[2], left[2]]
    
    # We ensure that all distances are integers, excluding distances with are 
    # None (if scanning did not detect dirt in the given direction)
    integer_distances = list(filter(lambda distance: distance is not None, 
                                    distances))
    
    # We calculate the shortest_distance provided that one sensor scanned dirt
    if integer_distances:
        shortest_distance = min(integer_distances)
    else:
        shortest_distance = None
        index = None
        
    # Next, we determine which sensor found the nearest dirt
    # This method prioritises directions in the order up, right, down, left 
    if shortest_distance is not None:
        index = distances.index(shortest_distance)
        
    # Finally, we can output the list of moves, since we know which sensor 
    # found the nearest dirt
    if index == 0:
        list_of_moves = return_output(shortest_distance, DIR_UP)
    elif index == 1:
        list_of_moves = return_output(shortest_distance, DIR_RIGHT)
    elif index == 2:
        list_of_moves = return_output(shortest_distance, DIR_DOWN)
    elif index == 3:
        list_of_moves = return_output(shortest_distance, DIR_LEFT)
    else:
        list_of_moves = []
    return list_of_moves
