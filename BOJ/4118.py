while True:
    N = int(input())
    
    if N == 0:
        break
    
    numbers = set()
    
    for _ in range(N):
        ticket = list(map(int, input().split()))
        
        numbers.update(ticket)
    
    res = 'Yes'
    
    for i in range(1, 50):
        if i not in numbers:
            res = 'No'
            
            break
    
    print(res)