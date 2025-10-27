arr = {'b': 'd', 'd': 'b', 'q': 'p', 'p': 'q',
       'i': 'i', 'o': 'o', 'v': 'v', 'w': 'w', 'x': 'x'}

while True:
    word = input()

    if word == '#':
        break

    res = ''

    for i in word[::-1]:
        if i in arr.keys():
            res += arr[i]
        else:
            res = 'INVALID'

            break
    
    print(res)