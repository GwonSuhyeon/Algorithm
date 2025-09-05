res = set()

for _ in range(10):
    A = int(input())

    res.add(A % 42)

print(len(res))