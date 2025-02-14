n = int(input())
prize = list(map(int, input().split()))

if sum(prize) % 3 == 0:
    print('yes')
else:
    print('no')