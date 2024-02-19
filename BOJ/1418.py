import math

n = int(input())
k = int(input())

prime = [1 for _ in range(n + 1)]
res = [1 for _ in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if prime[i] == 1:
        for j in range((2 * i), (n + 1), i):
            prime[j] = 0

for i in range(2, n + 1):
    if prime[i] == 1 and i > k:
        for j in range(i, (n + 1), i):
            res[j] = 0

print(res.count(1) - 1)