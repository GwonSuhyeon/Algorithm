text = input()

prev = ''
res = 'no hiss'

for i in text:
    if prev == 's' and i == 's':
        res = 'hiss'

        break
    
    prev = i

print(res)