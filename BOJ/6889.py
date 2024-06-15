n = int(input())
m = int(input())

arr1 = []
arr2 = []

for _ in range(n):
    arr1.append(input())

for _ in range(m):
    arr2.append(input())

for i in range(n):
    for j in range(m):
        print(f'{arr1[i]} as {arr2[j]}')