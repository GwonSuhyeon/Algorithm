user = 0

while True:
    L = int(input())
    
    if L == 0:
        break
    
    N = int(input())
    
    user += 1
    
    print(f'User {user}')
    
    for _ in range(N):
        d = int(input())
        
        print('%.5f' % ((d / 100000) * L))