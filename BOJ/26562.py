N = int(input())

arr = {'Franklin': 100, 'Grant': 50, 'Jackson': 20, 'Hamilton': 10, 'Lincoln': 5, 'Washington': 1}

for _ in range(N):
    res = 0
    
    names = input().split()
    
    for name in names:
        res += arr[name]
    
    print(f'${res}')