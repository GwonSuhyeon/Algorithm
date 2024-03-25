N = int(input())

tree = [list(map(int, input().split())) for _ in range(N)]

for i in range(N - 2, -1, -1):
    for k in range(len(tree[i])):
        tree[i][k] += max(tree[i + 1][k], tree[i + 1][k + 1])

print(tree[0][0])