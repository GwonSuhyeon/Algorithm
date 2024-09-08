N = int(input())

score_d, score_p = 0, 0

for _ in range(N):
    S = input()

    if S == 'D':
        score_d += 1
    elif S == 'P':
        score_p += 1
    
    if abs(score_d - score_p) >= 2:
        break

print(f'{score_d}:{score_p}')