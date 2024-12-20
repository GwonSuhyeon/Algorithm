while True:
    N = int(input())

    if N == 0:
        break
    
    arr = list(map(int, input().split()))
    
    Y = sum(arr)
    X = N - Y

    print(f'Mary won {X} times and John won {Y} times')