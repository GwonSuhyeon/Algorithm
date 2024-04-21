res = []

while True:
    N = int(input())
    
    if N == 0:
        break
    
    names = []
    arr = {}
    
    for _ in range(N):
        name, height = map(str, input().split())
        
        arr[name] = float(height)
    
    arr = sorted(arr.items(), key=lambda x: -x[1])
    
    max_height = 0
    
    for name, height in arr:
        if max_height == 0:
            max_height = height
        
        if max_height > height:
            break
        
        names.append(name)

    res.append(names)

for i in res:
    for k in i:
        print(k, end=' ')
    print()