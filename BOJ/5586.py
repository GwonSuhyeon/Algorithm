S = input()

joi = 0
ioi = 0

for i in range(len(S) - 2):
    s = S[i:i+3]
    if s == 'JOI':
        joi += 1
    elif s == 'IOI':
        ioi += 1

print(joi)
print(ioi)