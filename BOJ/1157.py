s = input().lower()

c = list(set(s))

maximum = 0
res = ''

for i in c:
    
    cnt = s.count(i)
    
    if maximum < cnt:
        maximum = cnt
        res = i.upper()
    
    elif maximum == cnt:
        res = '?'
    
print(res)