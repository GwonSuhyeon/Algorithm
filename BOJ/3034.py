import math


N, W, H = map(int, input().split())

for _ in range(N):
    length = int(input())
    
    if length <= W or length <= H or length <= math.sqrt(W**2 + H**2):
        print('DA')
    else:
        print('NE')