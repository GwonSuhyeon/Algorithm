a, b =  input().split()

a_weight = len(a) * sum([int(i) for i in a])
b_weight = len(b) * sum([int(i) for i in b])

if a_weight > b_weight:
    print(1)
elif a_weight < b_weight:
    print(2)
else:
    print(0)