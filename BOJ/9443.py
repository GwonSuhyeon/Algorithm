n = int(input())

arr = set()

for _ in range(n):
    S = input()

    arr.add(S[0])

num = 0

for i in range(ord('A'), ord('Z') + 1):
    if chr(i) not in arr:
        break

    num += 1

print(num)