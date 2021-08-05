import convert_input

# function for getting top right coordinates input from user
def for_top_right_corner():
    top_right_corner_coordinates = input("What are your coordinates for the top right corner (x and y coordinates)? ")
    coordinates_list = convert_input.to_list(top_right_corner_coordinates)
    return coordinates_list


# function for getting rover coordinates input and direction facing from user
def for_rover():
    rover_coordinates_and_direction = input("What are the rover's coordinates and direction facing (x coordinate y coordinate direction)? ")
    rover_coordinates_and_direction_list = convert_input.to_list(rover_coordinates_and_direction)
    return rover_coordinates_and_direction_list

# function for getting rover movement input from user
def for_rover_movement():
    rover_movement_instructions = ""
    rover_movement_instructions_string = input("What are your movement instructions for the rover? ").upper()
    rover_movement_instructions_list = convert_input.to_list(rover_movement_instructions_string)
    for movement_instruction in rover_movement_instructions_list:
        rover_movement_instructions += movement_instruction
    return rover_movement_instructions

    