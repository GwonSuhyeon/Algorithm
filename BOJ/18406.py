N = input()

left = 0
right = 0

for idx, i in enumerate(N):
    if idx < (len(N) // 2):
        left += int(i)
    else:
        right += int(i)

if left == right:
    print('LUCKY')
else:
    print('READY')