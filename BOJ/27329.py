N = int(input())

S = input()

if N % 2 != 0:
    print('No')

else:
    center = N // 2
    
    if S[:center] == S[center:]:
        print('Yes')
    
    else:
        print('No')