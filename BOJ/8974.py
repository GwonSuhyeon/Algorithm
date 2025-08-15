A, B = map(int, input().split())

arr = [i for i in range(1, 1001) for _ in range(i)]

print(sum(arr[A - 1:B]))