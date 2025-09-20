while True:
    line = input()

    if line[0] == '#':
        break
    
    Cheryl = 0
    Tania = 0

    for i in line[:-1].split():
        if i == 'A':
            Cheryl += 1

            continue
        
        if int(i) % 2 == 0:
            Tania += 1
        else:
            Cheryl += 1
    
    if Cheryl > Tania:
        print('Cheryl')
    elif Cheryl < Tania:
        print('Tania')
    else:
        print('Draw')