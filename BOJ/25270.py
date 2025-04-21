n = int(input())

for i in range(0, 100):
    if str(n + i)[-2:] == '99':
        print(n + i)
        break
    elif str(n - i)[-2:] == '99':
        print(n - i)
        break