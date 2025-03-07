a, b = map(int, input().split())

res = 1
num = sum([i for i in range(1, a)])

for i in range(a, b + 1):
    num += i
    res *= num

print(res % 14579)