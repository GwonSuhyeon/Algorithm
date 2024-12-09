while True:
    start_time, end_time = map(str, input().split())
    start_h, start_m = map(int, start_time.split(':'))
    end_h, end_m = map(int, end_time.split(':'))

    if start_h == 0 and start_m == 0 and end_h == 0 and end_m == 0:
        break
    
    h = start_h + end_h
    m = start_m + end_m
    day = 0

    if m >= 60:
        h += 1
    
    if h // 24 >= 1:
        day += h // 24
    
    if day > 0:
        print(f'{h % 24:02}:{m % 60:02} +{day}')
    else:
        print(f'{h % 24:02}:{m % 60:02}')