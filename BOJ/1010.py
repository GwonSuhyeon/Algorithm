import math

t = int(input())

res = []

for _ in range(t):
    
    n, m = map(int, input().split())
    
    res.append(int(math.factorial(m) / (math.factorial(n) * math.factorial(m - n))))
    

for i in res:
    print(i)