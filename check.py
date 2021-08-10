import valid_inputs

# define classes for checking correct input
# define a parent class with a common check for different children classes
class Global_checks:
    def for_integer(self, coordinate_string):
        valid_integer_list = valid_inputs.integer()
        for character in coordinate_string:
            if int(character) not in valid_integer_list:
                print("Incorrect coordinate input: x and y coordinates must be positive integers.")
                return False

# define child class of Global_checks for plateau
class Checker_for_plateau(Global_checks):
    def for_top_right_coordinates_list_length(self, coordinates_list):
        if len(coordinates_list) != 2:
            print("Incorrect coordinates input: exactly one coordinate for x and one coordinate for y is reqiured.")
            return False
    
    def for_rectangular_plateau(self, coordinates_list):
        if coordinates_list[0] == 0 or coordinates_list[1] == 0:
            print("Incorrect coordinates input: x and y coordinates must be greater than 0.")
            return False
        elif coordinates_list[0] == coordinates_list[1]:
            print("Incorrect coordinates input: plateau must be a rectangle (x and y coordinates cannot be equal).")
            return False

# define child class of Global_checks for rover    
class Checker_for_rover(Global_checks):
    def for_rover_input_list_length(self, coordinates_heading_list):
        if len(coordinates_heading_list) != 3:
            return False

    def for_direction(self, direction):
        if len(direction) != 1:
            print("Incorrect rover direction input: rover direction must be specified with one character.")
            return False
        direction_list = valid_inputs.direction()
        if direction not in direction_list:
            print("Incorrect rover direction input: rover direction input must be one of N, S, E or W.")
            return False
        
    def for_staying_on_plateau(self, plateau_coordinates, rover):
        if rover.x > plateau_coordinates.x and rover.y > plateau_coordinates.y:
            print("Fatal error: rover went out of the plateau boundary on both the x axis and the y axis.")
            return False
        elif rover.x > plateau_coordinates.x:
            print("Fatal error: rover went out of the plateau boundary on the x axis.")
            return False
        elif rover.y > plateau_coordinates.y:
            print("Fatal error: rover went out of the plateau boundary on the y axis.")
            return False

# define class for checking movement
class Checker_for_movement:
    def for_correct_movement_instructions(self, movement_instruction_string):
        movement_list = valid_inputs.movement()
        for character in movement_instruction_string:
            if character not in movement_list:
                print("Incorrect movement instruction for rover: must be one of L/R/M.")
                return False

    