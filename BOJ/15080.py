h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

time1 = 3600 * h1 + 60 * m1 + s1
time2 = 3600 * h2 + 60 * m2 + s2

if time1 > time2:
    time2 += (3600 * 24)

print(abs(time1 - time2))