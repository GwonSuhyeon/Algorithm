n, m = map(int, input().split())

white_start = [[1 if (i + k) % 2 == 0 else 0 for i in range(8)] for k in range(8)]
black_start = [[0 if (i + k) % 2 == 0 else 1 for i in range(8)] for k in range(8)]

board = []

res = n * m

for _ in range(n):
    board.append([0 if i == 'W' else 1 for i in list(input())])

for col in range(0, (m - 8) + 1):
    for row in range(0, (n - 8) + 1):
        white_min = 0
        black_min = 0
        
        for i in range(8):
            white_min += sum([abs(a - b) for a, b in zip(board[row + i][col:col + 8], white_start[i])])
            black_min += sum([abs(a - b) for a, b in zip(board[row + i][col:col + 8], black_start[i])])
        
        if white_min <= black_min and white_min < res:
            res = white_min
        
        elif black_min <= white_min and black_min < res:
            res = black_min

print(res)