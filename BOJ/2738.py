N, M = map(int, input().split())

A = []
B = []

for _ in range(N):
    A.append(list(map(int, input().split())))

for _ in range(N):
    B.append(list(map(int, input().split())))

for i in range(N):
    row1 = A[i]
    row2 = B[i]

    for a, b in zip(row1, row2):
        print(a + b, end=' ')
    print()