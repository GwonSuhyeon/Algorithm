P = int(input())

for _ in range(P):
    K, N = map(int, input().split())

    S1 = ((1 + N) * N) // 2
    S2 = N**2
    S3 = (N + 1) * N

    print(f'{K} {S1} {S2} {S3}')