T = int(input())

for _ in range(T):
    arr = list(map(int, input().split()))

    even = 0
    odd = 0

    for i in arr[1:]:
        if i % 2 == 0:
            even += i
        else:
            odd += i
    
    if even > odd:
        print('EVEN')
    elif even < odd:
        print('ODD')
    else:
        print('TIE')