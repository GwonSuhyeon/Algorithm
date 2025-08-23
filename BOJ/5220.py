T = int(input())

for _ in range(T):
    number, check_bit = map(int, input().split())
    
    bit = []
    
    while number > 0:
        bit.append(number % 2)
        number //= 2
    
    if bit.count(1) % 2 == 0:
        res = 0
    else:
        res = 1
    
    if res == check_bit:
        print('Valid')
    else:
        print('Corrupt')