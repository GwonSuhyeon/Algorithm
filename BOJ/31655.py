A, B, C = map(str, input().split('/'))

EU = 0
US = 0

if 1 <= int(A) <= 31 and 1 <= int(B) <= 12 and 0 <= int(C) <= 9999:
    EU = 1

if 1 <= int(A) <= 12 and 1 <= int(B) <= 31 and 0 <= int(C) <= 9999:
    US = 1

if EU == 1 and US == 0:
    print('EU')

elif EU == 0 and US == 1:
    print('US')

else:
    print('either')