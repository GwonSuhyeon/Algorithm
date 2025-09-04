while True:
    arr = list(map(int, input().split()))

    N = arr[0]

    if N == 0:
        break
    
    arr = arr[1:]

    prev = 0

    for i in arr:
        if i != prev:
            print(i, end=' ')
            
            prev = i
    print('$')