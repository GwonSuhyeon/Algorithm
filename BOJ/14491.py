T = int(input())

res = []

while T > 0:
    res.append(str(T % 9))

    T //= 9

print(''.join(res[::-1]))