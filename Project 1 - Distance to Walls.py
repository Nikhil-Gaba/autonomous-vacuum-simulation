# Declare magic variables at the start of the program
WALL = "W"
VACUUMINATOR = "X"
EMPTY = "E"
DIRTY = "D"

def find_coordinates(world, character):
    """This function accepts the world and an object, either the 
    vacuuminator or the wall, and computes the coordinates of the object
    by the row and column it is in, returning these row and column numbers 
    of the objects as lists in a tuple.
    """
    row_numbers = []
    column_numbers = []
    # Here we can access each coordinate in the world grid
    for row in range(len(world)):
        for column in range(len(world[row])):
            if character == world[row][column]:
                row_numbers.append(row)
                column_numbers.append(column)
    return row_numbers, column_numbers

def distance_to_wall(world):
    """ This function accepts the world (list of lists) as input, and calculates
    the distance to the nearest wall of the vacuuminator, and returns this
    shortest distance as integer.
    """
    # Firstly, we check if the world input has a wall present (since distance 
    # to the nearest wall cannot be determined if no wall is in the grid)
    # We know that all inputs have exactly one vacuuminator
    wall_present = False
    for row in world:
        if WALL in row:
            wall_present = True
            break
            
    if not wall_present:
        return None
    
    # We obtain the position of the wall and the vacuuminator to find distance
    wall_position = find_coordinates(world, character=WALL)
    vacuum_position = find_coordinates(world, character=VACUUMINATOR)
    
    # We obtain all row and column numbers for all walls in the world 
    wall_rows = wall_position[0]
    wall_columns = wall_position[1]
    # And similarly, we can obtain the row and column number for the vacuum
    vacuuminator_row = vacuum_position[0][0]
    vacuuminator_column = vacuum_position[1][0]
    
    # Now we can find the Manhattan distance of each wall from the vacuuminator
    # and keep track of each distance
    distance = []
    for wall in range(len(wall_rows)):
        vertical_distance = abs(vacuuminator_row - wall_rows[wall])    
        horizontal_distance = abs(vacuuminator_column - wall_columns[wall])
        distance.append(horizontal_distance + vertical_distance)
        
    # We calculate the distance of the nearest wall from the vacuuminator 
    shortest_distance = min(distance)
 
    return shortest_distance