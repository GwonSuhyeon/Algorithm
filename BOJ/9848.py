n, k = map(int, input().split())

pre = 0
res = 0

for i in range(n):
    t = int(input())
    
    if i > 0:
        if pre - t >= k:
            res += 1
        
    pre = t

print(res)