n, k = map(int, input().split())

value = k
coin = []
res = []

for _ in range(n):
    coin.append(int(input()))

for i in coin[::-1]:
    res.insert(0, int(value / i))
    value = int(value % i)

print(sum(res))