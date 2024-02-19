import math

s = list(input())

res = [0 for _ in range(10)]

for i in s:
    number = int(i)
    
    if number == 6 or number == 9:
        res[6] += 1
        
    else:
        res[number] += 1

res[6] = math.ceil(res[6] / 2)

print(max(res))