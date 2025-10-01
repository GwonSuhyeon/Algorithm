while True:
    line = input()

    if line == '#':
        break
    
    p = line[-1]
    
    line = line[:-1]

    odd = line.count('1')
    
    if odd == 0 or odd % 2 == 0:
        if p == 'e':
            print(line + '0')
        else:
            print(line + '1')
    elif odd % 2 == 1:
        if p == 'e':
            print(line + '1')
        else:
            print(line + '0')