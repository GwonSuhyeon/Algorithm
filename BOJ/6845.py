n = int(input())

for _ in range(n):
    y, m, d = map(int, input().split())
    
    age = 2007 - y
    if age > 18:
        print('Yes')
    elif age < 18:
        print('No')
    else:
        if m < 2:
            print('Yes')
        elif m > 2:
            print('No')
        else:
            if d <= 27:
                print('Yes')
            else:
                print('No')