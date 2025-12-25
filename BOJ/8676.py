n = int(input())
arr = list(map(int, input().split()))

res = 'NIE'

for i in range(n - 2):
    a = arr[i]
    b = arr[i + 1]
    c = arr[i + 2]

    if a != b and b != c and a != c:
        res = 'TAK'

        break

print(res)