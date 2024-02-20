n = int(input())

res = 0

for i in range(1, n + 1):
    
    if i < 100:
        res += 1
        
        continue
    
    diff = 0
    isHansu = True
    
    value = list(str(i))
    
    for k in range(len(value) - 1):
        if k == 0:
            diff = int(value[k]) - int(value[k + 1])
        
        else:
            if diff != int(value[k]) - int(value[k + 1]):
                isHansu = False
                
                break
    
    if isHansu == True:
        res += 1

print(res)