N = int(input())

calls = list(map(int, input().split()))

res1, res2 = 0, 0

for call in calls:
    res1 += ((call // 30) + 1) * 10
    res2 += ((call // 60) + 1) * 15

if res1 == res2:
    print(f'Y M {res1}')
elif res1 < res2:
    print(f'Y {res1}')
else:
    print(f'M {res2}')