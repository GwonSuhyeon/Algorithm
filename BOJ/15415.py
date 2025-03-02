import sys


input = sys.stdin.readline

W = int(input().rstrip())
N = int(input().rstrip())

cake = 0

for _ in range(N):
    w, l = map(int, input().rstrip().split())

    cake += (w * l)

print(cake // W)