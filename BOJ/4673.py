def d(n):
    
    sum = 0
    
    for i in list(str(n)):
        sum += int(i)
    
    return sum + n

res = set([i for i in range(1, 10001)])

for i in range(1, 10001):
    self_num = d(i)
    
    if self_num in res:
        res.remove(self_num)

for i in res:
    print(i)