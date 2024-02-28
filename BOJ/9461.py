t = int(input())

res = []

for _ in range(t):
    n = int(input())
    
    dp = [0 for _ in range(100 + 1)]
    
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2
    
    for i in range(6, n + 1):
        dp[i] = dp[i - 1] + dp[i - 5]
    
    res.append(dp[n])

for i in res:
    print(i)