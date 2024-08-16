T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    
    arr = list(map(int, input().split()))
    
    res = 0
    
    for i in arr:
        res += i // K
    
    print(res)