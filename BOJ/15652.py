def back_tracking(start_idx):
    
    if len(digit) == M:
        for d in digit:
            print(d, end=' ')
        print()
                
        return
    
    for i in range(start_idx, N + 1):
        digit.append(i)
        back_tracking(i)
        digit.pop()

N, M = map(int, input().split())

arr = [i for i in range(N + 1)]

digit = []

back_tracking(1)