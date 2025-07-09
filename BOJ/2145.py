while True:
    N = int(input())
    
    if N == 0:
        break
    
    while len(str(N)) > 1:
        temp = 0
        
        for i in str(N):
            temp += int(i)
        
        N = temp
    
    print(N)