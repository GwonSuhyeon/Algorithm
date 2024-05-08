N = int(input())

arr = sorted(list(map(int, input().split())))

X = int(input())

front = 0
back = N - 1

res = 0

while True:
    if front >= back:
        break
    
    num = arr[front] + arr[back]
    
    if num == X:
        res += 1
        
        front += 1
        back -= 1
    
    elif num > X:
        back -= 1
    
    elif num < X:
        front += 1

print(res)