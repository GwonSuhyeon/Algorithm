a, b, c, d = map(int, input().split())

num1 = a * b
num2 = c * d

if num1 > num2:
    print('M')
elif num1 < num2:
    print('P')
else:
    print('E')