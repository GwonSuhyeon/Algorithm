min_t = 99999
max_t = -99999

while True:
    try:
        t = list(map(int, input()[10:].split()))

        min_t = min(*t, min_t)
        max_t = max(*t, max_t)

    except:
        break

print(min_t, max_t)