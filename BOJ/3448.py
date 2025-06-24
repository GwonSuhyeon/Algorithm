N = int(input())

for _ in range(N):
    R = 0
    A = 0
    
    while True:
        line = input()
        
        if len(line) == 0:
            res = round((R / A) * 100, 1)
            
            if res % 2 == 0:
                print(f'Efficiency ratio is {int(res)}%.')
            else:
                print(f'Efficiency ratio is {res}%.')
            
            break
        
        A += len(line)
        R += len(line) - line.count('#')