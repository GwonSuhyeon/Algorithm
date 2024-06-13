S = input()

num = None
res = 0
arr = []

for i in S:
    if num is None:
        num = int(i)
        arr.append(int(i))
    
    else:
        if int(i) - num == 1:
            arr.append(int(i))
        
        else:
            if len(arr) == 3:
                res += 1
            
            arr.clear()
            arr.append(int(i))
        
        num = int(i)

if len(arr) == 3:
    res += 1

print(res)