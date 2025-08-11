card = [i for i in range(21)]

for _ in range(10):
    a, b = map(int, input().split())
    
    temp = card[a:b+1][::-1]
    
    idx = a
    
    for i in temp:
        card[idx] = i
        
        idx += 1

print(*card[1::])