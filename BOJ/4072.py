while True:
    line = input()
    
    if line == '#':
        break
    
    for word in line.split():
        print(word[::-1], end=' ')
    
    print()