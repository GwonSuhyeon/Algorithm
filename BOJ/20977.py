N = int(input())

S = input()

J = []
O = []
I = []

for i in S:
    if i == 'J':
        J.append(i)
    
    elif i == 'O':
        O.append(i)
    
    elif i == 'I':
        I.append(i)

print(''.join(J), end='')
print(''.join(O), end='')
print(''.join(I), end='')