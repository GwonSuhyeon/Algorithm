M, N = map(int, input().split())

eng = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
arr = []

for i in range(M, N + 1):
    temp = []
    temp.append(i)
    
    s = ''
    
    for k in list(str(i)):
        s += eng[int(k)]
        s += ' '
    
    temp.append(s.rstrip())
    
    arr.append(temp)

arr = sorted(arr, key=lambda x : x[1])

for idx, i in enumerate(arr):
    if (idx + 1) % 10 == 0:
        print(i[0])
    
    else:
        print(i[0], end=' ')