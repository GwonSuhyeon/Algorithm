H = input()
N = input()

idx = 0
res = 0

while True:
    if idx > len(H) - len(N):
        break
    
    if H[idx:idx + len(N)] == N:
        res += 1
        
        idx += len(N)
    else:
        idx += 1

print(res)