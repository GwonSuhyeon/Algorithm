s = input().split()
s = ''.join(s)

ascending = '12345678'
descending = '87654321'

if s == ascending:
    print('ascending')

elif s == descending:
    print('descending')

else:
    print('mixed')