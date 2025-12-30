n = int(input())
word = input()

res = 0
hidden = ''

for i in word:
    if 'a' <= i.lower() <= 'z':
        if len(hidden) > 0:
            res += int(hidden)
            hidden = ''
        
        continue

    hidden += i

if len(hidden) > 0:
    res += int(hidden)

print(res)