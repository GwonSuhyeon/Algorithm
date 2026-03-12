N = int(input())
S = input()

try:
    i = S.index('I')
    o = S.index('O', i + 1)
    i_2 = S.index('I', o + 1)

    print('Yes')
except:
    print('No')