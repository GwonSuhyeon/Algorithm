S1 = input()
S2 = input()

if len(S1) < len(S2):
    print('no')
else:
    if S2 in S1:
        print('go')
    else:
        print('no')