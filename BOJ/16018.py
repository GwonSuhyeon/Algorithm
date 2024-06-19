N = int(input())

arr1 = input()
arr2 = input()

res = 0

for a, b in zip(arr1, arr2):
    if a == 'C' and b == 'C':
        res += 1

print(res)