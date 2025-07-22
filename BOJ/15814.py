S = list(input())
T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    
    temp = S[A]
    S[A] = S[B]
    S[B] = temp

print(''.join(S))