n = int(input())

o, p = 1, 0

while True:
    o = n / (2**p)
    
    if o % 2 > 0:
        break
    
    p += 1

print(int(o), p)