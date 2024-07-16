T = int(input())

for i in range(T):
    S = input().split()
    
    if S[1] == '+':
        if int(S[0]) + int(S[2]) == int(S[-1]):
            print(f'Case {i + 1}: YES')
        
        else:
            print(f'Case {i + 1}: NO')
    
    else:
        if int(S[0]) - int(S[2]) == int(S[-1]):
            print(f'Case {i + 1}: YES')
        
        else:
            print(f'Case {i + 1}: NO')