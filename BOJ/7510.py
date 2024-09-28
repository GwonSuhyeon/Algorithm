import math


T = int(input())

for i in range(1, T + 1):
    a, b, c = map(int, input().split())

    print(f'Scenario #{i}:')

    if int(math.sqrt((a**2 + b**2 + c**2) - max(a, b, c)**2)) == max(a, b, c):
        print('yes')
    else:
        print('no')
    
    if i < T:
        print()