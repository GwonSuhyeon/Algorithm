X = input().split()
Y = input().split()

for x, y in zip(X, Y):
    if x == y:
        print('N')

        exit()

print('Y')