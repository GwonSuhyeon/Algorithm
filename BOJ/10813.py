N, M = map(int, input().split())

ball = [i + 1 for i in range(N)]

for _ in range(M):
    i, j = map(int, input().split())
    
    if i != j:
        temp = ball[i - 1]
        ball[i - 1] = ball[j - 1]
        ball[j - 1] = temp

print(*ball)