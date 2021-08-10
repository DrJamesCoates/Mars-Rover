import convert_input
from check_functions import for_input

# function for getting top right coordinates input from user
def for_top_right_corner():
    while True:
        top_right_corner_coordinates = input("What are your coordinates for the top right corner (x and y coordinates)? ")
        if for_input(top_right_corner_coordinates) == True:
            break
    coordinates_list = convert_input.to_list(top_right_corner_coordinates)
    return coordinates_list


# function for getting rover coordinates input and direction facing from user
def for_rover():
    while True:
        rover_coordinates_and_direction = input("What are the rover's coordinates and direction facing (x coordinate y coordinate direction)? ")
        if for_input(rover_coordinates_and_direction) == True:
            break
    rover_coordinates_and_direction_list = convert_input.to_list(rover_coordinates_and_direction)
    return rover_coordinates_and_direction_list

# function for getting rover movement input from user
def for_rover_movement():
    while True:
        rover_movement_instructions = input("What are your movement instructions for the rover? ")
        if for_input(rover_movement_instructions) == True:
            rover_movement_instructions = rover_movement_instructions.upper()
            break
    return rover_movement_instructions
