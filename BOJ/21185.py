N = int(input())

if N == 1:
    print('Either')
else:
    if N % 2 == 1:
        print('Either')
    else:
        if (N // 2) % 2 == 1:
            print('Odd')
        else:
            print('Even')