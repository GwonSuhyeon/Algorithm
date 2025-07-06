N = int(input())

res = 0

for i in range(N, 0, -1):
    check = True
    
    for k in str(i):
        if k not in '47':
            check = False
            
            break
    
    if check == True:
        res = i
        
        break

print(res)