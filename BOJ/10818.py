n = int(input())

s = input().split()
s = list(map(int, s))

print(str(min(s)) + ' ' + str(max(s)))