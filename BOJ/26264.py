N = int(input())
S = input()

bigdata = S.count('bigdata')
security = S.count('security')

if bigdata > security:
    print('bigdata?')
elif security > bigdata:
    print('security!')
else:
    print('bigdata? security!')