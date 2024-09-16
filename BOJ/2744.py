S = input()

for i in S:
    if 'a' <= i <= 'z':
        print(i.upper(), end='')
    else:
        print(i.lower(), end='')