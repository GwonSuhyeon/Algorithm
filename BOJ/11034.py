while True:
    try:
        A, B, C = map(int, input().split())
        
        ab = B - A
        bc = C - B

        res = max(ab, bc) - 1

        print(res)
    except:
        break