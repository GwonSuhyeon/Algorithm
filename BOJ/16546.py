N = int(input())

runner = list(map(int, input().split()))

arr = [i for i in range(1, N + 1)]

print(*(set(arr) - set(runner)))