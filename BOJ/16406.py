k = int(input())
answer1 = input()
answer2 = input()

num = 0

for a, b in zip(answer1, answer2):
    if a == b:
        num += 1

res = min(num, k) + min(len(answer1) - num, len(answer1) - k)

print(res)