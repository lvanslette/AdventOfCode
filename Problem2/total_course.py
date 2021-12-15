import numpy as np

def part1():
    # get total course using the input
    position_total = 0
    depth_total = 0
    with open('input.txt') as f:
        directions = f.readlines()
        # convert to numpy array
        directions = np.array(directions)
        # parse each line into the word then the number
        directions = [direction.split() for direction in directions]
        # split array into two arrays: horizontal and vertical
        forward_indeces = [direction[0] == "forward" for direction in directions]
        depth_indeces = [direction[0] != "forward" for direction in directions]
        forwards = directions[forward_indeces]
        depths = directions[depth_indeces]
        # for horizontal, sum the second element of each array
        position_total = sum(int(forwards[:,1]))
        # for vertical, change the number to negative if the first element is down, then sum
        for depth in depths:
            if depth[0] == "down":
                depth[1] = -1*int(depth[1])
            depth_total += depth[1]
    # multiply position and depth
    total_movement = depth_total * position_total


#def part2():


if __name__ == "__main__":
    part1()