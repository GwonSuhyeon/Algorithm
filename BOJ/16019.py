arr = list(map(int, ('0 ' + input()).split()))

dist = []

for idx, i in enumerate(arr):
    if idx == 0:
        dist.append(i)
    else:
        dist.append(i + dist[-1])

for i in range(5):
    for k in range(5):
        print(abs(dist[i] - dist[k]), end=' ')
    print()