n, k, a, b = map(int, input().split())

time1 = (n - 1) * a
time2 = ((n - 1) + abs(k - 1)) * b

print(time2, time1)