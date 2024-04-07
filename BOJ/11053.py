import sys


N = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [0 for _ in range(N)]

for i in range(N):
    dp[i] = 1
    
    for k in range(i):
        if arr[k] < arr[i]:
            dp[i] = max(dp[i], dp[k] + 1)

print(max(dp))