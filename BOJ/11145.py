T = int(input())

for _ in range(T):
    line = input().strip()

    if line.isdigit() == False:
        print('invalid input')

        continue
    elif int(line) < 0:
        print('invalid input')

        continue

    print(int(line))