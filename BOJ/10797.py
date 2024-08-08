date = int(input())

cars = list(map(int, input().split()))

res = 0

for car in cars:
    if date == car:
        res += 1

print(res)