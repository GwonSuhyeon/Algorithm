n = int(input())

minimum = 3

while True:
    if (minimum - 2)**2 >= n:
        break
    
    minimum += 1

for i in range(minimum):
    if i == 0 or i == (minimum - 1):
        print('x' * minimum)
    else:
        print('x', end='')
        print('.' * (minimum - 2), end='')
        print('x')