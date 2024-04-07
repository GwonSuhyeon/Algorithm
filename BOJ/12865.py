import sys


N, K = map(int, sys.stdin.readline().rstrip().split())

dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

weight = [0 for _ in range(N + 1)]
value = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    W, V = map(int, sys.stdin.readline().rstrip().split())
    
    weight[i] = W
    value[i] = V

for n in range(1, N + 1):
    for k in range(1, K + 1):
        w, v = weight[n], value[n]
        
        if n == 0 or k == 0:
            if w <= k:
                dp[n][k] = v
            
            else:
                dp[n][k] = 0
        
        elif w <= k:
            dp[n][k] = max(dp[n - 1][k], (dp[n - 1][k - w] + v))
        
        else:
            dp[n][k] = dp[n - 1][k]

print(dp[N][K])