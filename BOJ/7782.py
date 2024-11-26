n = int(input())
b1, b2 = map(int, input().split())

res = 'No'

for _ in range(n):
    lx, ly, hx, hy = map(int, input().split())

    if lx <= b1 <= hx and ly <= b2 <= hy:
        res = 'Yes'

print(res)