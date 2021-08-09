# list for ascii of integers or spaces
def ascii_integer():
    ascii_integer_list = []
    for integer in range(48, 58):
        ascii_integer_list.append(integer)
    return ascii_integer_list

# list for 'N', 'S', 'E' and 'W'
def direction():
    direction_list = ['N', 'E', 'S', 'W']
    return direction_list

# list for 'L', 'R' or 'M'
def movement():
    movement_list = ['L', 'R', 'M', ' ']
    return movement_list
