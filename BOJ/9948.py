month = {'January': 1, 'February': 2, 'March': 3,
         'April': 4, 'May': 5, 'June': 6,
         'July': 7, 'August': 8, 'September': 9,
         'October': 10, 'November': 11, 'December': 12}

while True:
    d, m = input().split()
    d = int(d)

    if m == '#':
        break

    if month[m] == 2 and d == 29:
        print('Unlucky')
    elif month[m] < 8:
        print('Yes')
    elif month[m] == 8 and d < 4:
        print('Yes')
    elif month[m] == 8 and d == 4:
        print('Happy birthday')
    else:
        print('No')