t = int(input())

result = []

for i in range(t):
    h, w, n = map(int, input().split())
    
    res = None
    
    for room in range(w):
        for floor in range(h):
            
            if (room * h) + (floor + 1) == n:
                if (room + 1) < 10:
                    res = str(floor + 1) + '0' + str(room + 1)
                else:
                    res = str(floor + 1) + str(room + 1)
                
                break
        
        if res is not None:
            break
    
    result.append(res)

for i in result:
    print(i)