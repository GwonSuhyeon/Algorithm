length = int(input())
s = input()

cnt_2 = 0
cnt_e = 0

for i in s:
    if i == '2':
        cnt_2 += 1
    elif i == 'e':
        cnt_e += 1

if cnt_2 == cnt_e:
    print('yee')
elif cnt_2 > cnt_e:
    print(2)
else:
    print('e')