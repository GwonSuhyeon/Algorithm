N = int(input())
arr = list(map(int, input().split()))

res = 'YES'
prev = 0
descent = False

for i in arr:
    if prev > i:
        descent = True
    
    if descent == False and prev >= i:
        res = 'NO'
        
        break
    elif descent == True and prev <= i:
        res = 'NO'

        break

    prev = i

print(res)