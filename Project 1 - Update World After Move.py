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
    row and column numbers of the vacuuminator as an integer.
    """
    # Here we can access each coordinate in the world grid
    for row in range(len(world_vacuum)):
        for column in range(len(world_vacuum[row])):
            if VACUUMINATOR == world_vacuum[row][column]:
                return world_vacuum, row, column
                
def update_world(vacuum_world, row_number, column_number, direction_to_move):
    """ This function accepts the world, the row and column the vacuuminator is 
    in as well as the direction the vacuuminator moves in as input. The 
    function updates the world by first updating the row and column numbers if 
    the move is legal. The function returns the updated state of the world.
    """
    if direction_to_move == DIR_UP:
        new_row = row_number - 1
        new_column = column_number

    elif direction_to_move == DIR_DOWN:
        new_row = row_number + 1
        new_column = column_number

    elif direction_to_move == DIR_LEFT:
        new_row = row_number
        new_column = column_number - 1

    elif direction_to_move == DIR_RIGHT:
        new_row = row_number
        new_column = column_number + 1

    # only updates the world if the move is legal (that is, it will not take 
    # the vacuum off the edge of the world or crash into the wall)
    if 0 <= new_row < len(vacuum_world) and\
        0 <= new_column < len(vacuum_world[0]):
        if vacuum_world[new_row][new_column] != WALL: 
            vacuum_world[new_row][new_column] = VACUUMINATOR
            vacuum_world[row_number][column_number] = EMPTY
    return vacuum_world
    
def make_move(world, direction):
    """ This function accepts the world (a list of lists) and a direction the
    vacuuminator should move, updating the world provided that it is a possible 
    move. The function returns the updated state of the world.
    """
      
    # Firstly, we determine the position of the vacuum by its row and column
    vacuum_position = find_vacuuminator_coordinates(world)
    row = vacuum_position[1]
    column = vacuum_position[2]
    
    # We update the world if the move is possible, or output the original world
    # if the move is not possible
    updated_world = update_world(world, row, column, direction)
    return updated_world