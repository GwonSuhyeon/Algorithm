A, B = map(int, input().split())

minimum = 1
res = 1

for _ in range(B):
    minimum += (A - 2)
    res += minimum
    
print(res)