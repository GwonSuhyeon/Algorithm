import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

A = list(map(int, input().rstrip().split()))

res = 0
value = 0

for i in A:
    if i >= 0:
        value += i
    
    elif i < 0:
        value += i
        
        if value < 0:
            value = 0
    
    if value >= M:
        res += 1

print(res)