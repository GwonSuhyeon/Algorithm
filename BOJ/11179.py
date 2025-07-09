num = int(input())

res = 0

arr = []

while num > 0:
    arr.append(num % 2)
    
    num //= 2

for idx, i in enumerate(arr[::-1]):
    if i == 1:
        res += 2**idx

print(res)