while True:
    try:
        arr = list(map(int, input().split()))

        for idx in range(len(arr)):
            if idx == 0:
                print(arr[idx] * arr[idx + 1], end=' ')
            elif 0 < idx < len(arr) - 1:
                print(arr[idx - 1] * arr[idx] * arr[idx + 1], end=' ')
            else:
                print(arr[idx - 1] * arr[idx], end=' ')
        
        print()
        
    except:
        break