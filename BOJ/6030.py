P, Q = map(int, input().split())

p = [P // i for i in range(P, 0, -1) if P % i == 0]
q = [Q // i for i in range(Q, 0, -1) if Q % i == 0]

for p_i in p:
    for q_i in q:
        print(p_i, q_i)