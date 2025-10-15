while True:
    n = int(input())

    if n == 0:
        break

    arr = list(map(int, input().split()))
    reverse_arr = []
    temp = {}

    ambiguous = True

    for idx, i in enumerate(arr):
        temp[i] = idx + 1
    
    temp = sorted(temp.items())
    
    for key, value in temp:
        reverse_arr.append(value)
    
    for i, k in zip(arr, reverse_arr):
        if i != k:
            ambiguous = False
            
            break
    
    if ambiguous == True:
        print('ambiguous')
    else:
        print('not ambiguous')