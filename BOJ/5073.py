while True:
    arr = sorted(list(map(int, input().split())))

    if sum(arr) == 0:
        break
    
    if arr[2] >= arr[0] + arr[1]:
        print('Invalid')
    elif arr[0] == arr[1] == arr[2]:
        print('Equilateral')
    elif (arr[0] == arr[1] and arr[1] != arr[2]) or (arr[0] != arr[1] and arr[1] == arr[2]):
        print('Isosceles')
    elif arr[0] != arr[1] != arr[2]:
        print('Scalene')