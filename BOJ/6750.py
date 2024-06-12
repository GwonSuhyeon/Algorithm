S = input()

for i in S:
    if i not in ['I', 'O', 'S', 'H', 'Z', 'X', 'N']:
        print('NO')
        
        exit()

print('YES')