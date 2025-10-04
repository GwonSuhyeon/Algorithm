T = int(input())

for _ in range(T):
    line = input() + ' '

    prev = None
    res = ''
    cnt = 0

    for i in line:
        if prev is None:
            cnt += 1
            prev = i
        else:
            if prev == i:
                cnt += 1
            else:
                res += str(cnt) + prev
                cnt = 1
                prev = i
    
    print(res)