def back_tracking():
    
    if len(digit) == M:
        res.append(digit.copy())
        
        return
    
    for i in range(0, N):
        if arr[i] in digit:
            continue
        
        digit.append(arr[i])
        back_tracking()
        digit.pop()
    
N, M = map(int, input().split())

arr = list(map(int, input().split()))
digit = []
res = []

back_tracking()

res = sorted(res)

for i in res:
    for k in i:
        print(k, end=' ')
    print()