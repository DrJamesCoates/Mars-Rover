import convert_input
from object_classes import Rover, Plateau

#function that makes and returns a plateau
def plateau(plateau_string_coordinates):
    plateau_integer_coordinates = convert_input.to_coordinates(plateau_string_coordinates)
    plateau = Plateau(plateau_integer_coordinates[0], plateau_integer_coordinates[1])
    return plateau

# function that makes and returns a rover
def rover(rover_coordinates_and_heading_list):
    rover_coordinates = convert_input.to_coordinates(rover_coordinates_and_heading_list)
    heading = convert_input.to_heading(rover_coordinates_and_heading_list)
    rover = Rover(rover_coordinates[0], rover_coordinates[1], heading)
    return rover
