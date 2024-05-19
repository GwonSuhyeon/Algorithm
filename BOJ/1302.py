import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input().rstrip())

res = defaultdict(int)

for _ in range(N):
    book = input().rstrip()
    
    res[book] += 1

res = sorted(res.items(), key=lambda x : (-x[1], x[0]))

print(res[0][0])