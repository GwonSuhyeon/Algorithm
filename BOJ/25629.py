N = int(input())

arr = sorted(list(map(int, input().split())))

odd_even = [0 for _ in range(N)]

odd_idx = 0
even_idx = 1

res = 1

for idx, i in enumerate(arr):
    if i % 2 != 0:
        if odd_idx < N:
            odd_even[odd_idx] = i
            odd_idx += 2
        else:
            break
    else:
        if even_idx < N:
            odd_even[even_idx] = i
            even_idx += 2
        else:
            break

for i in odd_even:
    if i == 0:
        res = 0

print(res)