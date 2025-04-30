S = input()

res = 1

if S[0] in ['a', 'e', 'i', 'o', 'u']:
    vowel = True
else:
    vowel = False

for s in S[1:]:
    if s in ['a', 'e', 'i', 'o', 'u']:
        if vowel == False:
            vowel = True
        else:
            res = 0
            break
    else:
        if vowel == True:
            vowel = False
        else:
            res = 0
            break

print(res)