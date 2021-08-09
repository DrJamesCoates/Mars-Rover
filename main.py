from sys import exit
import user_inputs
from checkers import plateau_checker, rover_checker, movement_checker
import make
import move


# Prompt user for plateau top right corner coordinates and create instance of mars plateau if checks passed
top_right_corner_coordinates_list =  user_inputs.for_top_right_corner()
if plateau_checker(top_right_corner_coordinates_list) == False:
    exit(1)
mars_plateau = make.plateau(top_right_corner_coordinates_list)

# create rover list
list_of_rovers = []
# Prompt user for the coordinates and direction facing of 3 rovers and create rover instance if checks passed
while len(list_of_rovers) < 3:    
    rover_position_and_heading_list = user_inputs.for_rover()
    if rover_checker(mars_plateau, rover_position_and_heading_list) == False:
        exit(2)
    rover = make.rover(rover_position_and_heading_list)

    # Prompt user for rover movement instruction
    rover_movement_instruction = user_inputs.for_rover_movement()
    if movement_checker(rover_movement_instruction) == False:
        exit(3)
    
    # move rover according to movement instructions
    move.rover(mars_plateau, rover, rover_movement_instruction)
    list_of_rovers.append(rover)

# print rover position and heading
for rover in list_of_rovers:
    print(rover.x, rover.y, rover.heading)

exit(0)
    