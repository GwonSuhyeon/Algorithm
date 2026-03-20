N = int(input())
K = int(input())
S = input()

r = S.count('R')

if r == K:
    print('W')
else:
    print('R')