while True:
    line = input()
    
    if line == 'EOI':
        break
    
    line = line.split()
    
    res = 'Missing'
    
    for word in line:
        if 'nemo' in word.lower():
            res = 'Found'
            
            break
    
    print(res)