N = int(input())

res = 0
prev = None

for i in list(map(int, input().split())):
    if prev is None and i == 0:
        prev = 0
        res += 1
    elif prev == 0 and i == 1:
        prev = 1
        res += 1
    elif prev == 1 and i == 2:
        prev = 2
        res += 1
    elif prev == 2 and i == 0:
        prev = 0
        res += 1

print(res)