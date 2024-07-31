t1 = int(input())
t2 = int(input())

res = 2

while True:
    t = t1 - t2
    
    res += 1
    
    if t > t2:
        break
    
    t1 = t2
    t2 = t

print(res)