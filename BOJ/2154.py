N = input()

num = ''

for i in range(1, int(N) + 1):
    num += str(i)

for i in range(len(num) - len(N) + 1):
    if int(N) == int(num[i:i + len(N)]):
        print(i + 1)

        break