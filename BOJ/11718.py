res = []

while True:
    try:
        S = input()
        
        if len(S) == 0:
            break
        
        res.append(S)
    
    except Exception as e:
        break

for i in res:
    print(i)