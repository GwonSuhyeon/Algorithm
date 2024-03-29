t = int(input())

res = []

for _ in range(t):
    dp = [0 for _ in range(11)]
    
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    
    n = int(input())
    
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    
    res.append(dp[n])

for i in res:
    print(i) 