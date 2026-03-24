N, Y = map(int, input().split())

all = set([i for i in range(N)])
found = []

for _ in range(Y):
    found.append(int(input()))

found = set(found)

for i in (all - found):
    print(i)

print(f'Mario got {len(found)} of the dangerous obstacles.')