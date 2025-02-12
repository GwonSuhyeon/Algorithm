from collections import deque


def bfs(row, col, viewing):
    global res

    bfs_q = deque()
    bfs_q.append([row, col, viewing])

    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    while len(bfs_q):
        r, c, v = bfs_q.popleft()

        if room[r][c] == 0:
            room[r][c] = -1
            res += 1
        
        isClean = True
        
        for y, x in direction:
            new_row, new_col = r + y, c + x

            if 0 <= new_row < N and 0 <= new_col < M:
                if room[new_row][new_col] == 0:
                    isClean = False
                    break
        
        if isClean == True:
            y, x = robot_move[v][0]

            new_row, new_col = r + y, c + x

            if new_row < 0 or new_row >= N or new_col < 0 or new_col >= M:
                break
            
            if room[new_row][new_col] == 1:
                break
            
            bfs_q.append([new_row, new_col, v])
        else:
            while True:
                if v == 0:
                    v = 3
                elif v == 1:
                    v = 0
                elif v == 2:
                    v = 1
                elif v == 3:
                    v = 2
                
                y, x = robot_move[v][1]

                new_row, new_col = r + y, c + x

                if room[new_row][new_col] == 0:
                    bfs_q.append([new_row, new_col, v])
                    break


N, M = map(int, input().split())
r, c, v = map(int, input().split())

room = []
res = 0

robot_move = {
    0: [[1, 0], [-1, 0]],
    1: [[0, -1], [0, 1]],
    2: [[-1, 0], [1, 0]],
    3: [[0, 1], [0, -1]]
}

for _ in range(N):
    room.append(list(map(int, input().split())))

bfs(r, c, v)

print(res)