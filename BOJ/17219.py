import sys

n, m = map(int, input().split())

memo = {}

res = []

for _ in range(n):
    s = sys.stdin.readline().rstrip().split()
    
    memo[s[0]] = s[1]

for _ in range(m):
    s = sys.stdin.readline().rstrip()
    
    res.append(memo[s])

for i in res:
    print(i)