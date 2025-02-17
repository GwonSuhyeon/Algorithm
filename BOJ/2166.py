n = int(input())

coord = []
res = 0

for _ in range(n):
    x, y = map(int, input().split())
    coord.append([x, y])

for i in range(len(coord)):
    if i < (len(coord) - 1):
        x_left = coord[i][0]
        y_left = coord[i + 1][1]
        x_right = coord[i + 1][0]
        y_right = coord[i][1]
    else:
        x_left = coord[i][0]
        y_left = coord[0][1]
        x_right = coord[0][0]
        y_right = coord[i][1]
    
    res += ((x_left * y_left) - (x_right * y_right))

print(abs(round(res / 2, 2)))