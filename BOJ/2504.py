arr = list(input())

stack = []
res = []
check = True

for i in arr:
    if i == ')':
        if len(stack) == 0:
            print(0)
            check = False
            stack.clear()
            break
        
        if stack[len(stack) - 1] != '(':
            print(0)
            check = False
            stack.clear()
            break
        
        stack.pop()
    
    elif i == ']':
        if len(stack) == 0:
            print(0)
            check = False
            stack.clear()
            break
        
        if stack[len(stack) - 1] != '[':
            print(0)
            check = False
            stack.clear()
            break
        
        stack.pop()
    
    else:
        stack.append(i)

if len(stack) > 0:
    print(0)
    check = False

if check == True:
    num = 1
    
    for idx, i in enumerate(arr):
        if i == '(':
            num *= 2
        
        elif i == '[':
            num *= 3
        
        elif i == ')':
            if arr[idx - 1] == '(':
                res.append(num)
            
            num //= 2
        
        elif i == ']':
            if arr[idx - 1] == '[':
                res.append(num)
            
            num //= 3

    print(int(sum(res)))