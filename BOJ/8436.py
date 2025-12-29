line = input()

arr = {'T': 2, 'K': 1, 'D': 2,
       'G': 1, 'L': 2, 'F': 2, 'R': 1
       }

res = 1

for i in line:
    if i in arr.keys():
        res *= arr[i]

print(res)