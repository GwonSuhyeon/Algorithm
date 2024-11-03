X = int(input())
N = int(input())

res = X * N

for _ in range(N):
    P = int(input())
    
    res -= P

res += X

print(res)