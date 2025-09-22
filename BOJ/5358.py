while True:
    try:
        line = input()

        res = ''

        for i in line:
            if i == 'i':
                res += 'e'
            elif i == 'e':
                res += 'i'
            elif i == 'I':
                res += 'E'
            elif i == 'E':
                res += 'I'
            else:
                res += i
        
        print(res)
    except:
        break