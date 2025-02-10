A, B, C = map(int, input().split())

res = [
	A * B * C,
	A * B,
	A * C,
	B * C,
	A,
	B,
	C
	]

odd = [i for i in res if i % 2 == 1]

if len(odd) == 0:
	print(max(res))
else:
	print(max(odd))