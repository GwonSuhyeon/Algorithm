while True:
    n = int(input())

    if n == -1:
        break

    res = set()

    for i in range(1, n // 2 + 1):
        if i not in res:
            if n % i == 0:
                res.add(i)
    
    if sum(res) == n:
        text = ' + '.join(map(str, sorted(res)))
        print(f'{n} = {text}')
    else:
        print(f'{n} is NOT perfect.')