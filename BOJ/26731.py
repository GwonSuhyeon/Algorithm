S = set(input())

alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

for i in alphabet:
    if i not in S:
        print(i)

        break