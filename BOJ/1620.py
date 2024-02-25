import sys

n, m = map(int, input().split())

names = {}
numbers = {}

res = []

for i in range(1, n + 1):
    name = sys.stdin.readline().rstrip()
    
    names[name] = i
    numbers[str(i)] = name

for _ in range(m):
    s = sys.stdin.readline().rstrip()
    
    if s in names:
        res.append(names[s])
    
    elif s in numbers:
        res.append(numbers[s])

for i in res:
    print(i)