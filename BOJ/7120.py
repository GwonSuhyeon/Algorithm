s = input()

prev = ''

for i in s:
    if i != prev:
        print(i, end='')

        prev = i