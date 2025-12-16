while True:
    name1, name2 = input().split()

    if name1 == '#' and name2 == '#':
        break

    n = int(input())
    
    res1 = 0
    res2 = 0
    
    for _ in range(n):
        call, result = input().split()

        if call == result:
            res1 += 1
        else:
            res2 += 1

    print(name1, res1, name2, res2)