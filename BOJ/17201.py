N = int(input())
arr = list(map(int, input()))

res = set([str(arr[i]) + str(arr[i + 1]) for i in range(0, len(arr) - 1, 2)])

if len(res) == 2:
    print('No')
else:
    print('Yes')