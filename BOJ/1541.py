import re

s = input()

s_split = s.split('-')

res = 0

for idx, i in enumerate(s_split):
    sum = 0
    
    if i == '':
        continue
    
    sub = i.split('+')
    
    for k in sub:
        sum += int(k)
    
    if idx == 0 and s[0] == '-':
        res += (sum * -1)
    
    elif idx == 0 and s[0] != '-':
        res += sum
        
    else:
        res -= sum

print(res)