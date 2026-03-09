N = int(input())
S = input()

res = 0

for i in range(N):
    if i % 2 == 0:
        ioi = 'I'
    else:
        ioi = 'O'
    
    if ioi != S[i]:
        res += 1

print(res)