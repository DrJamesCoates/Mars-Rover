import valid_inputs
import error_messages

# define a function that checks whether anything was inputted by user
def for_input(input_string):
    if len(input_string) == 0:
        error_messages.for_input_check()
        return False
    else:
        return True

# define a function that checks for integers in the coordinates input
def for_integer(coordinate_list):
    valid_ascii_integer_list = valid_inputs.ascii_integer()
    for coordinate in range(2):
        for character in str(coordinate_list[coordinate]):
            if ord(character) not in valid_ascii_integer_list:
                error_messages.for_integer_check()
                return False

# define a function that checks correct number of inputs for coordinates
def coordinates_list_length(coordinates_list):
    if len(coordinates_list) != 2:
        error_messages.for_coordinates_list_length()
        return False

# define a function that checks that the plateau is a rectangle
def for_rectangular_plateau(coordinates_list):
    if coordinates_list[0] == 0 or coordinates_list[1] == 0:
        error_messages.for_zero_coordinate()
        return False
    elif coordinates_list[0] == coordinates_list[1]:
        error_messages.for_square_plateau()
        return False

# define a function that checks only one input was given for rover heading and the input is a valid heading input
def for_direction(direction):
    if len(direction) != 1:
        error_messages.for_more_than_one_direction_input()
        return False
    direction_list = valid_inputs.direction()
    if direction not in direction_list:
        error_messages.for_incorrect_direction()
        return False

# define a function that checks that the rover is on the plateau
def for_staying_on_plateau(plateau, rover_coordinates_list):
    if rover_coordinates_list[0] > plateau.x and rover_coordinates_list[1] > plateau.y or rover_coordinates_list[0] < 0 and rover_coordinates_list[1] < 0:
        error_messages.for_x_and_y()
        return False
    elif rover_coordinates_list[0] > plateau.x or rover_coordinates_list[0] < 0:
        error_messages.for_x()
        return False
    elif rover_coordinates_list[1] > plateau.y or rover_coordinates_list[1] < 0:
        error_messages.for_y()
        return False
