A, B = map(int, input().split())

arr = [i + 1 for i in range(1000) for _ in range(i + 1)]

print(sum(arr[A - 1:B]))