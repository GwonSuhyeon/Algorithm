arr = ['c=', 'c-', 'dz=', 'd-', 'lj' ,'nj', 's=', 'z=']
s = input()

res = 0

for a in arr:
    if a in s:
        res += s.count(a)
        s = s.replace(a, '.')

s = s.replace('.', '')
res += len(s)

print(res)