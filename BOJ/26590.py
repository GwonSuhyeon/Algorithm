A, B = input().split()

res = []
idx = 0

while len(res) < len(A):
    if idx % 2 == 0:
        res.append(A[idx])
    
    else:
        res.append(B[idx])
    
    idx += 1

print(''.join(res))