while True:
    N = int(input())
    
    if N == -1:
        break
    
    total_time = 0
    d = 0
    
    for _ in range(N):
        m, t = map(int, input().split())
        
        d += m * (t - (total_time))
        total_time = t
    
    print(f'{d} miles')