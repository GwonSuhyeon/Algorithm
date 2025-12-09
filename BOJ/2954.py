line = input()

p_flag = False

for i in line:
    if p_flag == False:
        print(i, end='')
    
    if i in {'a', 'e', 'i', 'o', 'u'}:
        if p_flag == True:
            p_flag = False
        else:
            p_flag = True