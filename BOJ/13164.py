import sys


input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

arr = list(map(int, input().rstrip().split()))

diff = []

for i in range(len(arr) - 1):
    diff.append(abs(arr[i] - arr[i + 1]))

diff = sorted(diff)

end = len(diff) - (K - 1)

print(sum(diff[:end]))