from collections import deque


def bfs(A, B):
    bfs_q = deque()
    visited = [0 for _ in range(10000)]
    
    bfs_q.append([A, 0])
    visited[A] = 1
    
    while len(bfs_q):
        number, cnt = bfs_q.popleft()
        if number == B:
            return cnt
        
        for i in range(4):
            for k in range(10):
                if i == 0 and k == 0:
                    continue
                
                str_number = list(str(number))

                if str(k) == str_number[i]:
                    continue
                
                str_number[i] = str(k)
                temp = int(''.join(str_number))
                
                if visited[temp] == 1:
                    continue

                if et[temp] == 0:
                    bfs_q.append([temp, cnt + 1])
                
                visited[temp] = 1
    
    return -1

T = int(input())

et = [0 for _ in range(10000)]
et[1] = 1
for i in range(2, 10000):
    if et[i] == 1:
        continue
    
    for k in range(i * 2, 10000, i):
        et[k] = 1

for _ in range(T):
    A, B = map(int, input().split())
    
    res = bfs(A, B)
    
    if res > -1:
        print(res)
    
    else:
        print('Impossible')