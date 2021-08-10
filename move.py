from check_functions import for_staying_on_plateau
from error_messages import for_stopping_rover

def rover(plateau, rover, movement_instruction_string):
    for instruction in movement_instruction_string:
        if instruction == 'M':
            rover.move_forward()
        elif instruction == 'L' or instruction == 'R':
            rover.turn(instruction)
        rover_coordinates_list = [rover.x, rover.y]
        if for_staying_on_plateau(plateau, rover_coordinates_list) == False:
            for_stopping_rover()
            return
