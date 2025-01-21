N = int(input())

res = 999999999

for _ in range(N):
    a, b = map(int, input().split())
    
    res = min(res, b // a)

print(res)