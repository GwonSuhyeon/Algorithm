while True:
    try:
        line = input()
    except:
        break
    
    H, P = map(int, line.split())

    print(f'{round(H / P, 2):.02f}')