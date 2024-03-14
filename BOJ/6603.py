def back_tracking(start_idx):
    
    global K
    
    if len(digit) == 6:
        for d in digit:
            print(d, end=' ')
        print()
        
        return
    
    for i in range(start_idx, K):
        digit.append(arr[i])
        back_tracking(i + 1)
        digit.pop()

global K

arr = []
digit = []

while True:
    arr = list(map(int, input().split()))
    
    K = arr[0]
    
    if K == 0:
        break
    
    arr = arr[1:]
    
    back_tracking(0)
    
    print()