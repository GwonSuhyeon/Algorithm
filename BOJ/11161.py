T = int(input())

for _ in range(T):
    M = int(input())

    people = 0
    res = 0

    for _ in range(M):
        P1, P2 = map(int, input().split())

        people += (P1 - P2)

        if people < 0:
            res += abs(people)
            people = 0
    
    print(res)