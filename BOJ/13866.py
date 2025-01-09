level = list(map(int, input().split()))

print(abs(2 * (max(level) + min(level)) - sum(level)))