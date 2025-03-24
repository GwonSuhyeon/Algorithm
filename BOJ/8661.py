x, k, a = map(int, input().split())

k_pos = 0
a_pos = x % (k + a)

while True:
    k_pos += k

    if k_pos > a_pos:
        print(1)
        break
    
    a_pos -= a

    if a_pos < k_pos:
        print(0)
        break