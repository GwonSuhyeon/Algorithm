while True:
    line = input().lower()
    
    if line == '#':
        break
    
    res = []
    
    for i in line:
        if ord('a') <= ord(i) <= ord('z'):
            res.append(i)
    
    print(len(set(res)))