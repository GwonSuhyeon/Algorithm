n = int(input())

score = []
res = 0

for _ in range(n):
    score.append(int(input()))

while True:
    
    if len(score) == 1:
        break
    
    maximum = max(score[1:])
    
    if score[0] > maximum:
        break
    
    maximum_idx = (score[1:].index(maximum) + 1)
    
    score[0] += 1
    score[maximum_idx] -= 1
    
    res += 1

print(res)