n = int(input())

a = sorted(map(int, input().split()))
b = list(map(int, input().split()))

res = 0

for minimum in a:
    maximum = max(b)
    b[b.index(maximum)] = -1
    
    res += (minimum * maximum)

print(res)