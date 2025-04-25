n, d = map(int, input().split())

solved = []

for _ in range(n):
    solved.append(int(input()))

reward = d // sum(solved)

for i in solved:
    print(reward * i)