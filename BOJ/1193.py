x = int(input())

cnt = 0
step = 1

while x > cnt:
    cnt += step
    step += 1

if (step - 1) % 2 == 0:
    upper = (step - 1) - (cnt - x)
    lower = (cnt - x) + 1

else:
    upper = (cnt - x) + 1
    lower = (step - 1) - (cnt - x)

print(f'{upper}/{lower}')




### 시간 초과 ###

# X = int(input())

# direction = [(0, 1), (1, -1), (1, 0), (-1, 1)]
# dir_selector = 0

# x, y = 0, 0

# for i in range(X):
    
#     if i == 0:
#         continue
    
#     dir = dir_selector % 4
    
#     if dir == 0 or dir == 2:
#         dir_selector += 1
        
#         x += direction[dir][0]
#         y += direction[dir][1]
    
#     else:
#         if (x + direction[dir][0]) < 0 or (y + direction[dir][1]) < 0:
#             dir_selector += 1
            
#         else:
#             x += direction[dir][0]
#             y += direction[dir][1]
            
#             if (x + direction[dir][0]) < 0 or (y + direction[dir][1]) < 0:
#                 dir_selector += 1

# print(f'{x + 1}/{y + 1}')