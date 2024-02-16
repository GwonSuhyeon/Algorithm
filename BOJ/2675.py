n = int(input())

for _ in range(n):
    r, s = map(str, input().split())

    res = ''

    r = int(r)
    s = list(s)
    
    for i in s:
        res += i * r
    
    print(res)