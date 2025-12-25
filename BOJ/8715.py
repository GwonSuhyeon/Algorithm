n = int(input())
arr = list(map(int, input().split()))

arr_set = set(arr)

res = 'NIE'

if len(arr) == n and len(arr_set) == n and \
    min(arr_set) == 1 and max(arr_set) == n:
    res = 'TAK'

print(res)