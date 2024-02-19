s = input()

res = 0

if list(s).count('1') == 0 or list(s).count('0') == 0:
    res = 0

else:
    one = [i for i in s.split('0') if len(i) != 0]
    zero = [i for i in s.split('1') if len(i) != 0]

    if len(one) <= len(zero):
        res = len(one)
    else:
        res = len(zero)

print(res)