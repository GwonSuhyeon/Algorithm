T = int(input())

char = [chr(i) for i in range(65, 91)]

for _ in range(T):
    M, Type = input().split()
    
    if Type == 'C':
        arr = input().split()
        
        for i in arr:
            print(char.index(i) + 1, end=' ')
    else:
        arr = list(map(int, input().split()))
        
        for i in arr:
            print(char[i - 1], end= ' ')
    
    print()