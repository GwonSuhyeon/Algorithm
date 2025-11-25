birth = map(int, input().split())
current = map(int, input().split())

birth_year, birth_month, birth_day = birth
current_year, current_month, current_day = current

if birth_year < current_year:
    age = current_year - birth_year

    if birth_month > current_month or (birth_month == current_month and birth_day > current_day):
        age -= 1
    
    print(age)
else:
    print(0)

print(current_year - birth_year + 1)
print(current_year - birth_year)