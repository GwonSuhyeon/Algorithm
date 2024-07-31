N = int(input())

A = []
B = []

res = 0

for _ in range(N):
    A.append(input())

for _ in range(N):
    B.append(input())

for a, b in zip(A, B):
    if a == b:
        res += 1

print(res)