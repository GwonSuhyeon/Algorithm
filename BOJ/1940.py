N = int(input())
M = int(input())
arr = sorted(list(map(int, input().split())))

front = 0
back = len(arr) - 1

res = 0

while True:
    if front >= back:
        break
    
    if (arr[front] + arr[back]) == M:
        res += 1
        front += 1
        back -= 1
    
    elif (arr[front] + arr[back]) > M:
        back -= 1
    
    elif (arr[front] + arr[back]) < M:
        front += 1

print(res)