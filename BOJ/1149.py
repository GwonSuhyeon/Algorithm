N = int(input())

cost = [[]]

dp = [[0, 0, 0] for _ in range(N + 1)]

for i in range(1, N + 1):
    arr = list(map(int, input().split()))
    cost.append(arr)

dp[1][0] = cost[1][0]
dp[1][1] = cost[1][1]
dp[1][2] = cost[1][2]

for i in range(2, N + 1):
    dp[i][0] = min(dp[i - 1][1] + cost[i][0], dp[i - 1][2] + cost[i][0])
    dp[i][1] = min(dp[i - 1][0] + cost[i][1], dp[i - 1][2] + cost[i][1])
    dp[i][2] = min(dp[i - 1][0] + cost[i][2], dp[i - 1][1] + cost[i][2])

print(min(dp[N][0], dp[N][1], dp[N][2]))