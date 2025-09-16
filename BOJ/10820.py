while True:
    try:
        line = input()

        a = 0
        b = 0
        c = 0
        d = 0

        for i in line:
            if ord('a') <= ord(i) <= ord('z'):
                a += 1
            elif ord('A') <= ord(i) <= ord('Z'):
                b += 1
            elif ord('0') <= ord(i) <= ord('9'):
                c += 1
            elif i == ' ':
                d += 1
        
        print(a, b, c, d)
    except:
        break