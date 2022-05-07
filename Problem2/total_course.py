import numpy as np

def part1():
    # get total course using the input
    position_total = 0
    depth_total = 0
    with open('input.txt') as f:
        directions = f.readlines()
        # parse each line into the word then the number (each element looks like ['forward', '4'])
        directions = [direction.split() for direction in directions]
        # convert to numpy array
        directions = np.array(directions)

        # split array into two arrays: horizontal and vertical
        forward_indices = [direction[0] == "forward" for direction in directions]
        depth_indices = ~(np.array(forward_indices))
        forwards = directions[forward_indices]
        depths = directions[depth_indices]
        # for horizontal, sum the second element of each array
        position_total = sum(forwards[:,1].astype(int))
        depth_total = sum(depths[np.where(depths=='down')[0],1].astype(int)) - sum(depths[np.where(depths=='up')[0],1].astype(int))

    # multiply position and depth
    total_movement = depth_total * position_total
    print(total_movement)


def part2():
    position_total = 0
    depth_total = 0
    aim = 0
    with open('input.txt') as f:
        directions = f.readlines()
        # parse each line into the word then the number (each element looks like ['forward', '4'])
        directions = [direction.split() for direction in directions]
        # convert to numpy array
        directions = np.array(directions)

        # split array into two arrays: horizontal and vertical
        forward_indices = [direction[0] == "forward" for direction in directions]
        forwards = directions[forward_indices]
        # for horizontal, sum the second element of each array
        position_total = sum(forwards[:,1].astype(int))

        for direction in directions:
            value = int(direction[1])
            if direction[0] == "forward":
                depth_total += aim*value
            elif direction[0] == "up":
                aim -= value
            else: 
                aim += value

        # depth_indices = ~(np.array(forward_indices))
        # depths = directions[depth_indices]
        # downs = depths[np.where(depths=='down')[0],1].astype(int)
        # ups = depths[np.where(depths=='up')[0],1].astype(int)
        # # current aim should be a sum of all the previous depth numbers
        # aim = 0
        # aims = np.array([0])
        # for up, down in zip(ups, downs):
        #     aim += down

        


    # multiply position and depth
    total_movement = depth_total * position_total
    print(total_movement)        



if __name__ == "__main__":
    part2()