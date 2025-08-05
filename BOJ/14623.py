B1 = input()
B2 = input()

b1 = 0
b2 = 0

res = ''

for idx, i in enumerate(list(B1)[::-1]):
    if int(i) == 1:
        b1 += 2**idx

for idx, i in enumerate(list(B2)[::-1]):
    if int(i) == 1:
        b2 += 2**idx

num = b1 * b2

while num > 0:
    res += str(num % 2)
    
    num //= 2

print(res[::-1])