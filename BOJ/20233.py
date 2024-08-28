a = int(input())
x = int(input())
b = int(input())
y = int(input())
T = int(input())

if T < 30:
    res1 = a
else:
    res1 = a + ((T - 30) * x) * 21

if T < 45:
    res2 = b
else:
    res2 = b + ((T - 45) * y) * 21

print(res1, res2)