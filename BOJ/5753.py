while True:
    N, D = map(int, input().split())

    dinner = [0 for _ in range(N)]

    if N == 0 and D == 0:
        break

    for _ in range(D):
        arr = list(map(int, input().split()))

        dinner = [sum(values) for values in zip(dinner, arr)]
    
    if D in dinner:
        print('yes')
    else:
        print('no')