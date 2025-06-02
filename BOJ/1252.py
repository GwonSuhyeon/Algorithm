A, B = input().split()

res = []

A_binary = 0
B_binary = 0

for i, bit in enumerate(A[::-1]):
    if bit == '1':
        A_binary += 2**i

for i, bit in enumerate(B[::-1]):
    if bit == '1':
        B_binary += 2**i

C = A_binary + B_binary

while True:
    if C < 1:
        break
    
    res.append(str(C % 2))
    
    C //= 2

if not res:
    print(0)
else:
    print(''.join(res)[::-1])