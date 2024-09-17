L, P = map(int, input().split())

people = list(map(int, input().split()))

for i in people:
    print(i - (L * P), end=' ')