from check import Checker_for_rover

def mover(plateau, rover, movement_instruction_string):
    rover_checker = Checker_for_rover()
    for instruction in movement_instruction_string:
        if instruction == 'M':
            rover.move_forward()
        elif instruction == 'L':
            rover.turn_left()
        elif instruction == 'R':
            rover.turn_right()
        
        if rover_checker.for_staying_on_plateau(plateau, rover) == False:
            print("Rover movement stopped.")
            return
