A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

t = A
res = 0

if t < 0:
    freeze = True
else:
    freeze = False

while t != B:
    if t < 0:
        t += 1
        res += C
    elif t > 0:
        t += 1
        res += E
    else:
        if freeze == True:
            res += D
        
        t += 1
        res += E

print(res)