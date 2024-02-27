t = int(input())

dp = [[0, 0] for _ in range(40 + 1)]
dp[0] = [1, 0]
dp[1] = [0, 1]
dp[2] = [1, 1]

res = []

for i in range(3, 40 + 1):
    dp[i] = [dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1]]

for _ in range(t):
    n = int(input())
    
    res.append(dp[n])

for a, b in res:
    print(f'{a} {b}')