n, m = map(int, input().split())

res = 0

picture = [[0 for _ in range(100)] for _ in range(100)]

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
        
    for i in range(y1 - 1, y2):
        for k in range(x1 - 1, x2):
            picture[i][k] += 1

for p in picture:
    cnt = [0 for i in p if i > m]
    
    res += len(cnt)

print(res)