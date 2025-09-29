while True:
    line = input()

    if line == '#':
        break
    
    Y = 0
    N = 0
    P = 0
    A = 0

    for i in line:
        if i == 'Y':
            Y += 1
        elif i == 'N':
            N += 1
        elif i == 'P':
            P += 1
        elif i == 'A':
            A += 1
    
    if A >= (Y + N + P):
        print('need quorum')
    elif Y == N:
        print('tie')
    elif Y > N:
        print('yes')
    elif Y < N:
        print('no')