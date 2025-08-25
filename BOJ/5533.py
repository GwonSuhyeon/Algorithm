N = int(input())

scores = []

for _ in range(N):
    scores.append(list(map(int, input().split())))

scores_T = list(map(list, zip(*scores)))

res = [0 for _ in range(N)]

for arr in scores_T:
    for idx, i in enumerate(arr):
        if arr.count(i) == 1:
            res[idx] += i

for value in res:
    print(value)