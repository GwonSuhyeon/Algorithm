cnt = 0

while True:
    L, P, V = map(int, input().split())

    if L == 0 and P == 0 and V == 0:
        break
    
    cnt += 1

    res = 0

    res += (V // P) * L
    res += min(V % P, L)

    print(f'Case {cnt}: {res}')