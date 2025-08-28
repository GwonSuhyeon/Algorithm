arr = list(map(int, input().split()))

while True:
    if arr[0] > arr[1]:
        temp = arr[0]
        arr[0] = arr[1]
        arr[1] = temp
        
        print(*arr)
    
    if arr[1] > arr[2]:
        temp = arr[1]
        arr[1] = arr[2]
        arr[2] = temp
        
        print(*arr)
    
    if arr[2] > arr[3]:
        temp = arr[2]
        arr[2] = arr[3]
        arr[3] = temp
        
        print(*arr)
    
    if arr[3] > arr[4]:
        temp = arr[3]
        arr[3] = arr[4]
        arr[4] = temp
        
        print(*arr)
    
    if arr[0] == 1 and arr[1] == 2 and arr[2] == 3 and arr[3] == 4 and arr[4] == 5:
        break