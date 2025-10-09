T = int(input())

for i in range(T):
    n, P, Q = map(int, input().split())
    eggs = sorted(list(map(int, input().split())))

    cnt = 0
    weight = 0

    for egg in eggs:
        if cnt + 1 > P or weight + egg > Q:
            break
        
        cnt += 1
        weight += egg
    
    print(f'Case {i + 1}: {cnt}')