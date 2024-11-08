while True:
    l, w, a = map(int, input().split())

    if l == 0 and w == 0 and a == 0:
        break
    
    if a == 0:
        a = l * w
    elif l == 0:
        l = a // w
    elif w == 0:
        w = a // l
    
    print(l, w, a)