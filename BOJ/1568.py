N = int(input())

res = 0
k = 1

while N > 0:
    if N < k:
        k = 1
    
    N -= k
    k += 1
    
    res += 1

print(res)