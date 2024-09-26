M = int(input())
D = int(input())

if M == 1:
    print('Before')
elif M == 2 and D < 18:
    print('Before')
elif M == 2 and D == 18:
    print('Special')
else:
    print('After')