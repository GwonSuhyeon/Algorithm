a = int(input())
b = int(input())
c = int(input())

if a == 60 and b == 60 and c == 60:
    print('Equilateral')
elif sum([a, b, c]) == 180:
    if len(set([a, b, c])) == 2:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')