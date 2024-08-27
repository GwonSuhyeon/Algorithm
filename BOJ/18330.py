n = int(input())
k = int(input())

if n <= 60 + k:
    res = n * 1500
else:
    res = (60 + k) * 1500 + (n - 60 - k) * 3000

print(res)