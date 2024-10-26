T = int(input())

for _ in range(T):
    S = input()

    mid = (len(S) // 2) - 1

    if S[mid] == S[mid + 1]:
        print('Do-it')
    else:
        print('Do-it-Not')