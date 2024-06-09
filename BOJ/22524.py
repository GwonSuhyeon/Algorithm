while True:
    S = input()
    
    if S == '#':
        break
    
    left = 0
    right = 1
    current = None
    res = 0
    
    left_key = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b']
    
    for i in S:
        if i in left_key:
            if current == right:
                res += 1
            
            current = left
        
        else:
            if current == left:
                res += 1
            
            current = right
    
    print(res)