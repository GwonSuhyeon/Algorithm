N = int(input())

arr = set()

for _ in range(N):
    line = input()

    arr.add(line)

for password in arr:
    if password[::-1] in arr:
        print(len(password), password[len(password) // 2])

        break