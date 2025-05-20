from collections import defaultdict


s = input()

string_dict = defaultdict(int)

even = 0
odd = 0

for i in s:
    string_dict[i] += 1

for i in string_dict.values():
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

if even > 0 and odd > 0:
    print(2)
elif odd > 0:
    print(1)
else:
    print(0)