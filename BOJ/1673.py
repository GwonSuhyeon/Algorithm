while True:
    try:
        n, k = map(int, input().split())

        print(((n * k) - 1) // (k - 1))
    except:
        break