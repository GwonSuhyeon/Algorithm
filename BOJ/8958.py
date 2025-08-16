T = int(input())

for _ in range(T):
    line = input()
    
    score = 0
    res = 0
    
    for i in line:
        if i == 'X':
            score = 0
        else:
            score += 1
            
            res += score
    
    print(res)