while True:
    speed, weight, strength = map(float, input().split())

    if speed == 0 and weight == 0 and strength == 0:
        break
    
    position = []

    if weight >= 150 and strength >= 200 and speed <= 4.5:
        position.append('Wide Receiver')
    
    if weight >= 300 and strength >= 500 and speed <= 6.0:
        position.append('Lineman')
    
    if weight >= 200 and strength >= 300 and speed <= 5.0:
        position.append('Quarterback')
    
    if len(position) == 0:
        print('No positions')
    else:
        for i in position:
            print(i, end=' ')
        print()