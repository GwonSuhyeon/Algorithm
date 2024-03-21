from collections import deque


def rotation(left_wheel, center_wheel, right_wheel, center_direction, recursive):
    if left_wheel == None: pass
    else:
        if wheel[left_wheel][2] == wheel[center_wheel][6]: pass
        else:
            if left_wheel > 1:
                rotation(left_wheel - 1, left_wheel, None, cw if center_direction == ccw else ccw, True)
            
            if center_direction == cw:
                wheel[left_wheel].append(wheel[left_wheel].popleft()) # ccw
            elif center_direction == ccw:
                wheel[left_wheel].appendleft(wheel[left_wheel].pop()) # cw
    
    if right_wheel == None: pass
    else:
        if wheel[center_wheel][2] == wheel[right_wheel][6]: pass
        else:
            if right_wheel < 4:
                rotation(None, right_wheel, right_wheel + 1, cw if center_direction == ccw else ccw, True)
            
            if center_direction == cw:
                wheel[right_wheel].append(wheel[right_wheel].popleft()) # ccw
            elif center_direction == ccw:
                wheel[right_wheel].appendleft(wheel[right_wheel].pop()) # cw
    
    if recursive == False:
        if center_direction == cw:
            wheel[center_wheel].appendleft(wheel[center_wheel].pop()) # cw
        elif center_direction == ccw:
            wheel[center_wheel].append(wheel[center_wheel].popleft()) # ccw

cw = 1
ccw = -1
N = 0
S = 1

wheel = [deque()]

res = 0

for _ in range(4):
    wheel.append(deque(int(i) for i in list(input())))

K = int(input())

for _ in range(K):
    wheel_num, direction = map(int, input().split())
    
    left = wheel_num - 1
    center = wheel_num
    right = wheel_num + 1
    
    if center == 1:
        rotation(None, center, right, direction, False)
    elif center == 4:
        rotation(left, center, None, direction, False)
    else:
        rotation(left, center, right, direction, False)

res += 0 if wheel[1][0] == N else 1
res += 0 if wheel[2][0] == N else 2
res += 0 if wheel[3][0] == N else 4
res += 0 if wheel[4][0] == N else 8

print(res)