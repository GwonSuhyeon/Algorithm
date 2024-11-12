N = int(input())

ans = [((i - 1) % 5) + 1 for i in range(1, N + 1)]

for i in range(1, N + 1):
    student = list(map(int, input().split()))

    same = True

    for a, s in zip(ans, student):
        if a != s:
            same = False

            break
    
    if same == True:
        print(i)