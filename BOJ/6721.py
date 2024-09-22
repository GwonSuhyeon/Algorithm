N = int(input())

for _ in range(N):
    a, b = input().split()

    backward_a = int(a[::-1])
    backward_b = int(b[::-1])

    res = str(backward_a + backward_b)

    backward_res = int(res[::-1])

    print(backward_res)