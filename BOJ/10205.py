K = int(input())

for i in range(1, K + 1):
    h = int(input())
    attack = input()

    for a in attack:
        if a == 'c':
            h += 1
        elif a == 'b':
            h -= 1
    
    print(f'Data Set {i}:')
    print(h)
    print()