N = int(input())

res = 0

for _ in range(N):
    line = int(input())
    
    if line != 1:
        res += 1

print(res)