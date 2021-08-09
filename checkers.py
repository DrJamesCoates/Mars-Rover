import check_functions
import convert_input
from valid_inputs import movement
from error_messages import for_movement_instructions

# define function for checking plateau parameters
def plateau_checker(string_coordinate_list):
    if check_functions.coordinates_list_length(string_coordinate_list) == False:
        return False
    if check_functions.for_integer(string_coordinate_list) == False:
        return False
    integer_coordinate_list = convert_input.to_coordinates(string_coordinate_list)
    if check_functions.for_rectangular_plateau(integer_coordinate_list) == False:
        return False

# define function for checking rover parameters
def rover_checker(plateau, rover_coordinate_and_heading_list):
    if check_functions.for_integer(rover_coordinate_and_heading_list) == False:
        return False
    rover_integer_coordinates = convert_input.to_coordinates(rover_coordinate_and_heading_list)
    if check_functions.coordinates_list_length(rover_integer_coordinates) == False:
        return False
    if check_functions.for_staying_on_plateau(plateau, rover_integer_coordinates) == False:
        return False
    heading = convert_input.to_heading(rover_coordinate_and_heading_list)
    if check_functions.for_direction(heading) == False:
        return False

# define a function that checks for correct movement instructions input
def movement_checker(movement_instruction_list):
    movement_list = movement()
    for instruction in movement_instruction_list:
        if instruction not in movement_list:
            for_movement_instructions()
            return False
