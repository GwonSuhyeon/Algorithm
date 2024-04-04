def back_tracking(start):
    
    if len(digit) == M:
        for i in digit:
            print(i, end=' ')
        print()
        
        return
    
    for i in range(start, N):
        digit.append(arr[i])
        
        back_tracking(i)
        
        digit.pop()

N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr = sorted(arr)

digit = []

back_tracking(0)