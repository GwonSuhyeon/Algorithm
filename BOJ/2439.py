n = int(input())

space = ' '
star = '*'

for i in range(n):
    print(space * (n - (i + 1)) + star * (i + 1))