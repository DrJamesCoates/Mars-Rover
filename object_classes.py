# define class for plateau
class Plateau:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# define class for rover
class Rover:
    def __init__(self, x, y, heading):
        self.x = x
        self.y = y
        self.heading = heading

    def move_forward(self):
        change_in_rover_position = {'N': 1, 'S': -1, 'E': 1, 'W': -1}
        if self.heading == 'N' or self.heading == 'S':
            self.y += change_in_rover_position[self.heading]
        elif self.heading == 'E' or self.heading == 'W':
            self.x += change_in_rover_position[self.heading]
    
    def turn_left(self):
        rover_heading_positions = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
        direction_list = ['N', 'E', 'S', 'W']
        rover_heading_position_in_direction_list = rover_heading_positions[self.heading]
        if rover_heading_positions[self.heading] == 0:
            self.heading = direction_list[3]
        else:
            rover_heading_position_in_direction_list -= 1
            self.heading = direction_list[rover_heading_position_in_direction_list]
    
    def turn_right(self):
        rover_heading_positions = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
        direction_list = ['N', 'E', 'S', 'W']
        rover_heading_position_in_direction_list = rover_heading_positions[self.heading]
        if rover_heading_position_in_direction_list == 3:
            self.heading = direction_list[0]
        else:
            rover_heading_position_in_direction_list += 1
            self.heading = direction_list[rover_heading_position_in_direction_list]
        