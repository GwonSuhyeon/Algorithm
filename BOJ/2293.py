import sys


N, K = map(int, sys.stdin.readline().rstrip().split())

dp = [0 for _ in range(K + 1)]
dp[0] = 1

arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))

arr = sorted(arr)

for i in arr:
    for j in range(i, K + 1):
        dp[j] += dp[j - i]

print(dp[K])