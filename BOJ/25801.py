from collections import defaultdict

S = input()

arr = defaultdict(int)

for i in S:
    arr[i] += 1

even = 0
odd = 0

for i in arr.values():
    if i % 2 == 0:
        even += 1
    
    elif i % 2 == 1:
        odd += 1

if even > 0 and odd == 0:
    print('0')

elif even == 0 and odd > 0:
    print('1')

else:
    print('0/1')