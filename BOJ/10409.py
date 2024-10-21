n, T = map(int, input().split())

jobs = list(map(int, input().split()))

elapsed = 0
res = 0

for idx, job in enumerate(jobs):
    elapsed += job
    
    if elapsed > T:
        break
    
    res = idx + 1

print(res)