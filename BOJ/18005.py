N = int(input())

if N == 1:
    print(0)
else:
    if N % 2 == 1:
        print(0)
    else:
        if (N // 2) % 2 == 1:
            print(1)
        else:
            print(2)