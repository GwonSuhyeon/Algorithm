import math


n = int(input())

for _ in range(n):
    m = int(input())

    P = []
    s_x = 0
    s_y = 0

    res = [0, 0, 999999]

    for i in range(m):
        line = input()

        for idx, k in enumerate(line):
            if k == 'p':
                P.append([i, idx])
            elif k == 's':
                s_x = i
                s_y = idx

    for p_x, p_y in P:
        dist = math.sqrt((s_x - p_x)**2 + (s_y - p_y)**2)

        if dist < res[-1]:
            res = [p_x, p_y, dist]
    
    print(f'({s_x},{s_y}):({res[0]},{res[1]}):{res[-1]:.2f}')