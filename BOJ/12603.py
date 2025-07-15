N = int(input())

for i in range(N):
    C = int(input())
    I = int(input())
    P = list(map(int, input().split()))
    
    P_dict = {}
    
    for idx, p in enumerate(P):
        P_dict[idx + 1] = p
    
    P_dict = sorted(P_dict.items(), key=lambda x : x[1], reverse=True)
    
    res = []
    
    for idx, (x, y) in enumerate(P_dict[:len(P_dict) - 1]):
        for a, b in P_dict[idx + 1:]:
            if y + b == C:
                res.append(x)
                res.append(a)

    print(f'Case #{i + 1}: ', end='')
    print(*sorted(res))