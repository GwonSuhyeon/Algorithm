N, W, H = map(int, input().split())

for _ in range(N):
    l = int(input())
    
    if l <= W or l <= H or l**2 <= (W**2 + H**2):
        print('YES')
    
    else:
        print('NO')