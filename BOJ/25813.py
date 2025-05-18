s = input()

u_idx = 0
f_idx = 0

for i in range(len(s)):
    if s[i] == 'U':
        u_idx = i
        break

for i in range(len(s) - 1, u_idx, -1):
    if s[i] == 'F':
        f_idx = i
        break

for i in range(len(s)):
    if i < u_idx:
        print('-', end='')
    elif u_idx < i < f_idx:
        print('C', end='')
    elif f_idx < i:
        print('-', end='')
    else:
        print(s[i], end='')