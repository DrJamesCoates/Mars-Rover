from sys import exit
import user_inputs
from check import Checker_for_plateau, Checker_for_rover, Checker_for_movement
import convert_input
from move import mover
from object_classes import Plateau, Rover


# create instance of plateau checker object
plateau_checker = Checker_for_plateau()
# Prompt user for plateau top right corner coordinates and create instance of mars plateau if checks passed
top_right_corner_coordinates_list =  user_inputs.for_top_right_corner()
if plateau_checker.for_top_right_coordinates_list_length(top_right_corner_coordinates_list) == False:
    exit(1)
for coordinate_position in range(len(top_right_corner_coordinates_list)):
    if plateau_checker.for_integer(top_right_corner_coordinates_list[coordinate_position]) == False:
        exit(2)
    top_right_corner_coordinates_list[coordinate_position] = convert_input.to_integer(top_right_corner_coordinates_list[coordinate_position])
if plateau_checker.for_rectangular_plateau(top_right_corner_coordinates_list) == False:
    exit(3)
mars_plateau = Plateau(top_right_corner_coordinates_list[0], top_right_corner_coordinates_list[1])


# create instance of rover checker class
rover_checker = Checker_for_rover()
# create instance of movement checker class
movement_checker = Checker_for_movement()
# create rover list
list_of_rovers = []
# Prompt user for the coordinates and direction facing of 3 rovers and create rover instance if checks passed
while len(list_of_rovers) < 3:    
    rover_position_and_heading_list = user_inputs.for_rover()
    if rover_checker.for_rover_input_list_length(rover_position_and_heading_list) == False:
        exit(4)
    if rover_checker.for_integer(rover_position_and_heading_list[0]) == False or rover_checker.for_integer(rover_position_and_heading_list[1]) == False:
        exit(5)
    
    rover_x_coordinate = convert_input.to_integer(rover_position_and_heading_list[0])
    rover_y_coordinate = convert_input.to_integer(rover_position_and_heading_list[1])
    rover_heading = rover_position_and_heading_list[2].upper()
    if rover_checker.for_direction(rover_heading) == False:
        exit(6)
    
    rover = Rover(rover_x_coordinate, rover_y_coordinate, rover_heading)
    if rover_checker.for_staying_on_plateau(mars_plateau, rover) == False:
        exit(7)

    # Prompt user for rover movement instruction
    rover_movement_instruction = user_inputs.for_rover_movement()
    if movement_checker.for_correct_movement_instructions(rover_movement_instruction) == False:
        exit(8)
    
    # move rover according to movement instructions
    mover(mars_plateau, rover, rover_movement_instruction)
    list_of_rovers.append(rover)


for rover in list_of_rovers:
    print(rover.x, rover.y, rover.heading)

exit(0)
    
