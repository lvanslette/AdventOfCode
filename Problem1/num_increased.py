with open('input.txt') as f:
    measurements = f.readlines()
    prev_distance = -1
    increased = 0
    for distance in measurements:
        
        if int(distance) > prev_distance and prev_distance != -1:
            increased +=1
        prev_distance = int(distance)
        

    print(increased)
        