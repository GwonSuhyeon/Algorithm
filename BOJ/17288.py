# S = input()

# res = 0
# idx = 0

# while idx <= (len(S) - 3):
#     if int(S[idx]) == int(S[idx + 1]) - 1 and int(S[idx + 1]) == int(S[idx + 2]) - 1:
#         res += 1
        
#         cnt = 0
#         while (idx + 3) < len(S) and int(S[idx + 1]) == int(S[idx + 2]) - 1 and int(S[idx + 2]) == int(S[idx + 3]) - 1:
#             idx += 1
#         idx += 3
#         # continue
    
#     idx += 1

# print(res)




S = input()

num = None
res = 0
arr = []

for i in S:
    if num is None:
        num = int(i)
        arr.append(int(i))
    
    else:
        if int(i) - num == 1:
            arr.append(int(i))
        
        else:
            if len(arr) == 3:
                res += 1
            
            # else:
            # num = None
            arr.clear()
            
            arr.append(int(i))
        
        num = int(i)

if len(arr) == 3:
    res += 1

print(res)