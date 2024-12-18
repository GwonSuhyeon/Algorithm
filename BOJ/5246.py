from collections import defaultdict


Board = int(input())

for _ in range(Board):
    line = input()

    res = defaultdict(int)

    piece = line[0]

    position = list(map(int, line[2:].split()))

    for i in range(0, len(position), 2):
        col, row = position[i], position[i + 1]

        res[row] += 1
    
    print(max(res.values()))