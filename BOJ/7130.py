M, H = map(int, input().split())
N = int(input())

res = 0

for _ in range(N):
    C, B = map(int, input().split())

    res += max((M * C), (H * B))

print(res)