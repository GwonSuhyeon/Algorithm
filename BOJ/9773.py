N = int(input())

for _ in range(N):
    id = 0
    
    num = input()
    
    for i in num:
        id += int(i)
    
    id += int(num[-3:]) * 10
    
    if id < 1000:
        id += 1000
    
    id = str(id)
    
    if len(id) > 4:
        id = id[-4:]
    
    print(id)