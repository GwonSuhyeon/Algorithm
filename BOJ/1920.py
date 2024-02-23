n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = map(int, input().split())

res = []

for i in b:
    if i in a:
        res.append(1)
    
    else:
        res.append(0)

for i in res:
    print(i)





### 이분 탐색 시간초과 ###

# n = int(input())
# a = sorted(map(int, input().split()))
# m = int(input())
# b = map(int, input().split())

# res = []

# length = len(a)
# mid = length // 2

# for i in b:
#     idx = mid
    
#     while True:
        
#         if idx <= 0 or idx >= (length - 1):
#             if a[idx] == i:
#                 res.append(1)
            
#             else:
#                 res.append(0)
            
#             break
        
#         if a[idx] == i:
#             res.append(1)
            
#             break
        
#         elif a[idx] < i:
#             idx = (idx + length) // 2
        
#         elif a[idx] > i:
#             idx = idx // 2

# for i in res:
#     print(i)