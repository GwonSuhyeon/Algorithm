num1, num2 = map(int, input().split())

a = (num1 + num2) // 2
b = (num1 - num2) // 2

if a < 0 or b < 0:
    print(-1)
elif (num1 + num2) % 2 != 0 or (num1 - num2) % 2 != 0:
    print(-1)
elif num1 < num2:
    print(-1)
else:
    print(max(a, b), min(a, b))