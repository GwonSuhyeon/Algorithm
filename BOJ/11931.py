import sys


input = sys.stdin.readline

N = int(input().rstrip())

arr = []

for _ in range(N):
    arr.append(int(input().rstrip()))

arr = sorted(arr, reverse=True)

for i in arr:
    print(i)