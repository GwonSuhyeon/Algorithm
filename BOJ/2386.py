while True:
    line = input()
    
    if line == '#':
        break
    
    c = line.split()[0]
    s = ' '.join(line.split()[1:])
    
    res = 0
    
    try:
        res += s.count(c.lower())
        res += s.count(c.upper())
        
    except:
        continue
    
    print(c, res)