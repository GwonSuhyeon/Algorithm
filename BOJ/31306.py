S = input()

arr = ['a', 'e', 'i', 'o', 'u']

res = 0
y = 0

for i in S:
    if i in arr:
        res += 1
    
    elif i == 'y':
        y += 1

print(res, res + y)