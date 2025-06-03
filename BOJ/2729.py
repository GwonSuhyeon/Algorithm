T = int(input())

for _ in range(T):
    a_binary, b_binary = input().split()
    
    a, b = 0, 0
    
    for idx, i in enumerate(a_binary[::-1]):
        if i == '1':
            a += 2**idx

    for idx, i in enumerate(b_binary[::-1]):
        if i == '1':
            b += 2**idx
    
    res = []
    
    c = a + b
    
    while True:
        if c < 1:
            break
        
        res.append(c % 2)
        
        c //= 2
    
    if not res:
        print(0)
    else:
        for i in res[::-1]:
            print(i, end='')
        print()