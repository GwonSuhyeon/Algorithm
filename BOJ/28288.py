from collections import defaultdict


N = int(input())

res = defaultdict(int)
maximum = 0

for _ in range(N):
    days = input()

    for idx, d in enumerate(days):
        if d == 'Y':
            res[idx] += 1
            
            if res[idx] > maximum:
                maximum = res[idx]

arr = [key for key, value in res.items() if value == maximum]

for idx, i in enumerate(arr):
    if idx > 0:
        print(f',{i + 1}', end='')
    else:
        print(i + 1, end='')