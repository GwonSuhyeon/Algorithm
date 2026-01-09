from collections import Counter


line = input()
line_count = Counter(line).values()

odd_cnt = 0

for i in line_count:
    if i % 2 != 0:
        odd_cnt += 1

if odd_cnt > 1:
    print(odd_cnt - 1)
else:
    print(0)