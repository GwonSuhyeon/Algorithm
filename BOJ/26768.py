line = input()

Litera_Cyfra = {'a': 4, 'e': 3, 'i': 1, 'o': 0, 's': 5}
key = set(Litera_Cyfra.keys())

for i in line:
    if i in key:
        print(str(Litera_Cyfra[i]), end='')
    else:
        print(i, end='')