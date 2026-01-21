R, C, N = map(int, input().split())

row = ((R + N) - 1) // N
col = ((C + N) - 1) // N

res = row * col

print(res)