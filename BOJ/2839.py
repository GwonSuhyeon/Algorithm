n = int(input())

res = 0

max_5kg = n // 5
max_3kg = (n - abs((max_5kg * 5))) // 3

while True:
    
    if (max_5kg * 5) + (max_3kg * 3) == n:
        res = (max_5kg + max_3kg)
        
        break
    
    if max_5kg < 0:
        res = -1
        
        break
    
    max_5kg -= 1
    max_3kg = (n - abs((max_5kg * 5))) // 3

print(res)