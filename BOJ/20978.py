N, M = map(int, input().split())
arr1 = set(map(int, input().split()))
arr2 = set(map(int, input().split()))

for i in sorted(arr1 & arr2):
    print(i)