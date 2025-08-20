N = int(input())
B = list(map(int, input().split()))

A = []

for idx, i in enumerate(B):
    a = i * (idx + 1) - sum(A[:idx])
    A.append(a)

print(*A)