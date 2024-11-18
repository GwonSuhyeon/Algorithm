msg = input()

for i in msg:
    digit = ord(i)

    if ord('A') <= digit < ord('a'):
        digit -= 38
        print(digit, end='')
    elif ord('a') <= digit <= ord('z'):
        digit -= 96
        if digit < 10:
            print(f'0{digit}', end='')
        else:
            print(digit, end='')
    elif ord('0') <= digit <= ord('9'):
        print(f'#{i}', end='')
    else:
        print(i, end='')