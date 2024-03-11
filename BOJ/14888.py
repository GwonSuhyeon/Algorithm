def back_tracking(sum, idx):

    if idx == N:
        res.append(sum)
        
        return
        
    for i in range(4):
        if operator[i] > 0:
            value = 0
            
            operator[i] -= 1
            
            curr_digit = arr[idx]
            next_digit_idx = idx + 1
            
            if i == 0:
                value = sum + curr_digit
            
            elif i == 1:
                value = sum - curr_digit
                
            elif i == 2:
                value = sum * curr_digit
            
            elif i == 3:
                if sum < 0:
                    value = int(abs(sum) / curr_digit) * -1
                
                else:
                    value = int(sum / curr_digit)
            
            back_tracking(value, next_digit_idx)
            
            operator[i] += 1

N = int(input())

arr = list(map(int, input().split()))
operator = list(map(int, input().split()))

res = []

back_tracking(arr[0], 1)

print(max(res))
print(min(res))