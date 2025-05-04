N = int(input())

st = input()

for i in range(N):
    st_small = st[i:]

    s = st_small.count('s')
    t = st_small.count('t')

    if s == t:
        print(st_small)
        break