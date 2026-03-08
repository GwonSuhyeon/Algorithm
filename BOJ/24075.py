A, B = map(int, input().split())

res = sorted([A + B, A - B], reverse=True)

for i in res:
    print(i)