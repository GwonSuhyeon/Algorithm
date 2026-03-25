a, b = map(int, input().split())

num = (a * (100 - b)) / 100

if num < 100:
    print(1)
else:
    print(0)