while True:
    line = input()
    
    if line == '*':
        break

    arr = {ch for ch in line if 'a' <= ch <= 'z'}
    
    if len(arr) == 26:
        print('Y')
    else:
        print('N')