arr = ['A', 'E', 'I', 'O', 'U',
       'a', 'e', 'i', 'o', 'u']

S = int(input())

for _ in range(S):
    line = input()

    res1 = 0
    res2 = 0

    for i in line:
        if i not in arr and i != ' ':
            res1 += 1
        elif i in arr:
            res2 += 1
    
    print(res1, res2)