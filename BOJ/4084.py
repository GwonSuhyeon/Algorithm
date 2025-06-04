while True:
    a, b, c, d = map(int, input().split())
    
    if a == b == c == d == 0:
        break
    
    res = 0
    
    while True:
        if a == b == c == d:            
            break
        
        a_temp = abs(a - b)
        b_temp = abs(b - c)
        c_temp = abs(c - d)
        d_temp = abs(d - a)
        
        a = a_temp
        b = b_temp
        c = c_temp
        d = d_temp
        
        res += 1
    
    print(res)