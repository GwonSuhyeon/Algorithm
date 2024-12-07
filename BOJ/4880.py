while True:
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        break
    
    if b - a == c - b:
        print('AP %d' % (c + (b - a)))
    elif b % a == 0 and c % b == 0 \
        and b // a == c // b:
        print('GP %d' % (c * (b // a)))