scores = []

for _ in range(10):
    scores.append(int(input()))

res = 0

for score in scores:
    if res + score >= 100:
        if abs(100 - (res + score)) <= abs(100 - res):
            res += score
        
        break

    res += score

print(res)