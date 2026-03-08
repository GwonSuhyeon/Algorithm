N = int(input())
A = list(map(int, input().split()))
X, Y = map(int, input().split())

res1 = (N * X) // 100
res2 = 0

for i in A:
    if i >= Y:
        res2 += 1

print(res1, res2)