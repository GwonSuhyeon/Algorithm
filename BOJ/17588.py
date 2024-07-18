n = int(input())

good = True

arr = []

for _ in range(n):
    arr.append(int(input()))

arr = sorted(arr)

maximum = arr[-1]

arr = set(arr)

for i in range(1, maximum + 1):
    if i not in arr:
        print(i)

        good = False

if good == True:
    print('good job')