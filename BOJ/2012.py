import sys

input = sys.stdin.readline

N = int(input().rstrip())

arr = []

res = 0

for _ in range(N):
    arr.append(int(input().rstrip()))

arr = sorted(arr)

for idx, i in enumerate(arr):
    if i == (idx + 1):
        continue
    
    res += abs(i - (idx + 1))

print(res)