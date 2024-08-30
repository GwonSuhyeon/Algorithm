std_score = list(map(int, input().split()))

max_score = [100, 100, 200, 200, 300, 300, 400, 400, 500]

res = 'draw'

if sum(std_score) < 100:
    res = 'none'
else:
    for a, b in zip(std_score, max_score):
        if a > b:
            res = 'hacker'
            break

print(res)