n = int(input())

while True:
    value = int(input())

    if value == 0:
        break
    
    if value % n == 0:
        print(f'{value} is a multiple of {n}.')
    else:
        print(f'{value} is NOT a multiple of {n}.')