direction = ''

while True:
    S = input()

    if S == '99999':
        break

    num = sum(list(map(int, S[:2])))

    if num > 0 and num % 2 == 0:
        direction = 'right'
    elif num % 2 == 1:
        direction = 'left'
    
    print(f'{direction} {S[2:]}')