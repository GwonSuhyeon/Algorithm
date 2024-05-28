S = input()

AB = {'A': 0, 'B': 0}

A = 'A'
B = 'B'

for i in S:
    if i == A:
        AB[i] += 1
    
    elif i == B:
        AB[i] += 1

print(f'{AB[A]} : {AB[B]}')