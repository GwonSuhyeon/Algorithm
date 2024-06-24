N = int(input())

for _ in range(N):
    r, e, c = map(int, input().split())
    
    e2 = e - c
    
    if r > e2:
        print('do not advertise')
    
    elif r == e2:
        print('does not matter')
    
    else:
        print('advertise')