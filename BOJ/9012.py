t = int(input())

res = []

for _ in range(t):
    s = input()
    
    stack = []
    
    for i in s:
        if i =='(':
            stack.append(i)
        
        elif i == ')':
            if len(stack) == 0:
                stack.append(i)
                
                break
            
            else:
                stack.pop()
    
    if len(stack) == 0:
        res.append('YES')
    
    else:
        res.append('NO')
    
    
for i in res:
    print(i)