T = int(input())

for _ in range(T):
    N = int(input())
    
    C_sum, G_sum = 0, 0
    
    for _ in range(N):
        C, G = input().split()
        
        C_sum += int(C)
        G_sum += int(C) * float(G)
    
    print(f'{C_sum} {(G_sum / C_sum):.1f}')