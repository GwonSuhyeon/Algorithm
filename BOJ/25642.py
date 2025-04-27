yt, yj = map(int, input().split())

attack = 'yt'

while True:
    if attack == 'yt':
        yj += yt
        attack = 'yj'
    else:
        yt += yj
        attack = 'yt'
    
    if yt >= 5:
        print('yj')
        break
    elif yj >= 5:
        print('yt')
        break