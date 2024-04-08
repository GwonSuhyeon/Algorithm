N = int(input())

arr = list(map(int, input().split()))
arr = sorted(arr)

res = []

front = 0
back = len(arr) - 1

minimum = 10000000000

while front < back:
    temp = arr[front] + arr[back]
    abs_temp = abs(temp)
    
    if abs_temp < minimum:
        minimum = abs_temp
        res = [arr[front], arr[back]]
        
    if temp > 0:
        back -= 1
    
    elif temp < 0:
        front += 1
    
    else:
        break

res = sorted(res)

print(res[0], res[1])