T = int(input())

for _ in range(T):
    hp, mp, att, defe, hp2, mp2, att2, defe2 = map(int, input().split())

    hp += hp2
    mp += mp2
    att += att2
    defe += defe2

    if hp < 1:
        hp = 1
    
    if mp < 1:
        mp = 1
    
    if att < 0:
        att = 0
    
    res = 1 * hp + 5 * mp + 2 * att + 2 * defe

    print(res)