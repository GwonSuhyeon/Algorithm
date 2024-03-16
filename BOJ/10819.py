def back_tracking():
    
    global res
    
    if len(digit) == N:
        num = [abs(digit[i] - digit[i + 1]) for i in range(N - 1)]
        res = max(res, sum(num))
        
        return
    
    for i in range(N):
        if digit.count(arr[i]) == arr.count(arr[i]):
            continue
        
        digit.append(arr[i])
        back_tracking()
        digit.pop()
    
N = int(input())
arr = list(map(int, input().split()))

digit = []
res = -999999

back_tracking()

print(res)