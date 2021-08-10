def for_input_check():
    print("Incorrect input: input cannot be absent.")

def for_integer_check():
    print("Incorrect coordinate input: x and y coordinates must be positive integers.")

def for_coordinates_list_length():
    print("Incorrect coordinates input: exactly one coordinate for x and one coordinate for y is reqiured.")

def for_zero_coordinate():
    print("Incorrect coordinates input: x and y coordinates must be greater than zero.")

def for_square_plateau():
    print("Incorrect coordinates input: plateau must be a rectangle (x and y coordinates cannot be equal).")

def for_more_than_one_direction_input():
    print("Incorrect rover direction input: rover direction must be specified with one character.")

def for_incorrect_direction():
    print("Incorrect rover direction input: rover direction input must be one of N, S, E or W.")

def for_x_and_y():
    print("Fatal error: rover went out of the plateau boundary on both the x axis and the y axis.")

def for_x():
    print("Fatal error: rover went out of the plateau boundary on the x axis.")

def for_y():
    print("Fatal error: rover went out of the plateau boundary on the y axis.")

def for_movement_instructions():
    print("Incorrect movement instruction for rover: must be one of L/R/M.")

def for_stopping_rover():
    print("Rover movement stopped.")
