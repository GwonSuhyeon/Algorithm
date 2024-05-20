N = int(input())

names = []

for _ in range(N):
    names.append(input())

flag = False

increasing = sorted(names)

for a, b in zip(names, increasing):
    if a != b:
        flag = True
        break

if flag == False:
    print('INCREASING')
    exit()

flag = False

decreasing = sorted(names, reverse=True)

for a, b in zip(names, decreasing):
    if a != b:
        flag = True
        break

if flag == False:
    print('DECREASING')
    exit()

else:
    print('NEITHER')