import sys

n = int(sys.stdin.readline())

arr = [0 for i in range(10000)]

for i in range(n): 
    arr[int(sys.stdin.readline()) - 1] += 1

for idx, i in enumerate(arr):
    if i != 0:
        for _ in range(i):
            print(idx + 1)