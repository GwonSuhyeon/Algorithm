N = int(input())
arr = list(map(int, input().split()))

maximum_idx = arr.index(max(arr))

print(sum(arr[:maximum_idx]))
print(sum(arr[(maximum_idx + 1):]))