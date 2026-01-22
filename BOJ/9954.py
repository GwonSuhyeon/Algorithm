while True:
    line = input()

    if line == '#':
        break

    res = []

    shift = (ord(line[-1]) - ord('A')) % 26

    for i in line[:-1]:
        if 'A' <= i <= 'Z':
            ch = chr(((ord(i) - ord('A') - shift) % 26) + ord('A'))
        elif 'a' <= i <= 'z':
            ch = chr(((ord(i) - ord('a') - shift) % 26) + ord('a'))
        else:
            ch = i
        
        res.append(ch)
    
    print(''.join(res))