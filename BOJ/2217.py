n = int(input())

weight = []

max = 0
res = 0

for _ in range(n):
    weight.append(int(input()))

weight = sorted(weight)

for idx, i in enumerate(weight[::-1]):
    cnt = idx + 1
    max = i * cnt
    
    if max > res:
        res = max

print(res)