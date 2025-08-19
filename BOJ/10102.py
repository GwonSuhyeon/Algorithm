V = int(input())

arr = input()

A = 0
B = 0

for i in arr:
    if i == 'A':
        A += 1
    else:
        B += 1

if A > B:
    print('A')
elif A < B:
    print('B')
else:
    print('Tie')