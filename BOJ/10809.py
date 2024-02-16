s = input()

eng = list('abcdefghijklmnopqrstuvwxyz')

res = []
for i in eng:
    if i in s:
        res.append(s.index(i))
    
    else:
        res.append(-1)

for i in res:
    print(i, end=' ')