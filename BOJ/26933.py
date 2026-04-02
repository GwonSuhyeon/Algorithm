N = int(input())

res = 0

for _ in range(N):
    H, B, K = map(int, input().split())

    num = max(0, B - H)
    
    res += (num * K)

print(res)