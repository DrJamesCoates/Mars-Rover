# function to convert an inputted string into a list of string
def to_list(input_string):
    input_list = input_string.strip().split()
    return input_list

# function to convert coordinates in list to integers
def to_integer(coordinate):
    coordinate = int(coordinate)
    return coordinate