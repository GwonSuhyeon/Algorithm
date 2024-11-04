N = int(input())

res = 0

for _ in range(N):
    line  = input()

    for i in line:
        if i == 'A':
            res += 4
        elif i == 'K':
            res += 3
        elif i == 'Q':
            res += 2
        elif i == 'J':
            res += 1

print(res)