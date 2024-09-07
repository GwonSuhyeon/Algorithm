N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = set(list(map(int, input().split())))

res = 0

for a in A:
    res += a

    if res in B:
        res = 0

print(res)