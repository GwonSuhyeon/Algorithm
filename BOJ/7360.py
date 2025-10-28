while True:
    n = int(input())

    if n == 0:
        break

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A_score = 0
    B_score = 0

    for a, b in zip(A, B):
        if a == b:
            continue

        if a + b == 3:
            if a < b:
                A_score += 6
            else:
                B_score += 6
        elif abs(a - b) == 1:
            if a < b:
                A_score += (a + b)
            else:
                B_score += (a + b)
        else:
            if a > b:
                A_score += a
            else:
                B_score += b
    
    print(f'A has {A_score} points. B has {B_score} points.', end='\n\n')