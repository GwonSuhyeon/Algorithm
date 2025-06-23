arr = list(map(int, input().split()))

piece = [1, 1, 2, 2, 2, 8]

for i, j in zip(piece, arr):
    if i > j:
        print(i - j, end=' ')
    else:
        print(i - j, end=' ')