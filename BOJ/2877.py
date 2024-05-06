from collections import deque


K = int(input()) + 1

binary = deque()

res = ''

while K > 0:
    binary.appendleft(K % 2)
    K //= 2

binary.popleft()

while len(binary):
    num = binary.popleft()
    
    if num == 0:
        res += '4'
    
    elif num == 1:
        res += '7'

print(res)