while True:
	a, b = input().split()

	if a == '0' and b == '0':
		break
	
	a = a[::-1]
	b = b[::-1]

	if len(a) > len(b):
		b += ('0' * (len(a) - len(b)))
	elif len(a) < len(b):
		a += ('0' * (len(b) - len(a)))

	res = 0
	prev = 0

	for i in range(len(a)):
		if int(a[i]) + int(b[i]) + prev >= 10:
			res += 1
			prev = 1
		else:
			prev = 0
    
	print(res)
