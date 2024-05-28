S = input()

AB = {'A': 0, 'B': 0}

for i in S:
    if i == 'A':
        AB[i] += 1
    
    elif i == 'B':
        AB[i] += 1

print(str(AB['A']) + ' : ' + str(AB['B']))