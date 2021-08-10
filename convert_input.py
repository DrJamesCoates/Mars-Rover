# function to convert an inputted string into a list of string
def to_list(input_string):
    input_list = input_string.strip().split()
    return input_list

# function that returns imput rover coordinates
def to_coordinates(coordinates_list):
    integer_coordinates_list = []
    for coordinate_postion in range(2):
        coordinate_integer = int(coordinates_list[coordinate_postion])
        integer_coordinates_list.append(coordinate_integer)
    return integer_coordinates_list

# function that returns input rover heading
def to_heading(coordinate_list):
    heading = coordinate_list[2].upper()
    return heading
