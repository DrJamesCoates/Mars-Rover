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

    def turn(self, direction):
        self.direction = direction
        direction_list = ['N', 'E', 'S', 'W', 'N']
        if direction == 'L':
            direction_list.reverse()
        rover_heading_position_in_direction_list = direction_list.index(self.heading) + 1
        self.heading = direction_list[rover_heading_position_in_direction_list]
