import math


cnt = 1

while True:
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        break
    
    if a == -1:
        if c**2 <= b**2:
            print(f'Triangle #{cnt}')
            print('Impossible.', end='\n\n')
        else:
            print(f'Triangle #{cnt}')
            print(f'a = {math.sqrt(c**2 - b**2):.3f}', end='\n\n')
    elif b == -1:
        if c**2 <= a**2:
            print(f'Triangle #{cnt}')
            print('Impossible.', end='\n\n')
        else:
            print(f'Triangle #{cnt}')
            print(f'b = {math.sqrt(c**2 - a**2):.3f}', end='\n\n')
    elif c == -1:
        print(f'Triangle #{cnt}')
        print(f'c = {math.sqrt(a**2 + b**2):.3f}', end='\n\n')
    
    cnt += 1