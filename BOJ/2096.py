import sys


N = int(sys.stdin.readline().rstrip())

dp = [[0 for _ in range(3)] for _ in range(2)]

for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    
    dp[0] = [a + max(dp[0][0], dp[0][1]), b + max(dp[0][0], dp[0][1], dp[0][2]), c + max(dp[0][1], dp[0][2])]
    dp[1] = [a + min(dp[1][0], dp[1][1]), b + min(dp[1][0], dp[1][1], dp[1][2]), c + min(dp[1][1], dp[1][2])]

print(max(dp[0]), min(dp[1]))