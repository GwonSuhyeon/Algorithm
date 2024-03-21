N = int(input())

people = []
res = []

for i in range(N):
    people.append(list(map(int, input().split())))

for p in people:
    order = 1
    for i in range(N):
        if people[i][0] > p[0] and people[i][1] > p[1]:
            order += 1
    
    res.append(order)

for i in res:
    print(i, end=' ')