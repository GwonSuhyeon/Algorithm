res = 0

for _ in range(6):
    line = input()

    if line == 'W':
        res += 1

if res >= 5:
    print(1)
elif res >= 3:
    print(2)
elif res >= 1:
    print(3)
else:
    print(-1)