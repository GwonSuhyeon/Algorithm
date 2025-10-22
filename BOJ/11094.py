N = int(input())

Simon_says = 'Simon says'

for _ in range(N):
    line = input()

    if Simon_says in line:
        print(line[len(Simon_says):])