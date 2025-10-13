A, B = map(int, input().split())

if A == B:
    print(B)
else:
    while A != B:
        A_temp = A
        A = max(A, B) - min(A, B)
        B = min(A_temp, B)
    
    print(B)