N = int(input())

print('Gnomes:')

for _ in range(N):
    arr = list(map(int, input().split()))
    arr_sort = sorted(arr)
    arr_reverse = arr_sort[::-1]

    ordered = True

    for a, b, c in zip(arr, arr_sort, arr_reverse):
        if a != b and a != c:
            ordered = False
    
    if ordered == True:
        print('Ordered')
    else:
        print('Unordered')