A, B = input().split()

a_idx = len(A) - 1
b_idx = len(B) - 1

res = ''

while a_idx >= 0 or b_idx >= 0:
    a, b = 0, 0
    
    if a_idx >= 0:
        a = int(A[a_idx])
        a_idx -= 1
    
    if b_idx >= 0:
        b = int(B[b_idx])
        b_idx -= 1
    
    res = str(a + b) + res

print(res)