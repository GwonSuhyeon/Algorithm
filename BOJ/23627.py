S = input()

if len(S) < 5:
    print('not cute')
else:
    if S[-5::] == 'driip':
        print('cute')
    else:
        print('not cute')