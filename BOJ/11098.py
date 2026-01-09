n = int(input())

for _ in range(n):
    p = int(input())

    arr = {}

    for _ in range(p):
        C, name = input().split()

        arr[int(C)] = name
    
    print(arr[max(arr.keys())])