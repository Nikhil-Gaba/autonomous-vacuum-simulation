from task3 import path_to_next

# Declare magic variables at the start of the program
WALL = "W"
VACUUMINATOR = "X"
EMPTY = "E"
DIRTY = "D"

DIR_UP = "u"
DIR_DOWN = "d"
DIR_LEFT = "l"
DIR_RIGHT = "r"

def find_vacuuminator_coordinates(vacuuminator_world):
    """This function accepts the input world, and computes the coordinates of 
    the vacuuminator in terms of the row and the column it is in, returning the
    row and column numbers of the vacuuminator as integers.
    """
    # Here we access each coordinate in the world grid
    for row in range(len(vacuuminator_world)):
        for column in range(len(vacuuminator_world[row])):
            if VACUUMINATOR == vacuuminator_world[row][column]:
                return row, column

def updated_world_row_column(direction, vacuuminator_world, row, column):
    """ This function accepts the current world, the row and column the 
    vacuuminator is in, and the direction the vacuuminator moves. This function
    updates the world, the row and the column of the vacuuminator according to 
    the prescribed direction, returning the three updated variables.
    """
    # Clean the current position of vacuum before the world updates
    vacuuminator_world[row][column] = EMPTY
    if direction == DIR_UP:
        row -= 1
    elif direction == DIR_RIGHT:
        column += 1
    elif direction == DIR_DOWN:
        row += 1
    elif direction == DIR_LEFT:
        column -= 1
    # The vacuuminator moves to its new position 
    vacuuminator_world[row][column] = VACUUMINATOR
    return vacuuminator_world, row, column

def cleaning_on_sensors(complete_path, world, row, column, backtracking_list):
    """ This function accepts the complete path until now, the current world,
    row and column of the vacuuminator and the backtracking list. It operates 
    to detect dirt and calculates the cleaning cycle until no more dirt can be 
    detected. We also keep track of the opposite moves taken to enable 
    backtracking. The function returns the same outputs as inputs.
    """
       
    # Here we conduct the cleaning cycle, repeatedly identifying the next path
    # the vacuuminator should move and scanning at the new position until no
    # more dirt can be detected.
    cleaning_cycle = []
    while True:
        next_path = path_to_next(world)
        if next_path == []:
            break
        for move in next_path:
            complete_path.append(move)
            cleaning_cycle.append(move)
            # update the world, the row and the column so that the vacuum can
            # scan at the new position
            new_world_row_column = updated_world_row_column(move, world, 
                                                            row, column)
            world = new_world_row_column[0]
            row = new_world_row_column[1]
            column = new_world_row_column[2]
    
    # We must define the opposite directions to ensure backtracking is possible 
    opposite_dictionary = {DIR_UP: DIR_DOWN, DIR_RIGHT: DIR_LEFT,
                           DIR_DOWN: DIR_UP, DIR_LEFT: DIR_RIGHT}

    # We keep track of the opposite moves (in reverse order, since the vacuum
    # will backtrack along its original path)
    for move in cleaning_cycle:
        backtracking_list.insert(0, opposite_dictionary[move])
    return (complete_path, row, column, backtracking_list, world)

def backtracking(backtracking_list, complete_path, world, row_number, 
                 column_number):
    """ This function accepts a list of ordered moves to backtrack, the 
    complete path thus far, the world and the current row and columns of the
    vacuum. The function repeatedly backtracks one move and checks if any dirt
    can be detected from this new position. Once the vacuuminator is back to
    its original position, the complete path is the output from this function.
    """
    
    while backtracking_list:
        next_move = backtracking_list[0]
        complete_path.append(next_move)
        updated_variables = updated_world_row_column(next_move, world,
                                                     row_number, column_number)
        world = updated_variables[0]
        row_number = updated_variables[1]
        column_number = updated_variables[2]
        # We remove the backtracked move so that we backtrack subsequent moves
        backtracking_list.remove(next_move)
        # Start a new cleaning cycle if dirt is detected from the new position
        cleaning_cycle = cleaning_on_sensors(complete_path, world, row_number,
                                             column_number, backtracking_list)
        complete_path = cleaning_cycle[0]
        row_number = cleaning_cycle[1]
        column_number = cleaning_cycle[2]
        backtracking_list = cleaning_cycle[3]
        world = cleaning_cycle[4]
        
    return complete_path
    
def clean_path(world):
    """This function accepts the input world, finds the coordinates of
    the vacuuminator, conducts a cleaning cycle based on the vacuuminator's 
    sensors, then backtracks along its original path, scanning for dirt along 
    this path. The function outputs the complete path of moves as a list.
    """
    complete_path = []   
    backtracking_list = []
    
    # Firstly, we determine the position of the vacuuminator
    vacuum_position = find_vacuuminator_coordinates(world)
    row_number = vacuum_position[0]
    column_number = vacuum_position[1]
    
    # We can now conduct a cleaning cycle, with the vacuuminator moving towards
    # the dirt closest, and scanning for dirt at this new position 
    initial_cleaning_cycle = cleaning_on_sensors(complete_path, world, 
                                                 row_number, column_number, 
                                                 backtracking_list)
    complete_path = initial_cleaning_cycle[0]
    row_number = initial_cleaning_cycle[1]
    column_number = initial_cleaning_cycle[2]
    backtracking_list = initial_cleaning_cycle[3]
    world = initial_cleaning_cycle[4]
    
    # Lastly, we backtrack along the path taken thus far, scanning for dirt 
    # at each position backtracked. 
    complete_path = backtracking(backtracking_list, complete_path, world, 
                                 row_number, column_number)
  
    return complete_path