N = input()[::-1]

num = 0

for i in range(len(N)):
    if N[i] == '1':
        num += (2**i)

num *= 17

res = ''

while num > 0:
    res += str(num % 2)
    num //= 2

print(res[::-1])