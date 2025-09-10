while True:
    n = int(input())

    if n == 0:
        break
    
    arr = list(map(int, input().split()))
    
    print(len([1 for i in arr if i <= sum(arr) / n]))