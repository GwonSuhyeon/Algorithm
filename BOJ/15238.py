from collections import defaultdict


size = int(input())
text = input()

text_cnt = defaultdict(int)

for i in text:
    text_cnt[i] += 1

res = ['', 0]

for key, value in text_cnt.items():
    if res[1] < value:
        res[0] = key
        res[1] = value

print(res[0], res[1])