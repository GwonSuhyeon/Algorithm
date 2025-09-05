while True:
    arr = list(map(int, input().split()))

    if arr[0] == -1:
        break
    
    arr_set = set(arr[:len(arr) - 1])

    res = 0

    for i in arr_set:
        if i * 2 in arr_set:
            res += 1
    
    print(res)