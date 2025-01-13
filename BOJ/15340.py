while True:
    c, d = map(int, input().split())

    if c == 0 and d == 0:
        break

    ParsTel = c * 30 + d * 40
    ParsCell = c * 35 + d * 30
    ParsPhone = c * 40 + d * 20

    print(min(ParsTel, ParsCell, ParsPhone))