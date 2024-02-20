import math

n = int(input())

factorial = list(str(math.factorial(n)))

res = 0

for i in factorial[::-1]:
    if i == '0':
        res += 1
    
    else:
        break

print(res)