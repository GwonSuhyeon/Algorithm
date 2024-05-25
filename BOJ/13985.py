S = input().replace(' ', '').split('=')

a, b = map(int, S[0].split('+'))

if (a + b) == int(S[-1]):
    print('YES')

else:
    print('NO')