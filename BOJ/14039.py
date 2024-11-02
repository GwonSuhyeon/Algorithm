arr = []

magic_num_row = []
magic_num_col = []

for i in range(4):
    arr.append(list(map(int, input().split())))
    magic_num_row.append(sum(arr[i]))

for i in range(4):
    num = arr[0][i] + arr[1][i] + arr[2][i] + arr[3][i]
    magic_num_col.append(num)

if max(magic_num_row) != min(magic_num_row):
    print('not magic')
elif max(magic_num_col) != min(magic_num_col):
    print('not magic')
else:
    print('magic')