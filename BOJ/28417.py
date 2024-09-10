import sys

input = sys.stdin.readline

N = int(input().rstrip())

res = []

for _ in range(N):
    arr = list(map(int, input().rstrip().split()))

    res.append(max(arr[:2]) + sum(sorted(arr[2:])[-2:]))

print(max(res))