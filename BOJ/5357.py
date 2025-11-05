n = int(input())

for _ in range(n):
    line = input()

    prev = None

    for i in line:
        if prev is None:
            print(i, end='')
            
            prev = i
        else:
            if i != prev:
                print(i, end='')

                prev = i
    
    print()