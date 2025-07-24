while True:
    line = input()
    
    if line == 'END':
        break
    
    for i in list(line)[::-1]:
        print(i, end='')
    
    print()