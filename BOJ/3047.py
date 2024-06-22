A, B, C = sorted(map(int, input().split()))

S = input()

res = []

for i in S:
    if i == 'A':
        res.append(A)
    
    elif i == 'B':
        res.append(B)
    
    elif i == 'C':
        res.append(C)

print(f'{res[0]} {res[1]} {res[2]}')