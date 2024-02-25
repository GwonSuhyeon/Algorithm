stack = []

res = []

while True:
    balance = True
    
    s = input()
    
    if s == '.':
        break
    
    stack.clear()
    
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        
        elif i == ')':
            if len(stack) == 0 or stack[-1] != '(':
                balance = False
                
                break
            
            else:
                stack.pop()
        
        elif i == ']':
            if len(stack) == 0 or stack[-1] != '[':
                balance = False
                
                break
            
            else:
                stack.pop()
    
    if len(stack) == 0 and balance == True:
        res.append('yes')
    
    else:
        res.append('no')

for i in res:
    print(i)