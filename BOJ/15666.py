def back_tracking(start):
    
    if len(digit) == M:
        # res.append(''.join(digit))
        res.append(digit.copy())
        
        return
    
    for i in range(start, N):
        digit.append(str(arr[i]))
        
        back_tracking(i)
        
        digit.pop()
    
N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr = sorted(arr)
res = []
digit = []

temp = []

back_tracking(0)

# res = list(set(res))
# res = sorted(res, key=lambda x : x)

for i in res:
    if '_'.join(i) in temp:
        continue
    
    temp.append('_'.join(i))
    
    for k in i:
        print(k, end=' ')
    print()