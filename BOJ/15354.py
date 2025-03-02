N = int(input())

res = 0
color = ''

for _ in range(N):
    c = input()

    if color != c:
        color = c
        res += 1

res += 1

print(res)