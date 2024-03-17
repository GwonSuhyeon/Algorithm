def back_tracking(start):
    
    if len(digit) == M:
        for d in digit:
            print(d, end=' ')
        print()
        
        return
    
    for i in range(start, N):
        digit.append(arr[i])
        back_tracking(i + 1)
        digit.pop()
    
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

digit = []
res = []

back_tracking(0)