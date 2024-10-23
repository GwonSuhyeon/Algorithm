T = int(input())

direction = [[-1, 2], [-1, -2], [1, 2], [1, -2], [-2, 1], [-2, -1], [2, 1], [2, -1]]

for i in range(1, T + 1):
    n, r1, c1, r2, c2 = map(int, input().split())

    knight = False

    for x, y in direction:
        if (r1 + x) == r2 and (c1 + y) == c2:
            knight = True
            break
    
    if knight == True:
        print(f'Case {i}: YES')
    else:
        print(f'Case {i}: NO')