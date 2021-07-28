# import necessary libraries
import sys


def main():
    # make rover class
    class Rover:
        def __init__(self, x, y, compass):
            self.x = x
            self.y = y
            self.compass = compass
    
    # list for instances of class rover and their final positions
    rover_end_pos = []

    # constant variable for number of rovers
    rover_numbers = 3
    
    # get top right corner (t_r_c) position input from user
    t_r_c = input('Coordinates for the top right hand corner of the plateau ("x-coordinate" followed by a space " " followed by "y-coordinate"): ')
    # strip the input of extra whitespace and split each coordinate by whitespace
    t_r_c_coords = t_r_c.strip().split()
    #check correct coordinates input for x and y
    while t_r_c_check(t_r_c_coords) == False:
        t_r_c = input('Coordinates for the top right hand corner of the plateau ("x-coordinate" followed by a space " " followed by "y-coordinate"): ')
        t_r_c_coords = t_r_c.strip().split()

    # convert coordinates into integers
    for j in range(2):
        t_r_c_coords[j] = int(t_r_c_coords[j])

    # for each rover
    for i in range(rover_numbers):
        # get rover's position
        position = input(f'What is Rover{i + 1} position? (x-coordinate y-coordinate rover-direction) ')
        position_ls = position.strip().split()
        # check rover is positioned on plateau
        while check_position(position_ls, t_r_c_coords[0], t_r_c_coords[1]) == False:
            position = input(f'What is Rover{i + 1} position? (x-coordinate y-coordinate rover-direction) ')
            position_ls = position.strip().split()

        # make an instance of a rover
        rover = Rover(int(position_ls[0]), int(position_ls[1]), position_ls[2].upper())

        # define string var for movement
        movement = ' '
        # adjust rover position with movement inputs
        while move_rover(rover, movement, t_r_c_coords) == False:
            # change rover position coords and direction to start values
            rover = Rover(int(position_ls[0]), int(position_ls[1]), position_ls[2].upper())
            # get movement input from user
            movement = input(f'What are your movement instructions for Rover{i + 1}? ')
            movement.strip()
            # check correct input for movement
            while check_movement(movement) == False:
                movement = input(f'What are your movement instructions for Rover{i + 1}? ')
                movement = movement.strip()

        # append new rover position to rover position list
        append_rover_list(rover, rover_end_pos)
    
    # Print the final positions of each rover
    for i in range(len(rover_end_pos)):
        print(f'Rover{i + 1}: {rover_end_pos[i].x} {rover_end_pos[i].y} ' + rover_end_pos[i].compass)
    


def t_r_c_check(a):
    # check more than 1 value inputted but not more than 2
    if len(a) == 0 or len(a) > 2:
        print("Incorrect input: inputs must only include a value for x and y coordinates respectively.")
        return False
    # check both values for trc are greater than zero
    if a[0] == '0':
        if a[1] == '0':
            print('Error: Plateau has no width in x and y axis.')
        else:
            print('Error: Plateau has no width in x axis')
        return False
    elif a[1] == '0':
        print('Error: Plateau has no width in y axis.')
        return False
    # iterate through each item in list
    for i in a:
        # iterate through each char of item
        for j in i:
            # convert to ascii - ints are 48 - 57 inclusive
            j = ord(j)
            # check char is an integer between 0 - 9
            if j > 57 or j < 48:
                print('Incorrect input: inputs must be a positive integer.')
                return False
            else:
                j = chr(j)

    # Check plateau is rectangular
    if int(a[0]) == int(a[1]):
        print('Input error: Plateau is rectangular (x and y coordinates cannot be equal).')
        return False



def check_position(p, x, y):
    # check 3 separate values were inputted
    if len(p) != 3:
        print('Incorrect rover position input.')
        return False
    # create list of appropriate direction inputs
    direction_ls = ['N', 'E', 'S', 'W']
    # iterate through the list
    for i in range(len(p)):
        # iterate through the chars of each list item
        for j in p[i]:
            # check if we're dealing with coordinates or direction
            if i < 2:
                # check if char is an int between 0 and 9
                if ord(j) > 57 or ord(j) < 48:
                    if i == 0:
                        print('Rover x coordinate must be a positive integer.')
                    elif i == 1:
                        print('Rover y coordinate must be a positive integer.')
                    return False
            else:
                # check direction is only one letter
                if len(p[i]) != 1:
                    print('Incorrect rover position input: direction must be specified with one letter.')
                    return False
                # check input is either one of N, E, S or W
                if j.upper() in direction_ls:
                    # check rover position is in boundary of plateau
                    if int(p[0]) > x:
                        if int(p[1]) > y:
                            print('Rover exceeds plateau boundary on both the x axis and y axis.')
                            return False
                        else:
                            print('Rover exceeds plateau boundary on x axis.')
                            return False
                    if int(p[1]) > y:
                        print('Rover exceeds plateau boundary on y axis.')
                        return False
                else:
                    print("Incorrect rover postion input: direction must be specified with either one of N/E/S/W.")
                    return False
    


def check_movement(m):
    # make list of appropriate inputs for movement command
    m_ls = ['M', 'L', 'R']

    # check correct input for movement
    for i in m:
        if i.upper() in m_ls:
            pass
        else:
            print("Incorrect input for rover movement command.")
            return False



def move_rover(r, mv, coord):
    # iterate through the movement string command
    for i in mv:
        # for moving forward
        if i.upper() == 'M':
            if r.compass == 'N':
                r.y += 1
            elif r.compass == 'E':
                r.x += 1
            elif r.compass == 'S':
                r.y -= 1
            else:
                r.x -= 1
        # for turning left
        elif i.upper() == 'L':
            if r.compass == 'N':
                r.compass = 'W'
            elif r.compass == 'E':
                r.compass = 'N'
            elif r.compass == 'S':
                r.compass = 'E'
            else:
                r.compass = 'S'
        # for turning right
        elif i.upper() == 'R':
            if r.compass == 'N':
                r.compass = 'E'
            elif r.compass == 'E':
                r.compass = 'S'
            elif r.compass == 'S':
                r.compass = 'W'
            else:
                r.compass = 'N'
        else:
            return False
    # check rover is on plateau
    if safety(r, coord) == False:
            return False
    
    return True



def safety(r, c):
    # check if x coordinate is less than zero or greater than the upper limit for x
    if r.x < 0 or r.x > c[0]:
        print('Error: rover went out of plateau boundary on x axis. DANGER!!!CAUTION!!')
        return False
    # check if y coordinate is less than zero or greater than the upper limit for y
    elif r.y < 0 or r.y > c[1]:
        print('Error: rover went out of plateau boundary on y axis. DANGER!!!CAUTION!!')
        return False



def append_rover_list(r, p):
    p.append(r)
    return



main()
