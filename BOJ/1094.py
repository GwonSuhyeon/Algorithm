x = int(input())

length = [64, 32, 16, 8, 4, 2, 1]

res = 0
stick = 0

for i in length:
    if (stick + i) <= x:
        stick += i
        res += 1

print(res)