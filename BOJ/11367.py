T = int(input())

for _ in range(T):
    name, score = input().split()
    
    score = int(score)
    
    if 97 <= score <= 100:
        grade = 'A+'
    elif 90 <= score <= 96:
        grade = 'A'
    elif 87 <= score <= 89:
        grade = 'B+'
    elif 80 <= score <= 86:
        grade = 'B'
    elif 77 <= score <= 79:
        grade = 'C+'
    elif 70 <= score <= 76:
        grade = 'C'
    elif 67 <= score <= 69:
        grade = 'D+'
    elif 60 <= score <= 66:
        grade = 'D'
    else:
        grade = 'F'
    
    print(f'{name} {grade}')