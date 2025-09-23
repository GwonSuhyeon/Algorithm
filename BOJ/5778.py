while True:
    N, M = map(int, input().split())

    if N == 0 and M == 0:
        break

    arr = sorted(list(map(int, input().split())))
    
    res = 0

    for i in set(arr):
        if arr.count(i) > 1:
            res += 1
    
    print(res)