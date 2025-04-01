res = 0

while True:
    try:
        s = input()

        if len(s) > 0:
            res += 1
    except:
        break

print(res)