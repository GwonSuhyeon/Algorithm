n = int(input())

for _ in range(n):
    arr = list(map(int, input().split()))
    
    print(*arr)

    if 17 in arr and 18 not in arr:
        print('zack', end='\n\n')
    elif 17 not in arr and 18 in arr:
        print('mack', end='\n\n')
    elif 17 in arr and 18 in arr:
        print('both', end='\n\n')
    else:
        print('none', end='\n\n')