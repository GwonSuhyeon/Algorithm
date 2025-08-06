while True:
    employee = int(input())
    
    if employee == 0:
        break
    
    if 1000000 < employee <= 5000000:
        employee -= int(employee * 0.1)
    elif employee > 5000000:
        employee -= int(employee * 0.2)
    
    print(employee)