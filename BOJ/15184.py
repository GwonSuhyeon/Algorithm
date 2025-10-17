from collections import defaultdict


line = input().upper()

res = defaultdict(int)

for i in line:
    if ord('A') <= ord(i) <= ord('Z'):
        res[i] += 1

for i in range(ord('A'), ord('Z') + 1):
    print(f'{chr(i)} | ', end='')

    if chr(i) in res.keys():
        print('*' * res[chr(i)])
    else:
        print()