import sys

N = int(input())

arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
res = sorted(arr, key=lambda x : (x[1], x[0]))

for x, y in res:
    print(x, y)