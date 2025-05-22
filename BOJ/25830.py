MM, SS = map(int, input().split(':'))

HMS = (MM * 60) + SS
hms = (MM * 3600) + (SS * 60)

res = hms - HMS

print(f'{(res // 3600):02}:{((res % 3600) // 60):02}:{(res % 60):02}')