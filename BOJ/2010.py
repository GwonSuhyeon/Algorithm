import sys

input = sys.stdin.readline

N = int(input().rstrip())

res = 0

for i in range(N):
    num = int(input().rstrip())

    if i < (N - 1):
        res += (num - 1)
    else:
        res += num

print(res)