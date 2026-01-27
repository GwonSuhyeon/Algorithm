T = int(input())

for _ in range(T):
    l_t, w_t, l_e, w_e = map(int, input().split())

    a_t = l_t * w_t
    a_e = l_e * w_e

    if a_t > a_e:
        print('TelecomParisTech')
    elif a_t < a_e:
        print('Eurecom')
    else:
        print('Tie')