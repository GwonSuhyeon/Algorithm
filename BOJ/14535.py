Case = 1

while True:
    T = int(input())

    if T == 0:
        break
    
    birthday = {'Jan': 0, 'Feb': 0, 'Mar': 0,
                'Apr': 0, 'May': 0, 'Jun': 0,
                'Jul': 0, 'Aug': 0, 'Sep': 0,
                'Oct': 0, 'Nov': 0, 'Dec': 0}
    
    month = list(birthday.keys())
    
    for _ in range(T):
        d, m, y = map(int, input().split())

        birthday[month[m - 1]] += 1
    
    print(f'Case #{Case}:')
    for key, value in birthday.items():
        cnt = '*' * value
        print(f'{key}:{cnt}')
    
    Case += 1