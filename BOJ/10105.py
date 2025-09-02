N = int(input())

arr1 = input().split()
arr2 = input().split()

partners = dict()

res = 'good'

for a, b in zip(arr1, arr2):
    partners[a] = b

for a in partners.keys():
    if a != partners[partners[a]] or a == partners[a]:
        res = 'bad'

        break

print(res)