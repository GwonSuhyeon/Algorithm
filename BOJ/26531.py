import re


S = re.split('[+=]', input().replace(' ', ''))

if int(S[0]) + int(S[1]) == int(S[-1]):
    print('YES')
else:
    print('NO')