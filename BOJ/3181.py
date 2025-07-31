line = input().split()

arr = set(['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili'])

res = ''

for i, word in enumerate(line):
    if i > 0 and word in arr:
        continue
    
    res += word[0]

print(res.upper())