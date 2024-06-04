lion = 0
tiger = 0

for _ in range(9):
    name = input()
    
    if name == 'Lion':
        lion += 1
    
    elif name == 'Tiger':
        tiger += 1

if lion > tiger:
    print('Lion')

else:
    print('Tiger')