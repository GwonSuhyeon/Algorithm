N, a, b = map(int, input().split())

room = []
res = 'HAPPY'

for _ in range(N):
    room.append(list(map(int, input().split())))

for i in range(N):
    if i != (b - 1) and room[a - 1][i] > room[a - 1][b - 1]:
        res = 'ANGRY'
        break
    
    if i != (a - 1) and room[i][b - 1] > room[a - 1][b - 1]:
        res = 'ANGRY'
        break

print(res)