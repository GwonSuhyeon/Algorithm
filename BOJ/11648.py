N = int(input())

res = 0

while True:
    digit = str(N)
    
    if len(digit) == 1:
        break
    
    for idx, i in enumerate(digit):
        if idx == 0:
            N = int(i)
        
        else:
            N *= int(i)
    
    res += 1

print(res)