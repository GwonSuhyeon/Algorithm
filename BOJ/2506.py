N = int(input())
arr = list(map(int, input().split()))

res = 0
score = 1

for i in arr:
    if i == 1:
        res += score
        score += 1
    else:
        score = 1

print(res)