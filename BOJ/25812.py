n, r = map(int, input().split())

option1 = 0
option2 = 0

for _ in range(n):
    salary = int(input())

    if salary < r:
        option1 += 1
    elif salary > r:
        option2 += 1

if option1 > option2:
    print(1)
elif option1 < option2:
    print(2)
else:
    print(0)