from collections import defaultdict


arr = []
arr_dict = defaultdict(int)

for _ in range(10):
    num = int(input())
    
    arr.append(num)
    arr_dict[num] += 1

print(sum(arr) // len(arr))

for key, value in arr_dict.items():
    if value == max(arr_dict.values()):
        print(key)