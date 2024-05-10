import sys
from collections import defaultdict


input = sys.stdin.readline

N = int(input().rstrip())

arr = defaultdict(int)

for _ in range(N):
    temp = input().rstrip().split('.')[-1]
    
    arr[temp] += 1

arr = sorted(arr.items())

for key, value in arr:
    print(key, value)