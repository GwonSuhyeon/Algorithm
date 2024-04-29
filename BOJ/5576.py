arr1 = []
arr2 = []

for _ in range(10):
    arr1.append(int(input()))

for _ in range(10):
    arr2.append(int(input()))

arr1 = sorted(arr1, reverse=True)
arr2 = sorted(arr2, reverse=True)

print(sum(arr1[:3]), sum(arr2[:3]))