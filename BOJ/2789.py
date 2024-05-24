S = input()

CAMBRIDGE = list('CAMBRIDGE')

for i in S:
    if i not in CAMBRIDGE:
        print(i, end='')