T = int(input())

for _ in range(T):
    N = int(input())
    
    num = str(N + int(str(N)[::-1]))
    
    res = True
    
    for i in range(len(num) // 2):
        if num[i] != num[len(num) - 1 - i]:
            res = False
            
            break
    
    if res:
        print('YES')
    else:
        print('NO')