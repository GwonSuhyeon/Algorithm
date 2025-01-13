N = input()

if int(N[-1]) == 0 and int(N[-2]) > 0:
    A = int(N[:-2])
    B = int(N[-2:])
else:
    A = int(N[:-1])
    B = int(N[-1])

print(A + B)