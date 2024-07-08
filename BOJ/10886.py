N = int(input())

cute = 0
not_cute = 0

for _ in range(N):
    value = int(input())
    
    if value == 0:
        not_cute += 1
    
    else:
        cute += 1

if cute > not_cute:
    print('Junhee is cute!')

else:
    print('Junhee is not cute!')