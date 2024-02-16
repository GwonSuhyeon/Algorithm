import math

s = input()
s = s.split()

sum = 0

for i in s:
    sum += math.pow(int(i), 2)

res = int(sum % 10)

print(res)