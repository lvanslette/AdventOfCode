def part1():
    with open('input.txt') as f:
        measurements = f.readlines()
        measurements = [int(i) for i in measurements]
        increased = [i < j for i,j in zip(measurements, measurements[1:])]
        num_increased = sum(increased)
        print(num_increased)

def part2():
    with open('input.txt') as f:
        measurements = f.readlines()
        measurements = [int(i) for i in measurements]
        increased = [((i+j+k) < (j+k+l)) for i,j,k,l in zip(measurements, measurements[1:], measurements[2:], measurements[3:])]
        num_increased = sum(increased)
        print(num_increased)

if __name__ == "__main__":
    part2()
            