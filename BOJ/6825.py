weight = float(input())
height = float(input())

bmi = weight / (height ** 2)

if bmi > 25.0:
    print('Overweight')
elif 18.5 <= bmi <= 25.0:
    print('Normal weight')
else:
    print('Underweight')