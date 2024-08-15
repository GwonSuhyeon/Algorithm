T = int(input())

for i in range(T):
    H, M = map(int, input().split())
    
    if M < 45:
        if H < 1:
            print(f'Case #{i + 1}: 23 {60 - 45 + M}')
        else:
            print(f'Case #{i + 1}: {H - 1} {60 - 45 + M}')
    else:
        print(f'Case #{i + 1}: {H} {M - 45}')