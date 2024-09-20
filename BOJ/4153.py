import math


while True:
    a, b, c = map(int, input().split())

    sum = 0

    if a == 0 and b == 0 and c == 0:
        break

    large = max(a, b, c)

    for i in [a, b, c]:
        if i == large:
            continue

        sum += i**2
    
    if int(math.sqrt(sum)) == large:
        print('right')
    else:
        print('wrong')