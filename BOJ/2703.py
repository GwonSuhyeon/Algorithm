T = int(input())

for _ in range(T):
    msg = input()
    crypto = input()
    crypto_dict = {}

    for idx, c in enumerate([c for c in range(ord('A'), ord('Z') + 1)]):
        crypto_dict[chr(c)] = crypto[idx]
    
    for i in msg:
        if i != ' ':
            print(crypto_dict[i], end='')
        else:
            print(i, end='')
    
    print()