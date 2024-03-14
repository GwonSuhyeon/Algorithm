def back_tracking(start_idx):
    
    global res
    
    for i in range(start_idx, N):
        digit.append(arr[i])
        
        if sum(digit) == S:
            res += 1
        
        back_tracking(i + 1)
        digit.pop()

N, S = map(int, input().split())

arr = list(map(int, input().split()))

digit = []

global res
res = 0

back_tracking(0)

print(res)